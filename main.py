import kivy
from kivy.app import App
from kivy.uix.label import Label

class FoodApp(App):
    def build(self):
        return Label(text="FoodApp")

if __name__ == "__main__":
    FoodApp().run()