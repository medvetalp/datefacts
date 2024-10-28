from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from mydatabase import Database
from custom_widget import SignupText
from login import Login
from signup import Signup
from home import Home
from history import History

#Window.size=(480,800)
Window.softinput_mode = "below_target"
class Interface(ScreenManager):
    def __init__(self, **kwargs):
        Window.bind(on_keyboard= self.quit)
        super().__init__(**kwargs)
        try:
            Database.connectDatabase()

            login = Login()
            signup = Signup()
            home = Home()
            history = History()

            self.add_widget(login)
            self.add_widget(signup)
            self.add_widget(home)
            self.add_widget(history)

        except Exception as e:
            print(e)
    def quit(self, window, key, *args):
        if(key==27):
            App.get_running_app().stop()
class NumberApp(App):
    pass


NumberApp().run()
