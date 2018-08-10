import subprocess, sys
# 使用run（）
'''cp = subprocess.run("cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
print(cp.stdout)'''
# 使用popen（）
p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
p.stdin.write("echo aaa\n")
p.stdin.flush()
'''while True:
    line = p.stdout.readline()
    print("==",line,end="")
    if not line:
        break
'''

# p.stdin.write("exit\n")
# p.stdin.flush()
for line in iter(p.stdout.readline, ''):
    print(line)