from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from mydatabase import Database
from styles import Styles

Builder.load_string("""
#: import CButton custom_widget
#: import CTextInput custom_widget
#: import SignupText custom_widget

<Login>:
    name: "login"
    BoxLayout:
        orientation:"vertical"
        padding: dp(20)
        BoxLayout:
            size_hint:1,0.25
            AnchorLayout:                    
                anchor_y: "center"
                Image:
                    source:"background.png"
                    #size_hint_y: None
                    #width: dp(50)
                        
        AnchorLayout:
            size_hint:1,0.55
            anchor_y: "top"
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: [dp(30), 0, dp(30), 0 ]
                Label:
                    text: "Login to your Account"
                    halign: "left"
                    text_size: self.size
                    #font_name: ""
                    font_size: '16sp'
                    size_hint_y: None
                    size: self.texture_size
                    color: root.secondary_color
                    
                CTextInput:
                    id: email
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Email"
                    text: "123"
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Password"
                    text: "123"
                CButton:
                    text: "Login"
                    on_press: root.login()
                    size_hint_y: None
                    height: dp(50)
                   
                
        AnchorLayout:
            size_hint:1,0.20
            anchor_x: "center"
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                Label:
                    text: "If you have no account "
                    color: root.secondary_color
                    size_hint_x: None
                    size: self.texture_size
                    
                SignupText:
                    text: "Sign-Up"
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switchToSignup()

""")
class Login(Screen):
    secondary_color = Styles.secondary_color
    email = None
    @staticmethod
    def getEmail():
        return Login.email
    def switchToSignup(self):
        self.manager.current = "signup"

    def login(self):
        Login.email = self.ids.email.text
        password = self.ids.password.text
        if(Database.isExist(Login.email,password)):
            print("Login successful")
            self.manager.current = "Home"
        else:
            print("Login failed")
