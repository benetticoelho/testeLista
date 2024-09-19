from kivy.lang import Builder
from kivymd.app import MDApp
from data import  data as ListItems
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.label import MDIcon

class Test(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def on_start(self):
        self.loadItems(ListItems)

    def loadItems(self, lst):
        for it in lst:
            _it = OneLineAvatarIconListItem(
                text = it["text"]
            )

            #Criar um ícone na esquerda
            _it.add_widget(MDIcon(
                icon = it["iconLeft"],
                size_hint = (None, None),
                size = (25,25),
                pos_hint = {"center_x": 0.04, "center_y": 0.5}
            ))

            # Criar um ícone na direita
            _it.add_widget(MDIcon(
                icon=it["iconRight"],
                size_hint=(None, None),
                size=(25, 25),
                pos_hint={"center_x": 0.95, "center_y": 0.5},
                radius=10,
                theme_text_color = "Custom",
                text_color = (1, 0, 0, 1),
                opposite_colors=True,
                #md_bg_color=(1, 1, 1, 1)
            ))

            self.root.ids.box.add_widget(_it)

    def filter_text(self, texto):
        ListItems_filter = []
        if len(self.root.ids.box.children) > 0:
            self.root.ids.box.clear_widgets()
            for it in ListItems:
                if texto.upper() in it["text"].upper():
                    ListItems_filter.append(it)
            self.loadItems(ListItems_filter)
        else:
            self.loadItems(ListItems)


Test().run()