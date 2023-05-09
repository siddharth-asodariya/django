"""cache api urls"""
from django.urls import path
from .views import (
    ExampleView,
    example_adhoc_method,
    example_view,
    DjangoThrottlingAPIView,
)

urlpatterns = [
    path("example/", ExampleView.as_view()),
    path("example-view/", example_view),
    path("example-method/", example_adhoc_method),
    path("", DjangoThrottlingAPIView.as_view(), name="throtling"),
]
