import math

mem = 0

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

def div(a, b):
    if b == 0: raise ValueError("Деление на ноль")
    return a / b

def power(a, b): return a ** b

def sqrt(a):
    if a < 0: raise ValueError("Корень из отрицательного")
    return math.sqrt(a)

def factorial(n):
    if not isinstance(n, int) or n < 0: raise ValueError("Некорректный факториал")
    return math.factorial(n)

def mem_save(v):
    global mem; mem = v; return mem

def mem_read(): return mem

def mem_add(v):
    global mem; mem += v; return mem

def mem_clear():
    global mem; mem = 0; return mem
import tkinter as tk
import calculator as c

root = tk.Tk()
root.title("Калькулятор")
root.geometry("320x460")

display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill="x", padx=8, pady=8)
display.insert(0, "0")

# состояние
first = {"value": None}   # первое число
op = {"fn": None}         # текущая операция

def current():
    try:
        return float(display.get())
    except ValueError:
        return 0.0

def set_display(v):
    display.delete(0, tk.END)
    display.insert(0, str(v))

def press_digit(d):
    txt = display.get()
    if txt == "0" or txt.startswith("Ошибка"):
        set_display(d)
    else:
        set_display(txt + d)

def press_dot():
    if "." not in display.get():
        set_display(display.get() + ".")

def press_op(fn):
    first["value"] = current()
    op["fn"] = fn
    set_display("0")

def press_eq():
    if op["fn"] is None:
        return
    a, b = first["value"], current()
    try:
        set_display(op["fn"](a, b))
    except Exception as e:
        set_display(f"Ошибка: {e}")
    op["fn"] = None

def unary(fn):
    try:
        set_display(fn(current()))
    except Exception as e:
        set_display(f"Ошибка: {e}")

def mem_op(fn):
    try:
        fn(current())
        set_display(c.mem_read())
    except Exception as e:
        set_display(f"Ошибка: {e}")

def clear_all():
    first["value"] = None
    op["fn"] = None
    set_display("0")

# кнопки: (текст, обработчик)
layout = [
    ("C",  clear_all),       ("MC", lambda: mem_op(c.mem_clear)), ("MR", lambda: set_display(c.mem_read())), ("MS", lambda: mem_op(c.mem_save)),
    ("7",  lambda: press_digit("7")), ("8", lambda: press_digit("8")), ("9", lambda: press_digit("9")), ("/", lambda: press_op(c.div)),
    ("4",  lambda: press_digit("4")), ("5", lambda: press_digit("5")), ("6", lambda: press_digit("6")), ("*", lambda: press_op(c.mul)),
    ("1",  lambda: press_digit("1")), ("2", lambda: press_digit("2")), ("3", lambda: press_digit("3")), ("-", lambda: press_op(c.sub)),
    ("0",  lambda: press_digit("0")), (".", press_dot),               ("=", press_eq),                  ("+", lambda: press_op(c.add)),
    ("x^y", lambda: press_op(c.power)), ("√x", lambda: unary(c.sqrt)), ("n!", lambda: unary(lambda x: c.factorial(int(x)))), ("M+", lambda: mem_op(c.mem_add)),
]

frame = tk.Frame(root)
frame.pack(padx=6, pady=6, fill="both", expand=True)

for i, (text, cmd) in enumerate(layout):
    r, col = divmod(i, 4)
    tk.Button(frame, text=text, font=("Arial", 12), width=6, height=2,
              command=cmd).grid(row=r, column=col, padx=2, pady=2)

root.mainloop()
import unittest
import calculator as c

class TestCalc(unittest.TestCase):
    def setUp(self):
        c.mem_clear()

    def test_base(self):
        self.assertEqual(c.add(2, 3), 5)
        self.assertEqual(c.sub(5, 3), 2)
        self.assertEqual(c.mul(3, 4), 12)
        self.assertEqual(c.div(10, 2), 5)
        with self.assertRaises(ValueError): c.div(1, 0)

    def test_power_sqrt(self):
        self.assertEqual(c.power(2, 3), 8)
        self.assertEqual(c.sqrt(9), 3)
        with self.assertRaises(ValueError): c.sqrt(-4)

    def test_factorial(self):
        self.assertEqual(c.factorial(5), 120)
        self.assertEqual(c.factorial(0), 1)
        with self.assertRaises(ValueError): c.factorial(-1)

    def test_memory(self):
        self.assertEqual(c.mem_save(42), 42)
        self.assertEqual(c.mem_read(), 42)
        self.assertEqual(c.mem_add(8), 50)
        self.assertEqual(c.mem_clear(), 0)

if __name__ == "__main__":
    unittest.main()
