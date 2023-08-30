from rest_framework.pagination import PageNumberPagination


class MainPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 50
    page_size_query_param = 'page_size'
