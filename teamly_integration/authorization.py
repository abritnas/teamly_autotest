import requests

data = {
    "client_id": "3a56391e-1509-4555-abbf-71459a326171",
    "redirect_uri": "https://woof.teamly.ru/",
    "client_secret": "8yAXocS4999ZdodpSnOuNFwzyA3EzYAIOUzObMC3",
    "code": "def5020089eb11a6d62138cfa3c70f3b758f6ba89908064bc423b03c7f834d88c72c3835e6707457cee11139ea3ff911c80814df31b7d7a76c2c23cceecfa0f198e2d7572734ec8b9a5c3eded043b1602f2946f204c5ba9f0af278fbd06a49f9b54f1ad73d035a5956e7b137df973e1be25571db7e23e9dc4f021e67a8dcf80b5f4bdcb749e31324b030c335eb8d5300b8282149519efbb7380febc37cc2c4ef212f443e59d2532b947bf35a425ba50ddaee05d90a2ab7861b021cab4b9a495003a04e24072fa9b0a02c7933f2c66f439ec89aba2bfb26fe81e5041117ce95d1f456f01b8aac20a21f91699e288f4187c64f0f3e2b1f277c8fdf0752d7bf881a337329924400fa26e6da97db156a1368b8b038c1c4080db1d1c33bfec2aac736824b353c8f5f61f183d53ac9bf78fc87c89fe953d4b3f85d6442702f8242d43809cfea43be08a05aebf984a9e56d90cdaef351641c9287ea2aedb4572892451378c2ed42cd7f6b6fa3d27be80063364a16f644dcfa3685fdcebb1516ce2daa1382aab3214b94ca1c7a1325a04a6b5f332b32520f2f9aad2b8b67e4e8f182f3d8dc50a41c60eacb1bbc"
}

response = requests.post('https://woof.teamly.ru/api/v1/auth/integration/authorize', json=data)

json_response = response.json()

if response.status_code == 200:
    print('успех')
elif response.status_code == 401:
    print(json_response['error_message'])
elif response.status_code == 404:
    print('Not found')

slug = json_response['accounts'][0]['slug']

print(json_response['accounts'][0]['slug'])
print(response.headers)
