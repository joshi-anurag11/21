from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (300, 500)

kv = '''

Screen:
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            type:'top'
            title: 'Vaidehi'
            md_bg_color: 207/255.0,180/255.0,191/255.0,1
            specific_text_color: 1,1,1,1
            elevation: 8
    
            
        MDFloatLayout:
        
            MDFloatingActionButton:
                size_hint: None,None
                size: 40,40
                icon: "plus"
                md_bg_color: 207/255.0,180/255.0,191/255.0,1
                text_color: 1,1,1,1
                pos_hint: {'center_x':0.5,'center_y':0.2}
                elevation: 8
                                
<content>
    orientation: "vertical"

    MDTextField:
        hint_text: "Enter your dream"
                   
'''


class content(MDBoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        screen = Builder.load_string(kv)
        return screen



MainApp().run()
