from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from rest_framework.response import Response
from urllib.parse import urlparse

from .models import URLMapping
from .serializers import CreateShortURLInputSerializer


class CreateShortURLViewSet(mixins.CreateModelMixin, GenericViewSet):
    model = URLMapping
    queryset = URLMapping.objects.all()
    serializer_class = CreateShortURLInputSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.data["original_url"]
            url = URLMapping.objects.create(original_url=original_url)
            parsed_uri = urlparse(request.build_absolute_uri())
            host = "{uri.scheme}://{uri.netloc}/".format(uri=parsed_uri)
            response = response = {
                "short_url": host + url.short_url,
                "expiration_date": url.expiration_date.date(),
                "success": True,
                "reason": None,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            error_msg = "".join(
                [str(item) for item in serializer.errors["original_url"]]
            )
            response = {
                "short_url": None,
                "expiration_date": None,
                "success": False,
                "reason": error_msg,
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ShortURLRedirectViewSet(GenericViewSet):
    @action(detail=False, methods=["GET"])
    def self(self, request, shortURLstr):
        try:
            query = URLMapping.objects.get(short_url=shortURLstr)
            # Check whether the short url is expired or not
            if now() < query.expiration_date:
                return Response(
                    status=status.HTTP_302_FOUND,
                    headers={"Location": query.original_url},
                )
            else:
                response = {
                    "success": False,
                    "reason": "The short url is expired.",
                }
                return Response(response, status=status.HTTP_410_GONE)
        except Exception:
            response = {
                "success": False,
                "reason": "The short url doesn't exist.",
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
