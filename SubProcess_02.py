import subprocess
#command=["ls","-l"]

command  = ["echo $SHELL"]

sp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# shell=False/True --> shell can have True or False values but recommended to keep it False
rt = sp.wait()
print(rt)

out,err = sp.communicate()
print(out)
print(err)
