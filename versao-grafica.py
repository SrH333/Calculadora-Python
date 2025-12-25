import tkinter as tk

# Função que realiza o cálculo
def calcular():
    try:
        a = float(entry_a.get().replace(",", "."))
        b = float(entry_b.get().replace(",", "."))
        op = operacao.get()

        if op == "1":
            resultado = a + b
        elif op == "2":
            resultado = a - b
        elif op == "3":
            resultado = a * b
        elif op == "4":
            if b == 0:
                raise ZeroDivisionError("Divisão por zero")
            resultado = a / b
        else:
            resultado = "Operação inválida"

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro: valores inválidos")
    except ZeroDivisionError as e:
        label_resultado.config(text=f"Erro: {e}")

# Funções de navegação
def mostrar_tela_menu():
    tela_operacao.pack_forget()
    tela_menu.pack()

def mostrar_tela_operacao(op):
    operacao.set(op)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_resultado.config(text="Resultado:")
    tela_menu.pack_forget()
    tela_operacao.pack()

# Janela principal
root = tk.Tk()
root.title("Calculadora Básica")

operacao = tk.StringVar()

# === Tela Menu ===
tela_menu = tk.Frame(root)
tk.Label(tela_menu, text="Escolha a operação:", font=("Arial", 14)).pack(pady=10)

tk.Button(tela_menu, text="Somar", width=20, command=lambda: mostrar_tela_operacao("1")).pack(pady=5)
tk.Button(tela_menu, text="Subtrair", width=20, command=lambda: mostrar_tela_operacao("2")).pack(pady=5)
tk.Button(tela_menu, text="Multiplicar", width=20, command=lambda: mostrar_tela_operacao("3")).pack(pady=5)
tk.Button(tela_menu, text="Dividir", width=20, command=lambda: mostrar_tela_operacao("4")).pack(pady=5)
tk.Button(tela_menu, text="Sair", width=20, command=root.quit).pack(pady=20)

# === Tela Operação ===
tela_operacao = tk.Frame(root)

tk.Label(tela_operacao, text="Digite o primeiro valor:", font=("Arial", 12)).pack(pady=5)
entry_a = tk.Entry(tela_operacao)
entry_a.pack()

tk.Label(tela_operacao, text="Digite o segundo valor:", font=("Arial", 12)).pack(pady=5)
entry_b = tk.Entry(tela_operacao)
entry_b.pack()

label_resultado = tk.Label(tela_operacao, text="Resultado:", font=("Arial", 12))
label_resultado.pack(pady=10)

tk.Button(tela_operacao, text="Calcular", width=20, command=calcular).pack(pady=5)
tk.Button(tela_operacao, text="Voltar ao menu", width=20, command=mostrar_tela_menu).pack(pady=5)
tk.Button(tela_operacao, text="Sair", width=20, command=root.quit).pack(pady=5)

# Iniciar com tela de menu
tela_menu.pack()
root.mainloop()
