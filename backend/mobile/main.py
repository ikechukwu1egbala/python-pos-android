from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

API_URL = "http://127.0.0.1:8000"

class POSApp(App):
    def build(self):
        self.cart = {}
        self.total = 0.0

        root = BoxLayout(orientation="horizontal", padding=10, spacing=10)

        # LEFT: Products Grid
        self.products_layout = GridLayout(cols=3, spacing=10, size_hint=(0.6, 1))
        root.add_widget(self.products_layout)

        # RIGHT: Cart Panel
        cart_panel = BoxLayout(orientation="vertical", size_hint=(0.4, 1), spacing=10)

        self.cart_label = Label(text="Cart Empty", halign="left", valign="top")
        self.cart_label.bind(size=self.cart_label.setter("text_size"))
        cart_panel.add_widget(self.cart_label)

        self.total_label = Label(text="TOTAL: $0.00", font_size=20)
        cart_panel.add_widget(self.total_label)

        checkout_btn = Button(text="CHECKOUT", size_hint=(1, 0.2))
        checkout_btn.bind(on_press=self.checkout)
        cart_panel.add_widget(checkout_btn)

        root.add_widget(cart_panel)

        self.load_products()
        return root

    def load_products(self):
        response = requests.get(f"{API_URL}/products")
        products = response.json()

        for p in products:
            btn = Button(
                text=f"{p['name']}\n${p['price']}",
                on_press=lambda _, prod=p: self.add_to_cart(prod),
            )
            self.products_layout.add_widget(btn)

    def add_to_cart(self, product):
        pid = product["id"]
        if pid not in self.cart:
            self.cart[pid] = {
                "product": product,
                "quantity": 0,
            }

        self.cart[pid]["quantity"] += 1
        self.update_cart()

    def update_cart(self):
        self.total = 0.0
        lines = []

        for item in self.cart.values():
            qty = item["quantity"]
            price = item["product"]["price"]
            subtotal = qty * price
            self.total += subtotal
            lines.append(
                f"{item['product']['name']} x{qty}  ${subtotal:.2f}"
            )

        self.cart_label.text = "\n".join(lines) or "Cart Empty"
        self.total_label.text = f"TOTAL: ${self.total:.2f}"

    def checkout(self, _):
        if not self.cart:
            return

        payload = {
            "cart": [
                {
                    "product_id": item["product"]["id"],
                    "quantity": item["quantity"],
                }
                for item in self.cart.values()
            ]
        }

        response = requests.post(f"{API_URL}/checkout", json=payload)

        if response.status_code == 200:
            self.cart.clear()
            self.update_cart()
            self.cart_label.text = "Sale Completed ✔"
        else:
            self.cart_label.text = response.json()["detail"]

if __name__ == "__main__":
    POSApp().run()
  
