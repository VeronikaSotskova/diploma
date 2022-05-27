from rest_framework.pagination import PageNumberPagination


class PaginationSerializer(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return {
            'next_page': self.page.next_page_number() if self.page.has_next() else None,
            'prev_page': self.page.previous_page_number() if self.page.has_previous() else None,
            'page_count': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'start_count': self.page.start_index(),
            'end_count': self.page.end_index(),
            'results': data,
            'curr_page': self.page.number
        }
