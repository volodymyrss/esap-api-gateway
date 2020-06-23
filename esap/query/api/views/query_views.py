import logging

from rest_framework import generics
from rest_framework.response import Response

from ..services import query_controller
from query.models import DataSet
from . import common_views

logger = logging.getLogger(__name__)

class CreateQueryView(generics.ListAPIView):
    """
    Receive a query and return the results
    examples:
    /esap-api/query/create-query/?esap_target=M51&archive_uri=astron_vo
    /esap-api/query/create-query/?ra=202&dec=46&fov=5
    """
    model = DataSet
    queryset = common_views.get_datasets()

    # override list and generate a custom response
    def list(self, request, *args, **kwargs):

        # read fields from the query

        datasets = common_views.get_datasets()

        # is there a query on archives?
        try:
            archive_uri = self.request.query_params['archive_uri']
            datasets = datasets.filter(dataset_archive__uri=archive_uri)

        except:
            pass

        # is there a query on level?
        try:
            level = self.request.query_params['level']
            datasets = datasets.filter(level=level)

        except:
            pass

        # is there a query on category?
        try:
            category = self.request.query_params['category']
            datasets = datasets.filter(category=category)

        except:
            pass

        # (remove the archive_uri (if present) from the params to prevent it being searched again
        query_params = dict(self.request.query_params)
        try:
            del query_params['archive_uri']
        except:
            pass

        try:
            del query_params['level']
        except:
            pass

        try:
            del query_params['category']
        except:
            pass

        input_results = query_controller.create_query(datasets=datasets, query_params = query_params)

        return Response({
            'query_input': input_results
        })


class RunQueryView(generics.ListAPIView):
    """
    Run a single query on a dataset (catalog) and return the results
    examples:
        /esap-api/query/run-query?dataset=ivoa.obscore&
        query=https://vo.astron.nl/__system__/tap/run/tap/sync?lang=ADQL&REQUEST=doQuery&
        QUERY=SELECT TOP 10 * from ivoa.obscore where target_name='M51'

        /esap-api/query/run-query/?dataset_uri=apertif_observations&query=https://alta.astron.nl/altapi/observations-flat?view_ra=202&view_dec=46&view_fov=5
    """
    model = DataSet
    queryset = DataSet.objects.all()

    # override list and generate a custom response
    def list(self, request, *args, **kwargs):

        # read fields from the query
        #datasets = DataSet.objects.all()

        # required parameters
        try:
            dataset_uri = self.request.query_params['dataset_uri']
            query = self.request.query_params['query']
            dataset = DataSet.objects.get(uri=dataset_uri)

        except Exception as error:
            return Response({
                'error': str(error)
            })


        # optional parameters
        try:
            dataset_name = self.request.query_params['dataset_name']
        except:
            dataset_name = "unknown"

        try:
            access_url = self.request.query_params['access_url']
        except:
            access_url = "unknown"

        query_results = query_controller.run_query(dataset=dataset,
                                                   dataset_name=dataset_name,
                                                   query = query,
                                                   access_url=access_url)

        return Response({
            'query_results': query_results
        })