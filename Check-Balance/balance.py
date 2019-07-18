import requests

def Bal_Avail(addr):
    url = "https://chain.so/api/v2/address/BTCTEST/{}".format(addr)

    response = requests.get(url).json()

    if response['status'] == 'fail':
        return response['message']
    return response['data']

Bitcoin_Tesnet_Address = ""

Available_Balance = Bal_Avail(Bitcoin_Tesnet_Address)

print(Available_Balance)