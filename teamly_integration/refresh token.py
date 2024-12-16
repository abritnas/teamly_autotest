import requests

data = {
    "client_id": "8238a403-6509-4818-ac87-daab05d7ddd2",
    "client_secret": "Bufc7OJYEAnBnYcDwD5sJl67ksXWhyqMbbhGo0Jv",
    "refresh_token": "def50200258d7ce8819fa04f217d6faf4168a2dad9d04e004157dd4f3342f9902056aabf0d62aa8413381275ef5d3"
                     "a6dd8802ac31a687afee1799302a023db0c974324a3bba4010d61cafccb00acc8cca642cc422a932fc4a38826ddc0ad"
                     "d5e9e1fa0650f692dc637fb463449db4999959fd0a69d3e5b72383b6f21ece29a84642e5dc837b22200a0662d4c11e8"
                     "135d5ec22be3084dceb8092df6c9f93900264bbc11b568ab389333024c6e7016a578cec58a02b801bffc3ea11650d27"
                     "7e5ec8177e34f9c4a6a2a195b4e76f8370a3fd7f99695b4d9e3728d4194bf4f8e93a3c592101726304fc8e8852fe299"
                     "4312ab1991afa0c53cc1300db05ba76e452e3443591e47d29b007ba8c3a4c4ba5596b25152ac6b36efd7f0d726cd24"
                     "0d998af63130e78931b64d8d849d4f17a7a523e8d69b83d7ce5aec066392e797f1608a126c29b8f6f4714697baf5f0c3"
                     "bf92b3df6cf5cc1c8d8ec4bc9dcc1ac12400328c3073ee3ee0a5d93b0d995d78e09fae982d0138eb972fd4718a6575e3"
                     "4dfdd9f2497e06e873b93e9afc1e3386e7e47041b7a93d48cb39b3b9b2c3daa8dfbdd362ccb2f87bc6691f03f95890d"
                     "fa72fba163a3bce0"
}

response = requests.post('https://woof.teamly.ru/api/v1/auth/integration/refresh', json=data)

json_response = response.json()

if response.status_code == 200:
    print('успех')
elif response.status_code == 401:
    print(json_response['error_message'])
elif response.status_code == 404:
    print('Not found')

print(json_response)
print(response.headers)
print(json_response["accounts"])
