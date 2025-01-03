from PyQt6.QtWidgets import QApplication
from Interfaces.login import Login

class Banco():
    def __init__(self):
        try:
            self.app = QApplication([])  
            self.login = Login()  
            self.app.exec() 
        except Exception as e:
            print(f"Error al iniciar la aplicación: {e}")


if __name__ == "__main__":
    banco_app = Banco()

