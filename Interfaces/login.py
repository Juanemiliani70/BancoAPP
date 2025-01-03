from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.usuario import UsuarioData
from Interfaces.main import MainWindow
from model.user import Usuario

class Login():
    def __init__(self):
        self.login = uic.loadUi("Interfaces/login.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")  
        self.login.show()

    def ingresar(self):
        usuario = self.login.txtUsuario_2.text()
        clave = self.login.txtClave.text()

        
        if not usuario or len(usuario) < 2:
            self.login.lblMensaje.setText("Ingrese un usuario válido")
            self.login.txtUsuario_2.setFocus()
        elif not clave or len(clave) < 3:
            self.login.lblMensaje.setText("Ingrese una contraseña válida")
            self.login.txtClave.setFocus()
        else:
            self.login.lblMensaje.setText("")
            
            
            usu = Usuario(usuario=usuario, clave=clave)
            usuData = UsuarioData()
            
            try:
                res = usuData.login(usu)
                if res:
                    self.main = MainWindow()
                    self.login.hide()  
                else:
                    self.login.lblMensaje.setText("Datos de acceso incorrectos")
            except Exception as ex:
                self.login.lblMensaje.setText(f"Error de conexión: {str(ex)}")
    
    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)
