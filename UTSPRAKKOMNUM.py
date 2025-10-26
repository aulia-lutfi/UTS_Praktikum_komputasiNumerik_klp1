from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from sympy import symbols, diff, sympify, lambdify
from kivy.graphics import Color, Rectangle


# --- Warna dasar aplikasi ---
Window.clearcolor = (1, 0.694, 1)  # pink pastel background


# --- Label dengan kotak warna (agar mirip input box) ---
class BoxLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.949, 0.494, 0.820, 1)  # ungu pastel
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.halign = "left"
        self.valign = "middle"
        self.bind(size=self._update_rect, pos=self._update_rect)
        self.bind(size=self._update_text_size)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def _update_text_size(self, *args):
        self.text_size = (self.width, self.height)

# --- Layout utama aplikasi ---
class NewtonLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # --- Bagian input parameter ---
        input_layout = GridLayout(cols=2, row_default_height=35, size_hint_y=0.4, spacing=5)

        # Input persamaan f(x)
        input_layout.add_widget(Label(text="Persamaan f(x):", color=(0, 0, 0), font_size=16, halign="right"))
