import requests
import typing as t


URL = 'http://172.21.234.129:8192/query'
HEADERS = {
        'Accept-Version': '1',
        'Content-Type': 'application/json'
    }


def get_response(*args) -> t.Dict:
    payload = ','.join(map(lambda x: f"'{str(x)}'", args))
    sql = f"select * from huntingticket_70.huntingticket_svedeniya({payload})"
    print('Your SQL query:', sql, end='\n')
    # body = {'sql': {'sql': sql}}
    # response = requests.post(url=URL, headers=HEADERS, json=body)
    # response = response.json()
    # return response


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_response('Слава', 'Слава', '7107', '939991'))
