from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (300, 500)

kv = '''

Screen:
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Anurag'
            md_bg_color: 207/255.0,180/255.0,191/255.0,1
            specific_text_color: 1,1,1,1
            elevation: 8    
        ScrollView:
            MDList:
                id:container
        
        MDFloatingActionButton:
            size_hint: None,None
            size: 40,40
            icon: "plus"
            md_bg_color: 207/255.0,180/255.0,191/255.0,1
            text_color: 1,1,1,1
            pos_hint: {'center_x':0.5,'center_y':0.15}
            elevation_normal: 8
            on_release: app.show_dialog()
            
        MDFlatButton:
            size:10,10

<content>:
    id:content
    orientation:'vertical'
    size_hint_y: None
    spacing: '12dp'
    height: '53dp'
    MDTextField:
        id: user_text
        hint_text:'Enter your dream'
        required: True                                                      
'''


class content(MDBoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(kv)
        return self.screen

    def show_dialog(self):
        self.dialog = MDDialog(title='Dream',
                               auto_dismiss=False,
                               type='custom',
                               content_cls=content(),
                               size_hint=(0.8, 0.3),
                               buttons=[
                                   MDFlatButton(text='CANCEL', on_release=self.close),
                                   MDFlatButton(text='OK', on_release=self.add_list)
                               ]
                               )
        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()

    def add_list(self, obj):
        user_text = self.dialog.content_cls.ids.user_text.text
        if len(user_text) > 0:
            item = OneLineListItem(text=user_text)
            self.root.ids.container.add_widget(item)
            self.dialog.dismiss()
        else:
            pass


MainApp().run()
