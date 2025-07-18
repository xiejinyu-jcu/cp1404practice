"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
16/07/2025
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty



MILES_TO_KM = 1.60934



class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_text = StringProperty('')

    def build(self):
        """Build the Kivy app from the .kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.handle_calculate()
        return self.root

    def handle_calculate(self):
        """
        Handle calculation and update the output label text.
        This is called on text input change.
        """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_text = f"{result:.4f}"


    def handle_increment(self, change):
        """
        Handle up/down button presses by changing the input text.
        This will then trigger the on_text event.
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_validated_miles(self):
        """
        Get and validate the text from the input widget.
        Returns 0.0 if the input is invalid.
        """
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

MilesConverterApp().run()


