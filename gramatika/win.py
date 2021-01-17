from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import subprocess
import sys


class Okno(Widget):
    btnRes = ObjectProperty(None)
    btnMen = ObjectProperty(None)

    def menu(self):
        subprocess.Popen(['python', 'menu.py'])
        App.stop()
        sys.exit(0)

    def restart(self):
        subprocess.Popen(['python', 'gramatika/gramatika.py'])
        App.stop()
        sys.exit(0)


class WinApp(App):
    def build(self):
        return Okno()


if __name__ == "__main__":
    WinApp().run()
