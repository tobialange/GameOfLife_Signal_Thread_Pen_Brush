import sys
from GOLWidget import *

app = QtWidgets.QApplication(sys.argv)
window = GOLWidget()
window.show()
sys.exit(app.exec())

#https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens