import os 

temp = os.popen('git push').read()

print("Hola: ", temp)

# import subprocess
# subprocess.run(["python", "--version"])
# # Python 3.6.0
# subprocess.CompletedProcess(args=['python', '--version'], returncode=0)