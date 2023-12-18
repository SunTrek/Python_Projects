import sys
import subprocess

result = subprocess.run([sys.executable, "-c", "print('This is a subprocess')"])

result2 = subprocess.run(["/usr/local/bin/python", "-c", "print('This is a subprocess result2')"],capture_output=True,text=True,check=True)

print(result)
print(result2)

print("\nError:",result2.stderr)
print("output:",result2.stdout)
