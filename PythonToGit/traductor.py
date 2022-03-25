import sys
from PyQt5 import uic, QtWidgets, QtGui
from AS import *

qtCreatorFile = "vista.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.botonTraductor.clicked.connect(self.verificarDatos)
        
    def verificarDatos(self):
        entrada = self.entrada.text()
        # print(entrada)
        salida = main(str(entrada))
        self.traduccion.setText(salida)

    def mainAG(self):
        initialPopulation, populationLimit, mutationIndividual, chromosomeMutation, resolution, intervalX, intervalY = self.getValue()
       
    def exit(self):
        self.close()
        # print(self.initialPopulation.text())

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())