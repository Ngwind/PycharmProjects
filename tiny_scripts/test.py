import os
import subprocess

s = '""'
print(s)
print("start")
os.system("ping 104.128.92.157")
p = subprocess.Popen("ping 104.128.92.157",stdout=subprocess.PIPE)
returncode = p.poll()
print("Hello")

while returncode is None:

        line = p.stdout.readline().decode(encoding="gbk")

        returncode = p.poll()

        line = line.strip()

        print(line)

print(returncode)
print("end")