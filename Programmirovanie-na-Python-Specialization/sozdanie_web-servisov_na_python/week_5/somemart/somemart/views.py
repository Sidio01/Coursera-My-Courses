import json

from django import forms
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.utils.decorators import method_decorator
from .models import Item, Review

ADD_ITEM_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 64
        },
        'description': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        },
        'price': {
            'anyOf': [
                {
                    'type': 'integer',
                    'minimum': 1,
                    'maximum': 1000000,
                },
                {
                    'type': 'string',
                    'minLength': 1,
                    'pattern': '^\d+$'
                }
            ]
        },
    },
    'required': ['title', 'description', 'price']
}

POST_REVIEW_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'text': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        },
        'grade': {
            'anyOf': [
                {
                    'type': 'integer',
                    'minimum': 1,
                    'maximum': 10,
                },
                {
                    'type': 'string',
                    'minLength': 1,
                    'pattern': '^\d+$'
                }
            ]
        },
    },
    'required': ['text', 'grade']
}


# class GoodForm(forms.Form):
#     title = forms.CharField(max_length=64)
#     description = forms.CharField(max_length=1024)
#     price = forms.IntegerField(min_value=1, max_value=1000000)
#
#
# class ReviewForm(forms.Form):
#     text = forms.CharField(max_length=1024)
#     grade = forms.IntegerField(min_value=1, max_value=10)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AddItemView(View):
#     """View для создания товара."""
#     def post(self, request):
#         form = GoodForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             Item.objects.create(**cd)
#             return JsonResponse(cd, status=201)
#         return JsonResponse(status=400, data={})


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        try:
            data = json.loads(request.body)
            validate(data, ADD_ITEM_SCHEMA)
            item = Item(title=data['title'],
                        description=data['description'],
                        price=data['price'])
            item.save()
            return JsonResponse({"id": item.id}, status=201)
        except ValueError:
            return JsonResponse({}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
            data = json.loads(request.body)
            validate(data, POST_REVIEW_SCHEMA)
            review = Review(grade=data['grade'],
                            text=data['text'],
                            item=item)
            review.save()
            # form = ReviewForm(request.POST)
            # if form.is_valid():
            #     cd = form.cleaned_data
            #     cd['item'] = item
            #     Review.objects.create(**cd)
            return JsonResponse({"id": review.id}, status=201)
        except ValueError:
            return JsonResponse({}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
        except Item.DoesNotExist:
            return JsonResponse({}, status=404)


class GetItemView(View):
    """View для получения информации о товаре."""

    def get(self, request, item_id):
        try:
            item = Item.objects.prefetch_related('review_set').get(id=item_id)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
        item_dict = model_to_dict(item)
        item_reviews = [model_to_dict(x) for x in item.review_set.all()]
        item_reviews = sorted(
            item_reviews, key=lambda review: review['id'], reverse=True)[:5]
        for review in item_reviews:
            review.pop('item', None)
        item_dict['reviews'] = item_reviews
        return JsonResponse(item_dict, status=200)
