from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        lbl1 = BoxLayout(orientation="vertical")
        lbl2 = BoxLayout(orientation="vertical")
        txt = Label(text="Выбери экран")
        btn1 = Button(text="Экран №1")
        btn2 = Button(text="Экран №2")
        btn3 = Button(text="Экран №3")
        btn4 = Button(text="Экран №4")
        mainlbl = BoxLayout()
        mainlbl.add_widget(lbl1)

        lbl1.add_widget(txt)

        lbl2.add_widget(btn1)
        lbl2.add_widget(btn2)
        lbl2.add_widget(btn3)
        lbl2.add_widget(btn4)

        btn1.on_press = self.scr1
        btn2.on_press = self.scr2
        btn3.on_press = self.scr3
        btn4.on_press = self.scr4

        mainlbl.add_widget(lbl2)

        self.add_widget(mainlbl)

    def scr1(self):
        self.manager.transition.direction = 'down'

        self.manager.current = 'first'

    def scr2(self):
        self.manager.transition.direction = 'down'

        self.manager.current = 'second'

    def scr3(self):
        self.manager.transition.direction = 'down'

        self.manager.current = 'tri'

    def scr4(self):
        self.manager.transition.direction = 'down'

        self.manager.current = 'chetire'


class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        btn = Button(text="Главный экран")
        txt = Label(text="1", color=(1, 0, 1))
        btnb = Button(text=">>>")
        lbl = BoxLayout()

        btn.on_press = self.back
        btnb.on_press = self.next
        self.add_widget(lbl)

        lbl.add_widget(btn)
        lbl.add_widget(txt)
        lbl.add_widget(btnb)

    def back(self):
        self.manager.transition.direction = 'down'

        self.manager.current = 'main'

    def next(self):
        self.manager.transition.direction = 'left'

        self.manager.current = 'second'


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="<<<")
        txt = Label(text="2", color=(1, 0, 1))

        tim = TextInput(text="Введите пароль!", multiline=False)
        tim.bind(text=self.on_txt)
        btnb = Button(text=">>>")
        lbl = BoxLayout()
        btnb.on_press = self.next
        btn.on_press = self.back

        self.add_widget(lbl)

        lbl.add_widget(btn)
        lbl.add_widget(txt)
        lbl.add_widget(tim)
        lbl.add_widget(btnb)

    text1 = ""

    def on_txt(self, instance, value):
        if value == "1234":
            self.manager.transition.direction = 'right'

            self.manager.current = 'tri'

    def back(self):
        self.manager.transition.direction = 'right'

        self.manager.current = 'first'

    def next(self):
        print("Введите пароль!")


class TriScr(Screen):
    def __init__(self, name='tri'):
        super().__init__(name=name)
        btn = Button(text="<<<")
        txt = Label(text="3", color=(1, 0, 1))
        btnb = Button(text=">>>")
        lbl = BoxLayout()
        btnb.on_press = self.next
        btn.on_press = self.back
        self.add_widget(lbl)

        lbl.add_widget(btn)
        lbl.add_widget(txt)
        lbl.add_widget(btnb)

    def back(self):
        self.manager.transition.direction = 'right'

        self.manager.current = 'second'

    def next(self):
        self.manager.transition.direction = 'left'

        self.manager.current = 'chetire'


class chetireScr(Screen):
    def __init__(self, name='chetire'):
        super().__init__(name=name)
        btn = Button(text="<<<")
        txt = Label(text="4", color=(1, 0, 1))
        btnb = Button(text="Главный экран")
        lbl = BoxLayout()
        btnb.on_press = self.next
        btn.on_press = self.back
        self.add_widget(lbl)

        lbl.add_widget(btn)
        lbl.add_widget(txt)
        lbl.add_widget(btnb)

    def back(self):
        self.manager.transition.direction = 'right'

        self.manager.current = 'tri'

    def next(self):
        self.manager.transition.direction = 'up'

        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(TriScr())
        sm.add_widget(chetireScr())

        return sm


app = MyApp()
app.run()
