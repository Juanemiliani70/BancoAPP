from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.usuario import UsuarioData
from model.user import Usuario 

class RegistroWindow():
    def __init__(self):
        self.v = uic.loadUi("interfaces/registro.ui") 
        self.initGUI()  
        self.v.show()

    def initGUI(self):
        self.v.btnRegistrar.clicked.connect(self.registrarUsuario)
        
    def registrarUsuario(self):
        usuario = self.v.txtUsuario.text()
        clave = self.v.txtClave.text()
        nombre = self.v.txtNombre.text()

       
        if len(usuario) < 3:
            self.mostrarMensaje("El nombre de usuario debe tener al menos 3 caracteres.")
            return
        if len(clave) < 6:
            self.mostrarMensaje("La contraseña debe tener al menos 6 caracteres.")
            return
        if len(nombre) < 3:
            self.mostrarMensaje("El nombre debe tener al menos 3 caracteres.")
            return
        
       
        nuevo_usuario = Usuario(usuario = usuario, clave=clave, nombre = nombre)
        usuario_data = UsuarioData()
        
        if usuario_data.registrar(nuevo_usuario):
            self.mostrarMensaje("Usuario registrado exitosamente.")
            self.limpiarCampos()
        else:
            self.mostrarMensaje("Hubo un error al registrar el usuario.")

    def mostrarMensaje(self, mensaje):
        mBox = QMessageBox()
        mBox.setText(mensaje)
        mBox.exec()

    def limpiarCampos(self):
        self.v.txtUsuario.setText("")
        self.v.txtClave.setText("")
        self.v.txtNombre.setText("")
        self.v.txtUsuario.setFocus()  
