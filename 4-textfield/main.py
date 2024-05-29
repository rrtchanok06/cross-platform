from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class UI(MDBoxLayout):
    def show(self):
        print("from ui", self.ids.txt_input.text)

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"
        return UI()
    

if __name__=="__main__":
    DemoApp().run()

