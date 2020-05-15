from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework.renderers import JSONRenderer
# from django.views import View
from .serializers import TagSerializer
from .models import Tag


class TagApiDetail(APIView):
    def get(self, request, pk):
        # request object from database
        tag = get_object_or_404(Tag, pk=pk)
        s_tag = TagSerializer(tag, context={"request": request},)
        # create a json
        return Response(s_tag.data)


class TagApiList(APIView):
    def get(self, request):
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(tag_list, many=True, context={"request": request},)

        return Response(s_tag.data)
