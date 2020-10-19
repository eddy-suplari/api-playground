import requests
import json

# Would be class variables instead of global
insight_id = 'f9bcc167f176cfb3f9e941d85e0b7009'  # ETLephant insight (broken)
env_id = 'suplari'
headers = {'Authorization': 'Bearer eyJraWQiOiJHbkYtSjA3N3hkVnJpTGw4Y3lZbWVpQWVEMnZZdDRKVjI5UnhLQk9KQXJzIiwiYWxnIjoiUlMyNTYifQ',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'envHeaderKey': env_id,
            'IE-Access-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL3N1cGxhcmkuY29tL2llL3VzZXJfYXV0aHoiOnsiaWVfcGVybWlzc2lvbnMiOlsiaW5zaWdodC1lbmdpbmUtZjliY2MxNjdmMTc2Y2ZiM2Y5ZTk0MWQ4NWUwYjcwMDkiXX0sImF1ZCI6IkFGZ2ZBeGw2cVpjVmZ3bmRNMWpaU2s0dVBoYVZMcmNOeVhyMzZSR3JvWkk9IiwiaWF0IjoxNjAzMTMyMjQzLCJleHAiOjE2MDMyMTg2NDN9.o8l8t9rglRUcGXbQvD7LtabvULAwvELbomgkWDnhcBc',
        }


def make_call(url, type):
    if type.lower() == 'get':
        import_api_response = requests.get(url, headers=headers)
    elif type.lower() == 'post':
        import_api_response = requests.post(url, headers=headers)
    else:
        return "Unknown request type, please pick get or post"
    if import_api_response.status_code == 200:
        return json.loads(import_api_response.text)
    else:
        return f'request failed with status code {import_api_response}'


def get_settings():
    url = f'https://suplari.suplari.com/engine/suplari/{insight_id}/api/v1/pipeline'
    txt = make_call(url, 'get')
    return txt['settings']


def run_insight():
    """
    From Line 277 from https://github.com/suplari/frontend/blob/3ca0e107279ae81c5a2e579eadf5969643825b35/src/app/services/insight-generator/ig-backend-engine.service.ts
    """
    url = f'https://suplari.suplari.com/engine/suplari/{insight_id}/api/v1/pipeline/run'
    txt = make_call(url, 'post')
    print(txt)
    return txt


d = run_insight()
for k, v in d.items():
    print(k)  # See everything in the response
