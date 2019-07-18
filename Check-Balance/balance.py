import requests

def Bal_Avail(addr):
    url = "https://chain.so/api/v2/address/BTCTEST/{}".format(addr)

    response = requests.get(url).json()

    if response['status'] == 'fail':
        return response['message']
    return response['data']

Bitcoin_Tesnet_Address = "" # insert your bitcoin testnet address here to check available testnet bitcoin

Available_Balance = Bal_Avail(Bitcoin_Tesnet_Address)

print(Available_Balance)