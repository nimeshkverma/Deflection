from mapping import BASE_URL, URL
import requests


def get_response(api_request):
    api = api_request.path.split('/')[-1]
    api_uri = BASE_URL + URL[api]["redirection_to"]
    payload = {}

    if api_request.method == 'POST':
        for param in URL[api]["params"]:
            payload[param] = api_request.form[param]
        api_response = requests.post(api_uri, data=payload)
    else:
        for param in URL[api]["params"]:
            payload[param] = api_request.args.get(param)
        api_response = requests.get(api_uri, params=payload)
    api_response.raise_for_status()
    return api_response.json()
