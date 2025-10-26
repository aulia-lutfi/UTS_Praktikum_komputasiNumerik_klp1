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
        self.fx_input = TextInput(
            text='',
            multiline=False,
            size_hint_y=None,
            height=30,
            background_color=(0.949, 0.494, 0.820, 1),
            foreground_color=(0, 0, 0)
        )
        input_layout.add_widget(self.fx_input)

        # Label turunan otomatis (tampil langsung setiap kali input berubah)
        input_layout.add_widget(Label(text="f'(x) (turunan):", color=(0, 0, 0), font_size=16, halign="right"))
        self.fpx_label = BoxLabel(
            text="(otomatis muncul saat mengetik)",
            color=(0, 0, 0),
            font_size=14,
            size_hint_y=None,
            height=30
        )
        input_layout.add_widget(self.fpx_label)

        # Input x₀
        input_layout.add_widget(Label(text="x0:", color=(0, 0, 0), font_size=16, halign="right"))
        self.x0_input = TextInput(
            text='',
            multiline=False,
            size_hint_y=None,
            height=30,
            background_color=(0.949, 0.494, 0.820, 1),
            foreground_color=(0, 0, 0)
        )
        input_layout.add_widget(self.x0_input)

        # Input toleransi ε
        input_layout.add_widget(Label(text="ε (toleransi):", color=(0, 0, 0), font_size=16, halign="right"))
        self.e_input = TextInput(
            text='',
            multiline=False,
            size_hint_y=None,
            height=30,
            background_color=(0.949, 0.494, 0.820, 1),
            foreground_color=(0, 0, 0)
        )
        input_layout.add_widget(self.e_input)

        # Input jumlah iterasi maksimum n
        input_layout.add_widget(Label(text="n (maks iterasi):", color=(0, 0, 0), font_size=16, halign="right"))
        self.n_input = TextInput(
            text='',
            multiline=False,
            size_hint_y=None,
            height=30,
            background_color=(0.949, 0.494, 0.820, 1),
            foreground_color=(0, 0, 0)
        )
        input_layout.add_widget(self.n_input)

        self.add_widget(input_layout)

        # --- Bind agar turunan langsung muncul saat persamaan diubah ---
        self.fx_input.bind(text=self.update_derivative)

        # --- Tombol hitung ---
        self.calc_button = Button(
            text="🔹 Hitung Akar (Newton-Raphson)",
            size_hint=(1, 0.1),
            background_color=(0.949, 0.494, 0.820, 1),
            color=(1, 1, 1),
            font_size=16
        )
        self.calc_button.bind(on_press=self.hitung)
        self.add_widget(self.calc_button)

        # --- Area hasil (tabel dalam ScrollView) ---
        self.result_layout = GridLayout(cols=5, spacing=4, size_hint_y=None)
        self.result_layout.bind(minimum_height=self.result_layout.setter('height'))

        scroll = ScrollView(size_hint=(1, 0.5))
        scroll.add_widget(self.result_layout)
        self.add_widget(scroll)
        
     # --- Fungsi untuk memperbarui turunan otomatis ---
    def update_derivative(self, instance, value):
        x = symbols('x')
        value = value.strip()
        
        if not value:  # kosong
            self.fpx_label.text = "(persamaan belum diinput)"
            return
        
        try:
            expr = sympify(value)
            expr_diff = diff(expr, x)
            self.fpx_label.text = str(expr_diff)
        except Exception:
            self.fpx_label.text = "(persamaan tidak valid)"

    # --- Fungsi bantu untuk tabel hasil ---
    def clear_table(self):
        self.result_layout.clear_widgets()

    def add_header(self):
        headers = ["Iterasi", "xi", "f(xi)", "f'(xi)", "|xi+1-xi|"]
        for h in headers:
            self.result_layout.add_widget(Label(
                text=f"[b]{h}[/b]",
                markup=True,
                color=(0, 0, 0),
                size_hint_y=None,
                height=30
            ))

    def add_row(self, data, color=(0, 0, 0)):
        for val in data:
            self.result_layout.add_widget(Label(
                text=str(val),
                color=color,
                font_size=14,
                size_hint_y=None,
                height=25
            ))
