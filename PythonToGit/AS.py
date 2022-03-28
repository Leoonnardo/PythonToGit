from distutils.errors import CompileError
from audioop import add
import csv
from mimetypes import init
from queue import PriorityQueue
import re
import string
from tkinter import N
import os 

from matplotlib.cbook import pts_to_midstep

comando = {
    'Clone'    : 'git clone',
    'Commit'   : 'git commit',
    'Config'   : 'git config',
    'Push'     : 'git push',
    'Checkout' : 'git checkout',
    'Branch'   : 'git branch',
    'Merge'    : 'git merge'
}

def main(entrada):
    # Lectura del CSV y extraccion de datos
    comando = entrada
    with open('tablaSintactico.csv', newline='') as File:  
        reader = csv.reader(File)
        auxLit = []
        listaDatos = []
        for row in reader:
            for datos in row:
                auxLit.append(datos)
            listaDatos.append(auxLit)
            auxLit = []  
        # print(ListaTot-alDatos[0][18])

    terminales = ['git', 'init', 'status', 'pull', 'stash', 'checkout', 'branch', 'clone', 'add', 'commit', 'config', 'push', 'remote', 'merge', 'fetch', '.', '-m', '"', '--global', 'user.name', '-v', 'origin', '-b', '-d', 'https', 'github.com', 'letra', 'digito', '://', '/']

    resultado = ''
    # Ingresar la entrada
    entrada = entrada + ' $'
    listEntrada = validarPalabra(entrada)
    
    # Establecer pila
    pila = ['S', '$']

    # Apuntador para la entrada
    apuntador = 0

    # Recorrer el while
    posicion = pila[0]
    bandera = False
    while (posicion != '$'):
        print('Entrada:', listEntrada)
        print('Pila:', pila)
        print('Posicion de pila:', posicion)
        print('Posicion de entrada:', listEntrada[apuntador])
        if (bandera == False or posicion == '://' or posicion == '/'):
            # print('Entramos en false primero')
            for ter in range(len(terminales)):
                # print('Pila', pila, 'posicion', posicion)
                if (posicion == terminales[ter] or posicion == '$'):
                    print('Es terminal')
                    print('ELIMINE DE LA PILA', pila[0])
                    pila.pop(0)
                    listEntrada.pop(0)
                    posicion = pila[0]
                    print('PILA', pila)
                    # bandera = False
                    resultado = 'VERDADERO'
                    break
            bandera = True
        else:
            print('NO ES TERMINAL')
            x = pila[0]
            a = listEntrada[apuntador]
            # print('ENTRADA', listEntrada)
            # print('APUNTADOR', a)
            # nX = 0
            # nA = 0

            # Buscar posicion de la pila en la tabla
            for bX in range(len(listaDatos)):
                # print('bX', listaDatos[bX][0])
                if (x == listaDatos[bX][0]):
                    nX = bX
                    print('FILA', nX, listaDatos[bX][0])

            # Buscar posicion de la entrada con el apuntador en la tabla
            ban = False
            for bA in range(len(listaDatos[0])):
                # print(listaDatos[0][bA])
                if (a == listaDatos[0][bA]):
                    nA = bA
                    print('COLUMNA', nA, listaDatos[0][bA])
                    # print(listaDatos[nX][nA])
                    if (listaDatos[nX][nA] == 'vacio'):
                        ban = False
                        break
                    else:
                        ban = True
                        break
                else:
                    ban = False
            # print(ban)
            # Extraer el valor de la posicion localizada en la tabla
            if (ban == True):
                valor = listaDatos[nX][nA]
                if (valor != '1'):
                    print('Valor añadir:', valor)
                    pila.pop(0)
                    # print(listEntrada)
                    listValor = valor.split()
                    # print('Lista de valores:', listValor)
                    aux = len(listValor)
                    for i in range(len(listValor)):
                        aux = aux - 1
                        # print(aux)
                        pila.insert(0, listValor[aux])
                        listValor.pop(aux)
                    # print(pila)
                    posicion = pila[0]
                    # print(pila[0])
                    bandera = False
                else:
                    print('---------------Cadena invalida por posicion no encontrada--------------')
                    posicion = '$'
                    resultado = 'INCORRECTO'
                    break
            else:
                print("Uñtimo else")
                if (pila[0] == 'COMPLEMENTO'):
                    print('Ban de columna', ban, 'Sacamos', pila[0])
                    pila.pop(0)
                    posicion = pila[0]
                    bandera = False
                elif (listaDatos[nX][nA] == 'vacio'):
                    pila.pop(0)
                    bandera = False
                    print('veamos la pila', pila)
                    break
                else:
                    print('---------------Cadena invalida por posicion no encontrada---------------')
                    posicion = '$'
                    resultado = 'INCORRECTO'
                    break
        print("---------------------------------------------TERMINA VUELTA---------------------------------------------")
    
    if pila[0] == "$" and listEntrada[0] == "$":
        resultado = "Correcto"
        print(resultado)
        resultado = os.popen(comando).read()
        print("Resultado: ", resultado)
        
        if comando == "git add .":
            resultado = "Añadido"

        if comando[0:9] == "git clone":
            comandoAux = str(comando[29:len(comando)-4])
            comandoAux = comandoAux.replace("/", " ")
            comandoAux = comandoAux.split()
            resultado = validarRepo(comandoAux[1])
            # if comandoAux[1]

        if comando[0:15] == "git checkout -b":
            resultado = "Switched to new branch " + comando[16:len(comando)]
        if comando[0:7] == "git push":
            resultado = "Everyting up-to-date"


    else:
        print(resultado)
        resultado = "Comando incorrecto"
    
    print(resultado)
    print('Pila final', pila)
    print('Entrada final', listEntrada)
    
    return resultado


