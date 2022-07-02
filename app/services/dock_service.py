from http import HTTPStatus

import requests
from requests.auth import HTTPBasicAuth


def dock_token(request_id, url, app_client, app_secret):
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    auth = HTTPBasicAuth(app_client, app_secret)
    try:
        response = requests.post(url, headers=header, auth=auth, timeout=10)
        if response.status_code == HTTPStatus.OK:
            data = response.json()
            return data['access_token']
        else:
            raise
    except Exception as e:
        print('{}| Error while generating DOCK token: {}'.format(request_id, e.args))
        raise


def create_qrcode_invoice(request_id, emissor, token, body):
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    try:
        payload = {}
        response = requests.post(emissor['url_qrcode']['S'], headers=header, json=payload, timeout=10)
        if response.status_code == HTTPStatus.CREATED:
            return response.json()
        else:
            raise
    except Exception as e:
        print('{}| Error while generating QRCODE INVOICE: {}'.format(request_id, e.args))
        raise
