import pickle
import random
import sys
import subprocess
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.config import Config


zadani = pickle.load(open("gramatika/data.dat", "rb"))
print(zadani)

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)


class Okno(Widget):
    l0 = ObjectProperty(None)
    l1 = ObjectProperty(None)
    l2 = ObjectProperty(None)
    l3 = ObjectProperty(None)
    l4 = ObjectProperty(None)
    l5 = ObjectProperty(None)
    l6 = ObjectProperty(None)
    l7 = ObjectProperty(None)
    l8 = ObjectProperty(None)
    l9 = ObjectProperty(None)

    t0 = ObjectProperty(None)
    t1 = ObjectProperty(None)
    t2 = ObjectProperty(None)
    t3 = ObjectProperty(None)
    t4 = ObjectProperty(None)
    t5 = ObjectProperty(None)
    t6 = ObjectProperty(None)
    t7 = ObjectProperty(None)
    t8 = ObjectProperty(None)
    t9 = ObjectProperty(None)

    button = ObjectProperty(None)
    pb = 0
    c = ['', '', '', '', '', '', '', '', '', '']

    def btn(self):
        if self.pb == 0:
            self.pb = 1
            self.button.text = "Zkontrolovat"

            s = 0
            for x in range(10):
                s = 0
                while s == 0:
                    self.c[x] = random.randint(0, len(zadani) - 1)
                    s = 1
                    for y in range(len(zadani) - 1):
                        if self.c[x] == self.c[y]:
                            if x != y:
                                s = 0

            self.l0.text = zadani[self.c[0]][0]
            self.l1.text = zadani[self.c[1]][0]
            self.l2.text = zadani[self.c[2]][0]
            self.l3.text = zadani[self.c[3]][0]
            self.l4.text = zadani[self.c[4]][0]
            self.l5.text = zadani[self.c[5]][0]
            self.l6.text = zadani[self.c[6]][0]
            self.l7.text = zadani[self.c[7]][0]
            self.l8.text = zadani[self.c[8]][0]
            self.l9.text = zadani[self.c[9]][0]
        else:
            ch = 0
            if self.t0.text == zadani[self.c[0]][1]:
                self.l0.color = 0, 1, 0, 1
            else:
                self.l0.color = 1, 0, 0, 1
                ch += 1

            if self.t1.text == zadani[self.c[1]][1]:
                self.l1.color = 0, 1, 0, 1
            else:
                self.l1.color = 1, 0, 0, 1
                ch += 1

            if self.t2.text == zadani[self.c[2]][1]:
                self.l2.color = 0, 1, 0, 1
            else:
                self.l2.color = 1, 0, 0, 1
                ch += 1

            if self.t3.text == zadani[self.c[3]][1]:
                self.l3.color = 0, 1, 0, 1
            else:
                self.l3.color = 1, 0, 0, 1
                ch += 1

            if self.t4.text == zadani[self.c[4]][1]:
                self.l4.color = 0, 1, 0, 1
            else:
                self.l4.color = 1, 0, 0, 1
                ch += 1

            if self.t5.text == zadani[self.c[5]][1]:
                self.l5.color = 0, 1, 0, 1
            else:
                self.l5.color = 1, 0, 0, 1
                ch += 1

            if self.t6.text == zadani[self.c[6]][1]:
                self.l6.color = 0, 1, 0, 1
            else:
                self.l6.color = 1, 0, 0, 1
                ch += 1

            if self.t7.text == zadani[self.c[7]][1]:
                self.l7.color = 0, 1, 0, 1
            else:
                self.l7.color = 1, 0, 0, 1
                ch += 1

            if self.t8.text == zadani[self.c[8]][1]:
                self.l8.color = 0, 1, 0, 1
            else:
                self.l8.color = 1, 0, 0, 1
                ch += 1

            if self.t9.text == zadani[self.c[9]][1]:
                self.l9.color = 0, 1, 0, 1
            else:
                self.l9.color = 1, 0, 0, 1
                ch += 1

            if ch > 0:
                self.button.text = "Chyb: " + str(ch) + " | Zkontrolovat"
            else:
                self.button.text = "Vyhjál, pjvní"
                subprocess.Popen(['python', 'gramatika/win.py'])
                App.stop()
                sys.exit(0)

class GramatikaApp(App):
    def build(self):
        return Okno()


if __name__ == "__main__":
    GramatikaApp().run()