def validarRepo(comandoAux):
    validar = ""
    ruta = os.path.dirname(os.path.abspath(__file__))

    dirs = os.listdir( ruta )

    # This would print all the files and directories
    for file in dirs:
        print(file)
        if comandoAux == file:
            validar = "Repositorio existente"
            return validar
    return "No existe el repositorio"
            
def validarPalabra(entrada):
    letra = list(string.ascii_uppercase) + list(string.ascii_lowercase)
    digito = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    retorno = []
    # git clone https://github.com/Fercas22/ProjectAG.git
    if (entrada[0:9] == comando['Clone']):
        git = entrada[0:3]
        clone = entrada[4:9]
        protocolo = entrada[10:15]
        pd = entrada[15:18]
        pagina = entrada[18:28]
        d = entrada[28:29]
        complemento = list(str(entrada[29:len(entrada)-6]))
        punto = entrada[len(entrada)-6] 
        ext = entrada[len(entrada)-5: len(entrada)-2]
        terminal = entrada[len(entrada)-1: len(entrada)]
        retorno.append(git)
        retorno.append(clone)
        retorno.append(protocolo)
        retorno.append(pd)
        retorno.append(pagina)
        retorno.append(d)
        for i in range(len(complemento)):
            vLetra = complemento[i] in letra
            vNumero = complemento[i] in digito
            if (vLetra == True):
                retorno.append('letra')
            elif (vNumero == True):
                retorno.append('digito')
            elif (complemento[i] == '/'):
                retorno.append('/')
        retorno.append(punto)
        retorno.append(ext)
        retorno.append(terminal)
    # git commit -m "Hola"    
    elif (entrada[0:10] == comando['Commit']):
        git = entrada[0:3]
        commit = entrada[4:10]
        guion = entrada[11:13]
        cA = entrada[14:15]
        complemento = str(entrada[15:len(entrada)-3])
        aux = list(complemento)
        cC = entrada[len(entrada)-3: len(entrada)-2]
        terminal = entrada[len(entrada)-1: len(entrada)]
        retorno.append(git)
        retorno.append(commit)
        retorno.append(guion)
        retorno.append(cA)
        for comp in range(len(aux)):
            vLetra = aux[comp] in letra
            vNumero = aux[comp] in digito
            if (vLetra == True):
                retorno.append('letra')
            elif (vNumero == True):
                retorno.append('digito')
        retorno.append(cC)
        retorno.append(terminal)
    # git config --global user.name "Hola"
    elif (entrada[0:10] == comando['Config']):
        git = entrada[0:3]
        config = entrada[4:10]
        guion = entrada[11:19]
        user = entrada[20:29]
        cA = entrada[30:31]
        complemento = str(entrada[31:len(entrada)-3])
        aux = list(complemento)
        cC = entrada[len(entrada)-3: len(entrada)-2]
        terminal = entrada[len(entrada)-1: len(entrada)]
        retorno.append(git)
        retorno.append(config)
        retorno.append(guion)
        retorno.append(user)
        retorno.append(cA)
        for comp in range(len(aux)):
            vLetra = aux[comp] in letra
            vNumero = aux[comp] in digito
            if (vLetra == True):
                retorno.append('letra')
            elif (vNumero == True):
                retorno.append('digito')
        retorno.append(cC)
        retorno.append(terminal)
    # git push origin HOLa
    elif (entrada[0:8] == comando['Push']):
        git = entrada[0:3]
        push = entrada[4:8]
        origin = entrada[9:15]
        complemento = str(entrada[16:len(entrada)-2])
        aux = list(complemento)
        terminal = entrada[len(entrada)-1: len(entrada)]
        retorno.append(git)
        retorno.append(push)
        retorno.append(origin)
        for comp in range(len(aux)):
            vLetra = aux[comp] in letra
            vNumero = aux[comp] in digito
            if (vLetra == True):
                retorno.append('letra')
            elif (vNumero == True):
                retorno.append('digito')
        retorno.append(terminal)
        print("Retorno: ", retorno)
    # git checkout -b HolA
    # git checkout HolA
    elif (entrada[0:12] == comando['Checkout']):
        git = entrada[0:3]
        checkout = entrada[4:12]
        retorno.append(git)
        retorno.append(checkout)
        guion = entrada[13:15]
        if (guion == '-b'):
            retorno.append(guion)
            complemento = str(entrada[16:len(entrada)-2])
            aux = list(complemento)     
            for comp in range(len(aux)):
                vLetra = aux[comp] in letra
                vNumero = aux[comp] in digito
                if (vLetra == True):
                    retorno.append('letra')
                elif (vNumero == True):
                    retorno.append('digito')
        else:
            complemento = str(entrada[13:len(entrada)-2])
            aux = list(complemento)     
            for comp in range(len(aux)):
                vLetra = aux[comp] in letra
                vNumero = aux[comp] in digito
                if (vLetra == True):
                    retorno.append('letra')
                elif (vNumero == True):
                    retorno.append('digito')
        terminal = entrada[len(entrada)-1: len(entrada)]
        retorno.append(terminal)
    # git branch -d HolA
    # git branch
    elif (entrada[0:10] == comando['Branch']):
        git = entrada[0:3]
        branch = entrada[4:10]
        retorno.append(git)
        retorno.append(branch)
        if (entrada[11:len(entrada)-2] != None):
            guion = entrada[11:13]
            if (guion == '-d'):
                retorno.append(guion)
                complemento = str(entrada[14:len(entrada)-2])
                aux = list(complemento)     
                for comp in range(len(aux)):
                    vLetra = aux[comp] in letra
                    vNumero = aux[comp] in digito
                    if (vLetra == True):
                        retorno.append('letra')
                    elif (vNumero == True):
                        retorno.append('digito')
            else:
                complemento = str(entrada[11:len(entrada)-2])
                aux = list(complemento)     
                for comp in range(len(aux)):
                    vLetra = aux[comp] in letra
                    vNumero = aux[comp] in digito
                    if (vLetra == True):
                        retorno.append('letra')
                    elif (vNumero == True):
                        retorno.append('digito')
        terminal = entrada[len(entrada)-1: len(entrada)]
        retorno.append(terminal)
        print('------------------------------------------------', retorno)
    # git merge Hola
    elif (entrada[0:9] == comando['Merge']):
        git = entrada[0:3]
        merge = entrada[4:9]
        complemento = str(entrada[10:len(entrada)-2])
        aux = list(complemento)
        terminal = entrada[len(entrada)-1: len(entrada)]
        retorno.append(git)
        retorno.append(merge)
        for comp in range(len(aux)):
            vLetra = aux[comp] in letra
            vNumero = aux[comp] in digito
            if (vLetra == True):
                retorno.append('letra')
            elif (vNumero == True):
                retorno.append('digito')
        retorno.append(terminal)
    else:
        retorno = entrada.split()
    return retorno

    # git clone https://github.com/Fercas22/ProjectAG.git
    # git commit -m "Hola"    
    # git config --global user.name "Hola"

    # git push origin HOLa
    # git checkout -b HolA
    # git checkout HolA

    # git branch -d HolA
    # git branch
    # git merge Hola
    
    # git init
    # git status
    # git pull
    # git stash
    # git add .
    # git remote -v
    # git fetch origin