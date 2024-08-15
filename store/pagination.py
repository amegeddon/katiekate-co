from rest_framework.pagination import PageNumberPagination

class PaginationCustom(PageNumberPagination): 
    page_size =  2 #edit appropiately when product list is complete, currently returning two products per page as db only has 3
    