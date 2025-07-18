from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """main class for the boxlayout"""
    def build(self):
        """ create the kivy interface """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """handle the greet button on press """
        print("greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """handle the clear button on press"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()