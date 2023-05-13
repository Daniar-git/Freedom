from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatalogPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100


class AdminPagination(PageNumberPagination):
    max_page_size = 100
    page_size_query_param = 'page_size'
    page_size = 10

    def get_paginated_response(self, data):  # noqa: WPS110
        return Response({
            'count': self.page.paginator.count,
            'results': data,
        })

class ImagePagination(PageNumberPagination):
    max_page_size = 100
    page_size_query_param = 'page_size'
    page_size = 20

    def get_paginated_response(self, data):  # noqa: WPS110
        return Response({
            'count': self.page.paginator.count,
            'results': data,
        })