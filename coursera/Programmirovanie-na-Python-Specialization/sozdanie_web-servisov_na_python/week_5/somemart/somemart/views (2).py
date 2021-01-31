import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from jsonschema import validate
from jsonschema.exceptions import ValidationError
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

GET_ITEM_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'rstName': {
            'type': 'string'
        },
        'lastName': {
            'type': 'string'
        },
        'age': {
            'description': 'Age in years',
            'type': 'integer',
            'minimum': 0
        }
    },
    'required': ['rstName', 'lastName']
}


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
            return JsonResponse(data, status=201)
        except ValueError:
            return JsonResponse({}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)


class PostReviewView(View):
    """View для создания отзыва о товаре."""
    def post(self, request, item_id):
        try:
            data = json.loads(request.body)
            validate(data, POST_REVIEW_SCHEMA)
            item = Item.objects.get(id=1)
            print(item)
            return JsonResponse(data, status=201)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
        # except:
        #     return JsonResponse({'errors': exc.message}, status=404)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        # Здесь должен быть ваш код
        return JsonResponse(data, status=200)
