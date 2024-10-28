from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from mydatabase import Database
from styles import Styles

Builder.load_string("""
#: import CButton custom_widget
#: import CTextInput custom_widget

<Signup>:
    name: "signup"
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
            size_hint:1,0.75
            anchor_y: "top"
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: [dp(30), 0, dp(30), 0 ]
                Label:
                    text: "Create your Account"
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
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Password"
                CTextInput:
                    id: cpassword
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Confirm Password"
                CButton:
                    text: "Signup"
                    on_press: root.createEntry()
                    size_hint_y: None
                    height: dp(50)
     
""")

class Signup(Screen):
    secondary_color= Styles.secondary_color
    def createEntry(self):
        email = self.ids.email.text
        password = self.ids.password.text
        cpassword = self.ids.cpassword.text
        if(password==cpassword):
            if(Database.isValid(email)):
                print(f"Email ({email}) already exists!")
            else:
                Database.insertdata(email,password)
                self.manager.current="login"


