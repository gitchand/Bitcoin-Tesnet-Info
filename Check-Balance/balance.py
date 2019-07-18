import requests

def Bal_Avail(addr):
    url = "https://chain.so/api/v2/address/BTCTEST/{}".format(addr)

    response = requests.get(url).json()

    if response['status'] == 'fail':
        return response['message']
    return response['data']

print(Bal_Avail('mhcAAHY7M5WuQzqqAHfzDLdu5hsp9Dow8y'))