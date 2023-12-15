from requests import get

def get_token_pair_info(token_address):
    # Takes in a token's ERC20 address and returns the UNIX start time, earliest known LP address, name, and symbol
    response = get(f"https://api.dexscreener.com/latest/dex/tokens/{token_address}")
    pairs = response.json()["pairs"]

    first_pair_time = min([pair["pairCreatedAt"] for pair in pairs if "pairCreatedAt" in pair])

    lp_address = [[str(pair["pairCreatedAt"]), pair["pairAddress"], pair["baseToken"]["name"], pair["baseToken"]["symbol"]] for pair in pairs if "pairCreatedAt" in pair if pair["pairCreatedAt"] == first_pair_time]

    return lp_address[0]

test = get_token_pair_info("0x72e4f9F808C49A2a61dE9C5896298920Dc4EEEa9")

print(test)