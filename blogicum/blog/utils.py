from typing import Union
from django.http import Http404


def get_object_by_id_or_404(
        posts: dict[int, dict[str, Union[str, int]]],
        pk: int
) -> dict:
    try:
        return posts[pk]
    except KeyError:
        raise Http404('Page not found.')
