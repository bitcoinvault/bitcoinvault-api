import requests
import json
import random

url = "http://user:password@bitcoind:8332"

def get_block_hash(block_number):
    rpc = RPC("getblockhash", [block_number])
    return rpc.execute()

def get_block(block_number, verbosity=2):
    block_hash = get_block_hash(block_number)
    rpc = RPC("getblock", [block_hash, verbosity])
    return rpc.execute()

def get_block_count():
    rpc = RPC("getblockcount")
    return rpc.execute()

def get_hashrate():
    rpc = RPC("getnetworkhashps")
    return rpc.execute()

class RPC:
    def __init__(self, method="", params=[], rpc_id=random.random()):
        self.method = method
        self.params = params
        self.jsonrpc = "2.0"
        self.id = rpc_id

    def execute(self):
        response = requests.post(url, json=self.dict()).json()
        return response['result']

    def dict(self):
        payload = {
            "method": self.method,
            "params": self.params,
            "jsonrpc": self.jsonrpc,
            "id": self.id,
        }
        return payload