print("=== Organizador Financeiro ===")

gastos = []
total = 0

while True:
    descricao = input("Digite a descrição do gasto (ou 'sair' para finalizar): ")

    if descricao.lower() == "sair":
        break

    valor = float(input("Digite o valor do gasto: "))

    gastos.append((descricao, valor))
    total += valor

    print("Gasto registrado!\n")

print("\nResumo dos gastos:")
for item in gastos:
    print(f"- {item[0]}: R$ {item[1]:.2f}")

print(f"\nTotal gasto: R$ {total:.2f}")
print("Projeto em desenvolvimento 🚀")


