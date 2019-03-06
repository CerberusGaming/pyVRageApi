# Python VRage Rest API
# Please note this is still under heavy development and should not be used in any production environments (yet.)

At the moment this simply generates the ability to do rest calls against a VRage-based game over its remote admin api.

Games "Supported":
- Space Engineers
- Medieval Engineers

Current Usage:
```python
from VRageAPI.REST import VRageAPI

base_url = "http://127.0.0.1:8080/"
api_key = "ThIsIsThESeCuRiTyKeY=="


test = VRageAPI(base_url, api_key)
print(test.do_call("/v1/server/ping"))  # Pong!
```

---
Cerberus Gaming - https://Cerberus-Gaming.com

Keen Software - https://www.keenswh.com/

VRage / Space Engineers / Medieval Engineers Copyright Keen Software House.