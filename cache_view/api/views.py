from django.test import testcases
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.decorators import api_view, throttle_classes, action
from asgiref.sync import sync_to_async


class ExampleView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        content = {"status": "request was permitted"}
        return Response(content)


@api_view(["GET"])
@throttle_classes([UserRateThrottle])
def example_view(request, format=None):
    content = {"status": "request was permitted"}
    return Response(content)


@action(detail=True, methods=["post"], throttle_classes=[UserRateThrottle])
def example_adhoc_method(request, pk=None):
    content = {"status": "request was permitted"}
    return Response(content)


from rest_framework import status
from rest_framework.generics import GenericAPIView
from utils import ConcurrencyThrottleApiKey


class DjangoThrottlingAPIView(GenericAPIView):
    throttle_classes = [ConcurrencyThrottleApiKey]

    def get(self, request):
        return Response("ok", status=status.HTTP_200_OK)
