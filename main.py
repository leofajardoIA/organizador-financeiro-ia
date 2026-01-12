import csv

print("=== Organizador Financeiro ===")

arquivo = "gastos.csv"
total = 0

while True:
    descricao = input("Digite a descrição do gasto (ou 'sair' para finalizar): ")

    if descricao.lower() == "sair":
        break

    valor = float(input("Digite o valor do gasto: "))

    with open(arquivo, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([descricao, valor])

    total += valor
    print("Gasto salvo com sucesso!\n")

print(f"\nTotal gasto nesta sessão: R$ {total:.2f}")
print("Dados salvos em 'gastos.csv'")
print("Projeto em desenvolvimento 🚀")

