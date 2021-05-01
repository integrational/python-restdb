import json
import sys
import requests

# provide restdb.io API Key on command-line
api_key = sys.argv[1]

base_url = 'https://greetings-7eaa.restdb.io/rest'
url = f'{base_url}/greetings'

requ_hs = {
    'x-apikey':      api_key,
    'cache-control': 'no-cache'
}

timeout = 5  # seconds


def pp(d: dict) -> str:
    return json.dumps(d, indent=4)


all_resp = requests.get(url, headers=requ_hs, timeout=timeout)
all_resp.raise_for_status
all_greetings = all_resp.json()
print(f'All greetings: {pp(all_greetings)}')

new_greeting = {'greeter': 'Dagmar',
                'greeted': 'Gerald', 'greeting': 'Ich dich auch!'}
add_resp = requests.post(url, json=new_greeting,
                         headers=requ_hs, timeout=timeout)
add_resp.raise_for_status
added_entry = add_resp.json()
print(f'Added entry: {pp(added_entry)}')

query_resp = requests.get(
    url, params={'q': '{"greeted": "Gerald"}'}, headers=requ_hs, timeout=timeout)
query_resp.raise_for_status
query_result = query_resp.json()
print(f'Query result: {pp(query_result)}')

for g in query_result:
    g_id = g['_id']
    print(f'Deleting greeting: {g_id}')
    del_resp = requests.delete(
        f'{url}/{g_id}', headers=requ_hs, timeout=timeout)
    del_resp.raise_for_status
    print(f'Deletion response: {del_resp.text}')

all_resp = requests.get(url, headers=requ_hs, timeout=timeout)
all_resp.raise_for_status
all_greetings = all_resp.json()
print(f'All greetings: {pp(all_greetings)}')
