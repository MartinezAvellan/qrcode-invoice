from app.services.token_service import NewToken
from app.utils.utils import get_request_id, is_str_or_dict

new_token = NewToken()


def handler(event, context):
    request_id = get_request_id(event, context)
    message = is_str_or_dict(event)
    try:
        body = is_str_or_dict(message['Records'][0]['body'])
        token, emissor = new_token.get_token(request_id, body)
        print(token)
        print(emissor)
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    eeeee = {'Records': [
        {'messageId': '154e99d1-f79c-4f23-8d2d-169ecc9e4bbc',
         'receiptHandle': 'AQEB+f2dex7L5+dkYg==',
         'body': '{\n   "file_name":"EcosyInstdePagamentoSA29042022.txt",\n   '
                 '"bucket_name":"read-invoice",\n   '
                 '"nome_cedente":"Banco EC S.A.",\n   '
                 '"cnpj_cedente":"33264668000103",\n   '
                 '"data_geracao":"29042022",\n   '
                 '"nome_cliente":"FABILANIA SANDES",\n   '
                 '"cpf_cnpj":"99958773414",\n   '
                 '"conta":"682680",\n   '
                 '"cep":"71505235",\n   '
                 '"cidade":"Barueri",\n   '
                 '"estado":"DF",\n   '
                 '"endereco":"Av. Tambore",\n   '
                 '"numero":"267",\n   '
                 '"complemento":"Complemento",\n   '
                 '"valor_fatura":"00000000204655",\n   '
                 '"idtx":"QT332646680001032904202200000000001",\n   '
                 '"loc":{\n      "url":"api-h.developer.btgpactual.com/v1/p/v2/bd2f1763b529490c97792f543fd1d01c",\n      '
                 '"emv":"00020101021226930014br.gov.bcb.pix2571api-h.developer.btgpactual.com/v1/p/v2/bd2f1763b529490c97792f543fd1d01c5204010053039865802BR5923Joselito de Souza Silva6007Barueri61087150523562070503***630471FB",\n      '
                 '"locType":"COB",\n      '
                 '"id":"4078206097511746876",\n      '
                 '"idTx":"RQT332646680001032904202200000000019999",\n      '
                 '"loc":"bd2f1763-b529-490c-9779-2f543fd1d01c"\n   }'
                 '\n}', 'attributes': {'ApproximateReceiveCount': '1',
                                       'SentTimestamp': '1656794186254',
                                       'SenderId': 'AIDAYT3YFZIESZ6X7UGX6',
                                       'ApproximateFirstReceiveTimestamp': '1656794186260'
                                       }, 'messageAttributes': {}, 'md5OfBody': '9169a31dbb0d4efce4eeb484e9e725e2',
         'eventSource': 'aws:sqs',
         'eventSourceARN': 'arn:aws:sqs:sa-east-1:592420653577:qrcode-invoice',
         'awsRegion': 'sa-east-1'}
    ]}


    handler(eeeee, None)
