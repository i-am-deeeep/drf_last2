from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MovieListPNPagination(PageNumberPagination):
    page_size=4
    page_size_query_param='size'
class MovieListLOPagination(LimitOffsetPagination):
    default_limit=4
class PlatformListCPagination(CursorPagination):
    page_size=4
    ordering=['name',]
