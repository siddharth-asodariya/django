"""helper function related to cache view app"""

from django.db import connections
from .models import SiteVisit


def query_count_all() -> int:
    """count query of database hit"""
    return sum(len(c.queries) for c in connections.all())


def create_or_increment_site_count(path_name: str = ""):
    """create new object of Site count or increment if exists"""
    if SiteVisit.objects.filter(path=path_name).exists():
        visited_count = SiteVisit.objects.get(path=path_name).increment_view_count()
        print("increamented", path_name)
    else:
        SiteVisit.objects.create(path=path_name, view_count=1)
        visited_count = 1
    return visited_count
