from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate_queryset(queryset, page_size, page_number,):
    """
    Paginates a queryset of models.

    Args:
        queryset (QuerySet): The queryset to paginate.
        page_size (int): The number of items per page.
        page_number (int): The page number to retrieve.

    Returns:
        tuple: A tuple containing the paginated queryset, the current page number,
               and a boolean indicating if there is a next page.
    """
    paginator = Paginator(queryset, page_size)

    try:
        paginated_queryset = paginator.page(page_number)
    except PageNotAnInteger:
        # If page number is not an integer, deliver first page.
        paginated_queryset = paginator.page(1)
        page_number = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_queryset = paginator.page(paginator.num_pages)

    return paginated_queryset
