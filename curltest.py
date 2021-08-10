import requests

def testAPI ():
    headers = {
        'Accept': 'application/json',
    }

    response = requests.post('http://192.168.100.10/api/recording/start', headers=headers)
    print(response)

testAPI()