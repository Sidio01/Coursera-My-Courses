import requests
import json
import sqlite3
from somemart.somemart.models import Item, Review

url_post_item = 'http://127.0.0.1:8000/api/v1/goods/'
url_review_item = 'http://127.0.0.1:8000/api/v1/goods/:id/reviews/'
data_post_item = json.dumps({"title": "Сыр Голландский", "description": "Очень вкусный сыр, да еще и голландский.", "price": 1000
})
data_post_review = json.dumps({
    'text': 'Best. Cheese. Ever.',
    'grade': 9
})
post_item = requests.post(url_post_item, data=data_post_item)
print(json.loads(post_item.text))

# post_review = requests.post(url_review_item, data=data_post_review)
# print(json.loads(post_review.text))