import logging
from urllib.parse import urlparse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from ..models import *
import base64
import json
import time
import datetime
from django.urls import reverse
from django.conf import settings

logger = logging.getLogger(__name__)

import mozilla_django_oidc.utils

# overriding 'absolutify' to be able to log the callback_url.
# TODO: remove this when we get rid of the IAM cors errors
def my_absolutify(request, path):
    callback_url = request.build_absolute_uri(path)
    # callback_url = "https://localhost:8081" + path
    # callback_url = request.build_absolute_uri(reverse('oidc_authentication_callback')).replace('http:','https:')
    logger.info('callback_url built from request %s and path %s = %s', request, path, callback_url)
    return callback_url

mozilla_django_oidc.utils.absolutify = my_absolutify


class EsapQuerySchemaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EsapQuerySchemas to be viewed or edited.
    """

    queryset = EsapQuerySchema.objects.all().order_by("schema_name")
    serializer_class = EsapQuerySchemaSerializer
    permission_classes = [permissions.AllowAny]


class EsapComputeResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EsapComputeResources to be viewed or edited.
    """

    queryset = EsapComputeResource.objects.all().order_by("resource_name")
    serializer_class = EsapComputeResourceSerializer
    permission_classes = [permissions.AllowAny]


class EsapSoftwareRepositoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EsapSoftwareRepositorys to be viewed or edited.
    """

    queryset = EsapSoftwareRepository.objects.all().order_by("repository_name")
    serializer_class = EsapSoftwareRepositorySerializer
    permission_classes = [permissions.AllowAny]


class EsapShoppingItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EsapShoppingItems to be viewed or edited.
    """

    queryset = EsapShoppingItem.objects.all()
    serializer_class = EsapShoppingItemSerializer
    permission_classes = [permissions.AllowAny]


class EsapUserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EsapUserProfiles to be viewed or edited.
    """

    queryset = EsapUserProfile.objects.all().order_by("user_name")
    serializer_class = EsapUserProfileSerializer
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        # Returns nothing if no user_name supplied instead of all

        user_profile = []
        try:
            try:
                id_token = self.request.session["oidc_id_token"]
                access_token = self.request.session["oidc_access_token"]

                # a oidc_id_token has a header, payload and signature split by a '.'
                token = id_token.split('.')

                # when does the id_token expire according to the session?
                oidc_id_token_expiration = self.request.session["oidc_id_token_expiration"]
                now = time.time()
                time_to_expire = round(oidc_id_token_expiration - now)
                id_token_expiration = datetime.datetime.utcfromtimestamp(oidc_id_token_expiration).strftime('%Y-%m-%dT%H:%M:%SZ')

                logger.info('id_token expires in ' + str(time_to_expire) + " seconds")
                logger.info('OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS: ' + str(settings.OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS))

                # add the "===" to avoid an "Incorrect padding" exception
                decoded_payload = base64.urlsafe_b64decode(token[1] + "===")
                decoded_token = json.loads(decoded_payload.decode("UTF-8"))

                uid = uid = urlparse(decoded_token["iss"]).netloc + ':userinfo:' + decoded_token["sub"]
                logger.info('uid = ' + uid)

                aud = decoded_token["aud"]

                user_profile = EsapUserProfile.objects.filter(uid=uid)

                # save the current token to the user_profile (for transport and usage elsewhere)
                for profile in user_profile:
                    profile.oidc_id_token = id_token
                    profile.oidc_access_token = access_token
                    profile.id_token_expiration = id_token_expiration
                    profile.save()

                logger.info('user_profile = ' + str(user_profile))

            except Exception as error:
                logger.error(str(error))
                id_token = None

                # no AAI token found, try basic authentication (dev only)
                try:
                    user = self.request.user
                    user_email = user.email
                    user_profile = EsapUserProfile.objects.filter(user_email=user_email)
                except:
                    pass

            return user_profile

        except AttributeError as e:
            print('ERROR: '+str(e))
            user_name = self.request.query_params.get("user_name", None)
            return EsapUserProfile.objects.filter(user_name=user_name)
