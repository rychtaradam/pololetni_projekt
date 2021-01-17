import random
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.config import Config
import sys
import subprocess


Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
num_list = []


class Count(Widget):

    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    btn3 = ObjectProperty(None)
    btn4 = ObjectProperty(None)
    btn5 = ObjectProperty(None)
    btn6 = ObjectProperty(None)
    btn7 = ObjectProperty(None)
    btn8 = ObjectProperty(None)
    btn9 = ObjectProperty(None)
    btn10 = ObjectProperty(None)
    btn11 = ObjectProperty(None)
    btn12 = ObjectProperty(None)
    btn13 = ObjectProperty(None)
    btn14 = ObjectProperty(None)
    btn15 = ObjectProperty(None)
    btn16 = ObjectProperty(None)
    btn17 = ObjectProperty(None)
    btn18 = ObjectProperty(None)
    btn19 = ObjectProperty(None)
    btn20 = ObjectProperty(None)

    btn = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20]

    i = 1

    for i in range(20):
        num_list = random.sample(range(1, 21), 20)

    list_of_numbers = [str(x) for x in num_list]

    test = 1

    def check(self, id):

        if id == 1:
            if self.btn1.text == str(self.test):
                self.btn1.background_color = green
                self.test += 1
                self.btn1.disabled = True
            else:
                self.btn1.background_color = red

        if id == 2:
            if self.btn2.text == str(self.test):
                self.btn2.background_color = green
                self.test += 1
                self.btn2.disabled = True
            else:
                self.btn2.background_color = red

        if id == 3:
            if self.btn3.text == str(self.test):
                self.btn3.background_color = green
                self.test += 1
                self.btn3.disabled = True
            else:
                self.btn3.background_color = red

        if id == 4:
            if self.btn4.text == str(self.test):
                self.btn4.background_color = green
                self.test += 1
                self.btn4.disabled = True
            else:
                self.btn4.background_color = red

        if id == 5:
            if self.btn5.text == str(self.test):
                self.btn5.background_color = green
                self.test += 1
                self.btn5.disabled = True
            else:
                self.btn5.background_color = red

        if id == 6:
            if self.btn6.text == str(self.test):
                self.btn6.background_color = green
                self.test += 1
                self.btn6.disabled = True
            else:
                self.btn6.background_color = red

        if id == 7:
            if self.btn7.text == str(self.test):
                self.btn7.background_color = green
                self.test += 1
                self.btn7.disabled = True
            else:
                self.btn7.background_color = red

        if id == 8:
            if self.btn8.text == str(self.test):
                self.btn8.background_color = green
                self.test += 1
                self.btn8.disabled = True
            else:
                self.btn8.background_color = red

        if id == 9:
            if self.btn9.text == str(self.test):
                self.btn9.background_color = green
                self.test += 1
                self.btn9.disabled = True
            else:
                self.btn9.background_color = red

        if id == 10:
            if self.btn10.text == str(self.test):
                self.btn10.background_color = green
                self.test += 1
                self.btn10.disabled = True
            else:
                self.btn10.background_color = red

        if id == 11:
            if self.btn11.text == str(self.test):
                self.btn11.background_color = green
                self.test += 1
                self.btn11.disabled = True
            else:
                self.btn11.background_color = red

        if id == 12:
            if self.btn12.text == str(self.test):
                self.btn12.background_color = green
                self.test += 1
                self.btn12.disabled = True
            else:
                self.btn12.background_color = red

        if id == 13:
            if self.btn13.text == str(self.test):
                self.btn13.background_color = green
                self.test += 1
                self.btn13.disabled = True
            else:
                self.btn13.background_color = red

        if id == 14:
            if self.btn14.text == str(self.test):
                self.btn14.background_color = green
                self.test += 1
                self.btn14.disabled = True
            else:
                self.btn14.background_color = red

        if id == 15:
            if self.btn15.text == str(self.test):
                self.btn15.background_color = green
                self.test += 1
                self.btn15.disabled = True
            else:
                self.btn15.background_color = red

        if id == 16:
            if self.btn16.text == str(self.test):
                self.btn16.background_color = green
                self.test += 1
                self.btn16.disabled = True
            else:
                self.btn16.background_color = red

        if id == 17:
            if self.btn17.text == str(self.test):
                self.btn17.background_color = green
                self.test += 1
                self.btn17.disabled = True
            else:
                self.btn17.background_color = red

        if id == 18:
            if self.btn18.text == str(self.test):
                self.btn18.background_color = green
                self.test += 1
                self.btn18.disabled = True
            else:
                self.btn18.background_color = red

        if id == 19:
            if self.btn19.text == str(self.test):
                self.btn19.background_color = green
                self.test += 1
                self.btn19.disabled = True
            else:
                self.btn19.background_color = red

        if id == 20:
            if self.btn20.text == str(self.test):
                self.btn20.background_color = green
                self.test += 1
                self.btn20.disabled = True
            else:
                self.btn20.background_color = red

        if self.test == 21:
            subprocess.Popen(['python', 'pocitani/win.py'])
            App.stop()
            sys.exit(0)


class CountApp(App):
    def build(self):
        return Count()


game = CountApp()
game.run()
