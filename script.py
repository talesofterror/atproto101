import pprint
import requests
import json

pp = pprint.PrettyPrinter()

handle = "teleplasm.net"
resolved_handle = requests.get(
        "https://bsky.social/xrpc/com.atproto.identity.resolveHandle",
        params={"handle": handle}
        ).json() # returns a dict: {"did": "did:plc:abcd..."}

# did = json.loads(resolved_handle)

data_repository = requests.get(
        "https://bsky.social/xrpc/com.atproto.repo.describeRepo",
        # params={"repo": "did:plc:hkjsyp74tgqoka35lnovdumk"}
        params={"repo": resolved_handle["did"]}
        )

pp.pprint(resolved_handle)
pp.pprint(data_repository.json())
