from kivy.uix.filechooser import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

class MainScreen(Screen): # ui 1
    pass

class Register(Screen): 
    pass

class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class dltApp(App):
    def build(self):
        return UI()
    
if __name__ == "__main__":
    dltApp().run()