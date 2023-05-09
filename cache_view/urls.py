"""django_learn URL Configuration"""

from django.contrib import admin
from django.urls import path
from cache_view.views import (
    test_cache,
    test_fragment_cache,
    db_call_count,
    use_iterator,
    bulk_query,
    csv_response,
    lazy_example,
    see_request,
    user_info,
    template_tag_view,
    async_with_sync_view,
)

urlpatterns = [
    path("", test_cache, name="cache-test"),
    path("fragment-cache/", test_fragment_cache, name="fragment-cache-test"),
    path("db-count/", db_call_count, name="db-call-count"),
    path("use_iterator/", use_iterator, name="use_iterator"),
    path("bulk_query/", bulk_query, name="bulk_query"),
    path("csv_response/", csv_response, name="csv_response"),
    path("lazy_example/", lazy_example, name="lazy_example"),
    path("see_request/", see_request),
    path("user_info/", user_info),
    path("tag/", template_tag_view),
    path("async-with-sync-view/", async_with_sync_view),
]


# Multiple admin sites in the same URLconf¶
# You can create multiple instances of the admin site on the same Django-powered website. Create multiple instances of AdminSite and place each one at a different URL.

# In this example, the URLs /basic-admin/ and /advanced-admin/ feature separate versions of the admin site – using the AdminSite instances myproject.admin.basic_site and
# myproject.admin.advanced_site, respectively:

# # urls.py
# from django.urls import path
# from myproject.admin import advanced_site, basic_site

# urlpatterns = [
#     path('basic-admin/', basic_site.urls),
#     path('advanced-admin/', advanced_site.urls),
# ]
# AdminSite instances take a single argument to their constructor, their name, which can be anything you like. This argument becomes the prefix to the URL names for the
# purposes of reversing them. This is only necessary if you are using more than one AdminSite.
