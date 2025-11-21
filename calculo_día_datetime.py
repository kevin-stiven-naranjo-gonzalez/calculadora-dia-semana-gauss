import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_dia():
    try:
        fecha = entrada_fecha.get()
        fecha_dt = datetime.fromisoformat(fecha)
        dia_num = fecha_dt.weekday()
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        dia = dias[dia_num]
        messagebox.showinfo("Resultado", f"{fecha} = {dia}")
    except ValueError:
        messagebox.showerror("Error", "Formato inválido. Use YYYY-MM-DD")

# Ventana
ventana = tk.Tk()
ventana.title("Calculadora Día de la Semana (Con Datetime)")
ventana.geometry("350x150")

# Widgets
tk.Label(ventana, text="Formato: AAAA-MM-DD", font=("Arial", 10)).pack(pady=10)
tk.Label(ventana, text="Ejemplo: 2025-03-15", font=("Arial", 9), fg="gray").pack()

entrada_fecha = tk.Entry(ventana, width=20, font=("Arial", 12))
entrada_fecha.pack(pady=10)

tk.Button(ventana, text="Calcular", command=calcular_dia, width=15).pack(pady=5)

ventana.mainloop()
