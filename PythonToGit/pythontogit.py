# import os 

# temp = os.popen('git clone https://github.com/Leoonnardo/PythonToGit.git').read()
# temp2 = os.get_terminal_size().columns
# temp = os.path.dirname("D:\Escritorio\Cuatrimestre 8\Compiladores\Corte 3\Corte 3\C2")
# temp = os.system("git clone https://github.com/Leoonnardo/PythonToGit.git").__init__()

# print("Hola: ", temp)

import os

ruta = os.path.dirname(os.path.abspath(__file__))

dirs = os.listdir( ruta )

# This would print all the files and directories
for file in dirs:
   print(file)

entrada = "git clone https://github.com/Leoonnardo/PythonToGit.git"
# print(entrada[0:9])

comandoAux = str(entrada[29:len(entrada)-4])
comandoAux = comandoAux.replace("/", " ")
comandoAux = comandoAux.split()
print(comandoAux[1])


# cmd = "date"

# returns output as byte string
# returned_output = subprocess.check_output("git commit -m 'HOLa'")
# home_dir = os.system("git status")
# print("git status` ran with exit code %d" % home_dir)
# unknown_dir = os.system("git status")
# print("`git status` ran with exit code %d" % unknown_dir)
# # using decode() function to convert byte string to string
# print('Current date is:', returned_output.decode("base64"))

# print("Hola: ", temp2)

# import subprocess
# subprocess.run(["python", "--version"])
# # Python 3.6.0
# subprocess.CompletedProcess(args=['python', '--version'], returncode=0)