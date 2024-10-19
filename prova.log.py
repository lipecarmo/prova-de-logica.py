# Criando um dicionário para armazenar os produtos e preços

produtos = {}

# Pedindo ao usuário para inserir o nome e o preço de cinco produtos

for i in range(5):
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    produtos[nome_produto] = preco_produto

# Calculando o valor total da compra

valor_total = sum(produtos.values())

# Exibindo o valor total da compra

print(f"O valor total da compra é: R${valor_total:.2f}")
