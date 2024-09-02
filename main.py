import tkinter as tk
from tkinter import messagebox


class NumeroComplejo:
    def __init__(self, real: float, imaginario: float):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        signo = '+' if self.imaginario >= 0 else ''
        return f"{self.real} {signo}{self.imaginario}i"

    def sumar(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def restar(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicar(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def dividir(self, otro):
        divisor = otro.real ** 2 + otro.imaginario ** 2
        if divisor == 0:
            raise ValueError("No se puede dividir por 0")

        real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return NumeroComplejo(real, imaginario)


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones con Números Complejos")
        self.root.geometry("400x300")

        # Entradas para el primer número complejo
        tk.Label(root, text="Primer número complejo").pack(pady=5)
        self.real1 = tk.Entry(root)
        self.real1.pack(pady=5)
        self.imaginario1 = tk.Entry(root)
        self.imaginario1.pack(pady=5)

        # Entradas para el segundo número complejo
        tk.Label(root, text="Segundo número complejo").pack(pady=5)
        self.real2 = tk.Entry(root)
        self.real2.pack(pady=5)
        self.imaginario2 = tk.Entry(root)
        self.imaginario2.pack(pady=5)

        # Botones de operaciones
        tk.Button(root, text="Sumar", command=self.sumar).pack(pady=5)
        tk.Button(root, text="Restar", command=self.restar).pack(pady=5)
        tk.Button(root, text="Multiplicar", command=self.multiplicar).pack(pady=5)
        tk.Button(root, text="Dividir", command=self.dividir).pack(pady=5)

    def obtener_complejos(self):
        # Obtener los valores ingresados y crear los números complejos
        real1 = float(self.real1.get())
        imaginario1 = float(self.imaginario1.get())
        real2 = float(self.real2.get())
        imaginario2 = float(self.imaginario2.get())
        complejo1 = NumeroComplejo(real1, imaginario1)
        complejo2 = NumeroComplejo(real2, imaginario2)
        return complejo1, complejo2

    def mostrar_resultado(self, operacion, resultado):
        messagebox.showinfo("Resultado", f"{operacion}: {resultado}")

    def sumar(self):
        complejo1, complejo2 = self.obtener_complejos()
        resultado = complejo1.sumar(complejo2)
        self.mostrar_resultado("Suma", resultado)

    def restar(self):
        complejo1, complejo2 = self.obtener_complejos()
        resultado = complejo1.restar(complejo2)
        self.mostrar_resultado("Resta", resultado)

    def multiplicar(self):
        complejo1, complejo2 = self.obtener_complejos()
        resultado = complejo1.multiplicar(complejo2)
        self.mostrar_resultado("Multiplicación", resultado)

    def dividir(self):
        try:
            complejo1, complejo2 = self.obtener_complejos()
            resultado = complejo1.dividir(complejo2)
            self.mostrar_resultado("División", resultado)
        except ValueError as e:
            messagebox.showerror("Error", str(e))


# Crear la ventana principal
root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
