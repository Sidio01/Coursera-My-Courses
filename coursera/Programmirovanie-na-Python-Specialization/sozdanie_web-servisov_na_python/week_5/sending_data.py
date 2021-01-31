"""
Описание задания
В этом задании вам требуется отправить POST запрос на следующий https://datasend.webpython.graders.eldf.ru/submissions/1/

В запросе должен содержаться заголовок Authorization со способом аутентификации Basic логином alladin и паролем
opensesame закодированными в base64.
Authorization: Basic YWxsYWRpbjpvcGVuc2VzYW1l

Запрос можно отправить любым удобным для вас способом, но мы рекомендуем использовать библиотеку requests, так как она
понадобится вам при выполнении последующих заданий.

В ответе на запрос вы получите инструкции для последующего запроса который приведет вас к специальному коду который
является ответом на это задание.
"""
import requests
import json
import base64


url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'
url2 = 'https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/'
header = {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l', 'login': 'alladin', 'password': 'opensesame'}
header2 = {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l', 'login': 'galchonok', 'password': 'ktotama'}
x = 'YWxsYWRpbjpvcGVuc2VzYW1l'
y = b'hello:world'
print(base64.b64decode(x))
print(base64.b64encode(y))

# post = requests.post(url, headers=header)
# post2 = requests.put(url2, auth=('galchonok', 'ktotama'))
# print(json.loads(post.text))
# print()
# print(post2.text)
