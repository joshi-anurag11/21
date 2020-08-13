from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (300, 500)

kv = '''
Screen:
    BoxLayout:
        adaptive_height: True
        adaptive_height: True
        adaptive_size: True
        orientation:'vertical'
        MDToolbar:
            title: 'Example'
            elevation: 10
        
        MDLabel:
            text:'hi'
            halign:'center'
            
        
            
        MDFloatingActionButton:
            icon: 'plus'
            pos_hint: {'center_x':0.5,'center_y':0.5}
            
        
            
'''


class ThisApp(MDApp):
    def build(self):
        s = Builder.load_string(kv)
        return (s)


ThisApp().run()
