"""
Calculadora Python básica (interativa)

Uso:
 - Execute sem argumentos para modo interativo.
 - Execute com `--demo` para rodar um pequeno teste automático.

Menu: escolha a operação, digite o primeiro e segundo valores, veja o resultado.
Após o resultado, escolha voltar ao menu ou sair.
"""

import sys


def get_number(prompt):
	while True:
		try:
			raw = input(prompt).strip()
			if raw == "":
				print("Entrada vazia. Digite um número.")
				continue
			# aceita vírgula como separador decimal
			return float(raw.replace(",", "."))
		except ValueError:
			print("Entrada inválida. Digite um número válido.")


def calculate(choice, a, b):
	if choice == "1":
		return a + b
	if choice == "2":
		return a - b
	if choice == "3":
		return a * b
	if choice == "4":
		if b == 0:
			raise ZeroDivisionError("Divisão por zero")
		return a / b
	raise ValueError("Operação desconhecida")


def print_menu():
	print("\n=== Calculadora Básica ===")
	print("1) Somar")
	print("2) Subtrair")
	print("3) Multiplicar")
	print("4) Dividir")
	print("5) Sair")


def main():
	while True:
		print_menu()
		choice = input("Escolha a operação (1-5): ").strip()
		if choice == "5":
			print("Encerrando...")
			break
		if choice not in ("1", "2", "3", "4"):
			print("Opção inválida. Tente novamente.")
			continue

		a = get_number("Digite o primeiro valor: ")
		b = get_number("Digite o segundo valor: ")

		try:
			result = calculate(choice, a, b)
		except ZeroDivisionError:
			print("Erro: divisão por zero não permitida.")
			# após erro, oferece voltar ao menu ou sair
			post_error = input("\n1 - Voltar ao menu\n2 - Sair\nEscolha: ").strip()
			if post_error == "1":
				continue
			else:
				print("Encerrando...")
				break

		print(f"\nResultado: {result}\n")

		print("O que deseja fazer a seguir?")
		print("1) Voltar ao menu")
		print("2) Sair")
		next_choice = input("Escolha: ").strip()
		if next_choice == "1":
			continue
		else:
			print("Encerrando...")
			break


def demo():
	print("Executando demo rápido da calculadora:\n")
	samples = [
		("Soma", 1, 2, "1"),
		("Subtração", 5, 3, "2"),
		("Multiplicação", 4, 2.5, "3"),
		("Divisão", 10, 2, "4"),
	]
	for name, a, b, op in samples:
		try:
			res = calculate(op, a, b)
			print(f"{name}: {a} {'+' if op=='1' else '-' if op=='2' else '*' if op=='3' else '/'} {b} = {res}")
		except Exception as e:
			print(f"{name}: erro -> {e}")


if __name__ == "__main__":
	if "--demo" in sys.argv:
		demo()
	else:
		try:
			main()
		except (KeyboardInterrupt, EOFError):
			print("\nEncerrando...")

