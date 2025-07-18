from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QListWidget, QListWidgetItem, QMessageBox,
    QDialog, QDialogButtonBox, QMainWindow
)
from PySide6.QtGui import QIcon
import sys


class DialogNombre(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nuevo jugador")
        self.setMinimumWidth(250)
        self.nombre = None

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Nombre del jugador")

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ingrese el nombre del jugador:"))
        layout.addWidget(self.input)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def accept(self):
        texto = self.input.text().strip()
        if texto:
            self.nombre = texto
            super().accept()


class VentanaStats(QWidget):
    def __init__(self, nombre):
        super().__init__()
        self.setWindowTitle(f"Stats de {nombre}")
        self.setMinimumSize(300, 200)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Aquí irían los stats de {nombre}"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de personajes - Call of Cthulhu")
        self.setMinimumSize(400, 500)

        self.ventanas_stats = {}  # nombre -> ventana

        # Widgets principales
        self.lista = QListWidget()
        self.boton_agregar = QPushButton("Añadir jugador")

        # Conexiones
        self.boton_agregar.clicked.connect(self.mostrar_dialogo)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Personajes registrados:"))
        layout.addWidget(self.lista)
        layout.addWidget(self.boton_agregar)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        self.lista.itemClicked.connect(self.abrir_ventana_personaje)

    def mostrar_dialogo(self):
        dialogo = DialogNombre(self)
        if dialogo.exec():
            nombre = dialogo.nombre
            if nombre in self.ventanas_stats:
                self.abrir_ventana_personaje_por_nombre(nombre)
                return
            self.agregar_personaje(nombre)

    def agregar_personaje(self, nombre):
        item = QListWidgetItem(nombre)
        item.setIcon(QIcon.fromTheme("user-trash"))  # Requiere icon theme instalado (como en Linux)
        self.lista.addItem(item)

        ventana = VentanaStats(nombre)
        ventana.setAttribute(Qt.WA_DeleteOnClose, False)  # Solo ocultar, no destruir
        ventana.closeEvent = lambda event, n=nombre: self.ocultar_ventana(event, n)
        self.ventanas_stats[nombre] = ventana

    def abrir_ventana_personaje(self, item):
        nombre = item.text()
        self.abrir_ventana_personaje_por_nombre(nombre)

    def abrir_ventana_personaje_por_nombre(self, nombre):
        ventana = self.ventanas_stats.get(nombre)
        if ventana:
            ventana.show()
            ventana.raise_()
            ventana.activateWindow()

    def ocultar_ventana(self, event, nombre):
        event.ignore()
        self.ventanas_stats[nombre].hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())