from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (300, 500)

kv = '''

Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Anurag'
            md_bg_color: 171/255.0,194/255.0,232/255.0,1 
            specific_text_color: 1,1,1,1
            
        MDTabs:
            anim_duration:0.2
            tab_bar_height: '45dp'
            tab_indicator_anim:True
            color_indicator: 1,1,1,1
            background_color: 171/255.0,194/255.0,232/255.0,1
            id: tabs
            Tab1:
                text:'Dreams'
                
                id:tab1
                ScrollView:
                    MDList:
                        padding: 10
                        id:container
                        text_color:54/255.0,75/255.0,109/255.0,1

                MDFloatingActionButton:
                    size_hint: None,None
                    size: 40,40
                    icon: "plus"
                    pos_hint: {'center_x':0.5,'center_y':0.14}
                    md_bg_color: 171/255.0,194/255.0,232/255.0,1
                    text_color: 1,1,1,1
                    elevation_normal: 8
                    on_release: app.show_dialog()

            Tab2:
                text:'Progress'   





<content>:
    id:content
    orientation:'vertical'
    size_hint_y: None
    spacing: '12dp'
    height: '53dp'

    MDTextField:
        id: user_text
        hint_text:'Enter your dream' 
        color_mode:'custom'
        line_color_focus:54/255.0,75/255.0,109/255.0,1
        required:1

<Tab1>:

<Tab2>:


'''


class Tab2(FloatLayout, MDTabsBase):
    pass


class Tab1(FloatLayout, MDTabsBase):
    pass


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
                                   MDFlatButton(text='CANCEL', on_release=self.close,
                                                text_color=(54 / 255.0, 75 / 255.0, 109 / 255.0, 1)),
                                   MDFlatButton(text='OK', on_release=self.add_list,
                                                text_color=(54 / 255.0, 75 / 255.0, 109 / 255.0, 1))
                               ]
                               )
        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()

    def add_list(self, obj):
        user_text = self.dialog.content_cls.ids.user_text.text
        if len(user_text) > 0:
            item = OneLineListItem(text=user_text,
                                   theme_text_color='Custom',
                                   text_color=(54 / 255.0, 75 / 255.0, 109 / 255.0, 1))
            self.root.ids.container.add_widget(item)
            self.dialog.dismiss()
        else:
            pass


MainApp().run()
