import os 

temp = os.popen('git clone https://github.com/Leoonnardo/PythonToGit.git').read()
# temp = os.path.dirname("D:\Escritorio\Cuatrimestre 8\Compiladores\Corte 3\Corte 3\C2")

print("Hola: ", temp)

# import subprocess
# subprocess.run(["python", "--version"])
# # Python 3.6.0
# subprocess.CompletedProcess(args=['python', '--version'], returncode=0)