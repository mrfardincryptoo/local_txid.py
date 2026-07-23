import secrets

def generate_local_txid():
    return "0x" + secrets.token_hex(32)

print(f"Local TXID: {generate_local_txid()}")
