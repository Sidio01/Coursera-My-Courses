import requests
import json
from datetime import datetime


def calc_age(uid):
    token = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
    age_dict = dict()
    age_list_tuple = []
    request_id = requests.get(f'https://api.vk.com/method/users.get?v=5.71&access_token={token}&user_ids={uid}')
    get_id_new = json.loads(request_id.text)['response'][0]['id']
    request_friends = requests.get(
        f'https://api.vk.com/method/friends.get?v=5.71&access_token={token}&user_id={get_id_new}&fields=bdate')
    friends = json.loads(request_friends.text)
    count_x = friends['response']['count']
    if 'response' in friends.keys():
        for _ in range(count_x):
            if 'bdate' in friends['response']['items'][_].keys():
                if len(friends['response']['items'][_]['bdate'].split('.')) == 3:
                    age = datetime.today().year - int(friends['response']['items'][_]['bdate'].split('.')[2])
                    if age in age_dict:
                        age_dict[age] += 1
                    else:
                        age_dict[age] = 1
        for key in age_dict.keys():
            age_list_tuple.append((key, age_dict[key]))
        return sorted(sorted(age_list_tuple, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    else:
        return 'Error'


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)

# a = calc_age('id158628380')
# print('Denis -', a)
# b = calc_age('id1942953')
# print('Lusya -', b)
