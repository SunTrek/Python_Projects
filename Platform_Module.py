import platform
import os

osname = platform.system()
print(osname)
if platform.system() == "Linux":
  print("Command is executed for Linux OS")
  os.system('ls')
elif platform.system() == 'Windows':
  print("Command is excuted for Windows OS")
else:
  print("Unsupported OS")
