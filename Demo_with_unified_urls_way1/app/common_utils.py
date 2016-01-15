import requests


def api_response(api_request, api_mappings):
    api = api_request.path.split('/')[-1]
    api_uri = api_mappings[api]["third_party_url"]
    payload = {}

    if api_request.method == 'POST':
        for param in api_mappings[api]["params"]:
            payload[param] = api_request.form[param]
        api_response = requests.post(api_uri, data=payload)
    else:
        for param in api_mappings[api]["params"]:
            payload[param] = api_request.args.get(param)
        api_response = requests.get(api_uri, params=payload)

    api_response.raise_for_status()
    return api_response.json()
