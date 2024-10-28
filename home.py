import certifi
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen

from mydatabase import Database
from styles import Styles
from login import Login

Builder.load_string("""
#: import CButton custom_widget
#: import CTextInput custom_widget
<Home>:
    name: "Home"
    FloatLayout:
        Image:
            id: bg_img
            source:"background.png"
            fit_mode: "contain"
            pos_hint: {"center_x":0.5, "top":1.1}
            #size_hint_y: None
            #width: dp(50)
                
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_y: None
            height: dp(60)
            Label:
                text: "Interesting numbers"
                font_name: "robotoblack.ttf"
                font_size: '20sp'
            AnchorLayout:
                anchor_x: "right"
                #anchor_y: "center"
                padding: [0,0,dp(30),0]
                Button:
                    canvas.before:
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: "history.png"
                    size_hint: None, None
                    size: dp(35), dp(35)
                    background_normal: ""
                    background_color: 0,0,0,0
                    on_press: root.switchToHistory()
        BoxLayout:
            Label:
                id: result_placeholder      
                text_size: self.width, None      
                padding: [dp(20) , dp(20)]    
                color: root.secondary_color
        AnchorLayout:
            anchor_x: "center"
            anchor_y: "center"
            size_hint: 1, 0.3
                
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(30)
                spacing: dp(10)
                BoxLayout:
                    size_hint: 1, 0.65
                    spacing: dp(10)
                    BoxLayout:
                        orientation: "vertical"
                        spacing: dp(10)
                        Label:                           
                            text: "Day"
                            color:  root.secondary_color
                            size_hint_y: None
                            size: self.texture_size
                            font_name: "robotomedium.ttf"
                            font_size: '18sp'
                            halign: "left"
                            text_size: self.size
                        CTextInput:
                            id: day
                            size_hint_y: None
                            height: dp(50)
                    BoxLayout:
                        orientation: "vertical"
                        spacing: dp(10)
                        Label:                            
                            text: "Month"
                            color: root.secondary_color
                            size_hint_y: None
                            size: self.texture_size
                            font_name: "robotomedium.ttf"
                            font_size: '18sp'
                            halign: "left"
                            text_size: self.size
                        CTextInput:
                            id: month
                            size_hint_y: None
                            height: dp(50)
                CButton:
                    text: "Display Fact"
                    font_name: "robotomedium.ttf"
                    font_size: '18sp'
                    size_hint_y: None
                    height: dp(60)
                    on_press: root.getFact()
                    
                
""")

class Home(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color
    def switchToHistory(self):
        self.manager.current = "History"
    def response(self, req_body, result):
        print(result)
        self.ids.bg_img.color = (1,1,1,0.3)
        self.ids.result_placeholder.text = result
        Database.insertFact(Login.getEmail(),result)
    def getFact(self):
        day = self.ids.day.text
        month = self.ids.month.text
        url = f"https://numbersapi.p.rapidapi.com/{month}/{day}/date"
        headers = {
            "X-RapidAPI-Key": "2b70ce5ad5msha80c4a7354a73fep1253a2jsn9d164bb59240",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }
        UrlRequest(url, req_headers=headers, on_success=self.response, ca_file=certifi.where(), verify=True)