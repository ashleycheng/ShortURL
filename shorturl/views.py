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
