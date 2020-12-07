import time
import os
import subprocess



subp = subprocess.Popen('python trial.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
    cwd=os.getcwd(),encoding="utf-8")

subp.wait(2)

if subp.poll() == 0:
    print(subp.communicate()[0])
else:
    print("failed!")
    
