from rest_framework import serializers
from .models import EsapBaseObject, DataSet, Archive, Catalog, CatalogService, RetrievalParameters
import logging

logger = logging.getLogger(__name__)

class AdexBaseObjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = EsapBaseObject
        fields = "__all__"


# this is a serializer that uses hyperlinks to produce a navigable REST API
class DataSetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = DataSet
        fields = "__all__"


# this is a serializer that uses uri's in the datasets for easier identification for the frontend
class DataSetModelSerializer(serializers.ModelSerializer):

    # show the uri of the archive (
    data_archive = serializers.StringRelatedField(
        many=False,
        required=False,
    )

    class Meta():
        model = DataSet
        # fields = "__all__"
        fields = ('id', 'uri', 'name', 'short_description','long_description', 'retrieval_description', 'thumbnail',
                   'documentation_url', 'data_archive', 'archive_name_derived','archive_name_derived',
                  'archive_uri_derived','catalog_name_derived')


# this is a serializer that uses hyperlinks to produce a navigable REST API
class ArchiveSerializer(serializers.HyperlinkedModelSerializer):

    datasets = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        # read_only=False
        # queryset=DataSet.objects.all(),
        view_name='dataset-detail',
        lookup_field='pk',
        required=False
    )

    class Meta():
        model = Archive

       # note: 'datasets' is a special field, it is the 'datasets.data_archive' relationship also serialized in Archive
        fields = ('id', 'uri', 'name', 'short_description', 'long_description', 'retrieval_description', 'thumbnail',
                   'documentation_url','instrument','catalog_name_derived','catalog_url_derived','institute','datasets',
                  'archive_catalog')


# this is a serializer that uses uri's in the datasets for easier identification for the frontend
class ArchiveModelSerializer(serializers.ModelSerializer):

    datasets = serializers.StringRelatedField(
        many=True,
        required=False,
    )

    class Meta():
        model = Archive

        # note: "__all__" cannot be ussed because the id is also used in the frontend, and not automatically returned
        # note: 'datasets' is a special field, it is the 'datasets.data_archive' relationship also serialized in Archive
        fields = ('id', 'uri', 'name', 'short_description', 'long_description', 'retrieval_description', 'thumbnail',
                   'documentation_url','instrument','catalog_name_derived','catalog_url_derived','institute','datasets')


# this is a serializer that uses hyperlinks to produce a navigable REST API
class CatalogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = Catalog
        fields = "__all__"


# this is a serializer that uses hyperlinks to produce a navigable REST API
class CatalogServiceSerializer(serializers.HyperlinkedModelSerializer):
    parameters = serializers.StringRelatedField(
        many=True,
        required=False,
    )

    class Meta():
        model = CatalogService
        fields =  ('id', 'uri', 'name', 'thumbnail', 'parameters')


# this is a serializer that uses hyperlinks to produce a navigable REST API
class RetrievalParametersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta():
        model = RetrievalParameters
        fields = "__all__"