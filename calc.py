import tkinter as tk
from tkinter import messagebox

def clique(botao):
    if botao == '=':
        try:
            conta = entrada.get().replace(',', '.').replace('×', '*').replace('÷', '/') 
            resultado.set("Resultado: " + str(eval(conta)))
        except:
            messagebox.showerror("Erro", "Conta inválida.")
            entrada.delete(0, tk.END)
    elif botao == 'Limpar':
        entrada.delete(0, tk.END)
        resultado.set("")
    else:
        entrada.insert(tk.END, botao if botao != ',' else '.')

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

entrada = tk.Entry(janela, font=("Arial", 20), justify="right")
entrada.pack(padx=10, pady=10, fill="x")

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, font=("Arial", 14), anchor="e").pack(padx=10, fill="x")

botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', ',', '=', '+'],
    ['Limpar']
]

for linha in botoes:
    quadro = tk.Frame(janela)
    quadro.pack(expand=True, fill="both", padx=10)
    for b in linha:
        tk.Button(
            quadro, text=b, font=("Arial", 16),
            command=lambda x=b: clique(x)
        ).pack(side="left", expand=True, fill="both", padx=3, pady=5)

janela.mainloop()
