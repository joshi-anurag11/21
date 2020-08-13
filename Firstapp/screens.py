from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Example Tabs"

    MDTabs:
        id: tabs
        anim_duration:0.2
        tab_indicator_anim:True
        on_tab_switch: app.on_tab_switch(*args)


<Tab>:

    MDList:
        OneLineListItem:
            text:'Heyy Bro'
            
    MDFlatButton:
        text:'OK'
'''


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Example(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.tabs.add_widget(Tab(text='Hi'))
        self.root.ids.tabs.add_widget(Tab(text='Heyy'))
        self.root.ids.tabs.add_widget(Tab(text='How'))
        self.root.ids.tabs.add_widget(Tab(text='Sup'))


    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        pass


Example().run()
