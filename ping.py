import os, re
#by Nícolas Barbosa 

pergunta = input("IP ou url:")
cmd = "ping -c4 " + pergunta
r = "".join(os.popen(cmd).readlines())
print(r)

if re.search ("64 bytes from", r):
  print("Link UP")
else:
  print("Link Down")
   
