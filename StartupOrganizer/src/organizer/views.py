import json

from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views import View  # required to use class views

from .models import Tag


class TagApiDetail(View):
    def get(self, request, pk):
        # request object from database
        tag = get_object_or_404(Tag, pk=pk)
        # create a json
        tag_json = json.dumps(dict(id=tag.pk, name=tag.name, slug=tag.slug,))
        return HttpResponse(tag_json, content_type="application/json")


class TagApiList(View):
    def get(self, request):
        tag_list = get_list_or_404(Tag)
        tag_json = json.dumps(
            [dict(id=tag.pk, name=tag.name, slug=tag.slug,) for tag in tag_list]
        )
        return HttpResponse(tag_json, content_type="application/json")
