from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import sys
import subprocess


class Okno(Widget):
    btnGra = ObjectProperty(None)
    btnPoc = ObjectProperty(None)

    def poct(self):
        subprocess.Popen(['python', 'pocitani/count.py'])
        App.stop()
        sys.exit(0)

    def gram(self):
        subprocess.Popen(['python', 'gramatika/gramatika.py'])
        App.stop()
        sys.exit(0)


class MenuApp(App):
    def build(self):
        return Okno()


if __name__ == "__main__":
    MenuApp().run()
