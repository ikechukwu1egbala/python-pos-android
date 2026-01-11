import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

API_URL = "http://127.0.0.1:8000"

class POSApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.output = Label(text="POS Ready")
        layout.add_widget(self.output)

        load_btn = Button(text="Load Products")
        load_btn.bind(on_press=self.load_products)
        layout.add_widget(load_btn)

        sale_btn = Button(text="Make Sale (10.0)")
        sale_btn.bind(on_press=self.make_sale)
        layout.add_widget(sale_btn)

        return layout

    def load_products(self, instance):
        r = requests.get(f"{API_URL}/products")
        self.output.text = str(r.json())

    def make_sale(self, instance):
        r = requests.post(f"{API_URL}/sales", params={"total": 10.0})
        self.output.text = "Sale Recorded"

if __name__ == "__main__":
    POSApp().run()
  
