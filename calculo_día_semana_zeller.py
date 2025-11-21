import tkinter as tk
from tkinter import messagebox

def calcular_dia():
    try:
        fecha = entrada_fecha.get()
        año, mes, dia = map(int, fecha.split('-'))
        
        # A + B - C + D
        A = año
        B = año // 4
        C = año // 100
        D = año // 400
        peso = A + B - C + D
        
        # calculo dias por mes (no bisiesto)
        dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # calculo dias de año bisiesto
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            dias_mes[2] = 29
        
        # Día del año
        dia_año = sum(dias_mes[:mes]) + dia
        
        # Resultado
        resultado = (peso + dia_año) % 7
        dias = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        
        messagebox.showinfo("Resultado", f"{fecha} = {dias[resultado]}")
    except:
        messagebox.showerror("Error", "Formato inválido. Use YYYY-MM-DD")

# Ventana
ventana = tk.Tk()
ventana.title("Calculadora Día de la Semana")
ventana.geometry("350x150")

# Widgets
tk.Label(ventana, text="Formato: AAAA-MM-DD", font=("Arial", 10)).pack(pady=10)
tk.Label(ventana, text="Ejemplo: 2025-03-15", font=("Arial", 9), fg="gray").pack()

entrada_fecha = tk.Entry(ventana, width=20, font=("Arial", 12))
entrada_fecha.pack(pady=10)

tk.Button(ventana, text="Calcular", command=calcular_dia, width=15).pack(pady=5)

ventana.mainloop()
