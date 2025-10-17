# PARTE 1 TRABALHO 1

# Inicia as listas
produtos = []
codigos = []
precos = []

# Inicia a função de inclusão de produtos no sistema e retorna as listas
def produto_cdg_preco(produto, codigo, preco):
    # Inclui o produto digitado na lista produtos
    produtos.append(produto)
    # Inclui o preço digitado na lista de preços
    precos.append(preco)
    # Inclui o código digitado a lista de códigos
    codigos.append(codigo)
    # Retorna as listas
    return produtos, codigos, precos

# Faz uma contagem de 2 produtos que serão cadastrados no sistema (originalmente 25, alterado para 2 para teste rápido)
for i in range(2): # Mantido como 2 para facilitar o teste, como no seu código original
    # Recebe uma entrada de um produto
    produto = input("Digite o produto:")
    # Recebe a entrada do código desse produto
    codigo = input("Digite o código do produto:")
    # Recebe a entrada do preço desse produto
    preco = float(input("Digite o preço do respectivo produto:"))
    # Chama a função para adicionar o produto
    produto_cdg_preco(produto, codigo, preco)

# Imprime as três listas do sistema
print("\n--- Produtos Cadastrados ---")
print("PRODUTOS:", produtos)
print("CÓDIGOS:", codigos)
print("PREÇOS:", precos)

# PARTE 2 TRABALHO 1

# Inicia as listas para a compra
codigo_comp = []       # Lista para guardar os códigos dos produtos já adicionados à compra
produtos_comp = []     # Lista para guardar os nomes dos produtos comprados
quantidade = []        # Lista para guardar a quantidade de cada produto comprado
preco_produtos = []    # Lista para guardar o preço unitário de cada produto comprado
valor_produtos = []    # Lista para guardar o valor total (preço * quantidade) de cada produto

# Inicia um laço de repetição para a compra
print("\n--- Início da Compra (digite '0' para finalizar) ---")
while True:
    # Recebe uma entrada de um código de produto
    cdg_comp = input("Digite o código do produto (ou '0' para finalizar):")

    # Coloca uma condição no laço de repetição: Se a entrada do código for "0", o laço para de rodar
    if cdg_comp == "0":
        break

    # Condição: Se o código digitado estiver dentro da lista de códigos de produtos cadastrados
    if cdg_comp in codigos:
        # Verifica se o produto já está na lista de compras (codigo_comp)
        if cdg_comp in codigo_comp:
            # Se o item já existir na lista de ITENS_COMPRADOS (representado por codigo_comp)
            # Localiza o item na lista codigo_comp e identifica seu índice (posição)
            indice_existente = codigo_comp.index(cdg_comp)

            # Pergunta ao usuário a quantidade a ser adicionada
            quant_adicional = int(input(f"O produto '{produtos_comp[indice_existente]}' já está na lista. Deseja adicionar mais quantos? "))
            # Soma a quantidade adicional à quantidade existente
            quantidade[indice_existente] += quant_adicional
            print(f"Agora o produto '{produto_comp}' tem '{quantidade[indice_existente]}'")

            # Recalcula o valor total para esse item específico na lista valor_produtos
            preco_unitario = preco_produtos[indice_existente]
            nova_quantidade = quantidade[indice_existente]
            valor_produtos[indice_existente] = preco_unitario * nova_quantidade

        else:
            # Se o produto é novo na compra
            # Cria uma variável para guardar o índice do código digitado na lista "codigos"
            indice = codigos.index(cdg_comp)

            # Adiciona o código do produto à lista de códigos da compra
            codigo_comp.append(cdg_comp)

            # Cria uma variável para guardar o nome do produto comprado, de acordo com o mesmo índice da entrada
            produto_comp = produtos[indice]
            # Inclui a informação do respectivo índice na lista de produtos comprados
            produtos_comp.append(produto_comp)

            # Cria uma variável para guardar o preço do produto comprado, de acordo com o mesmo índice da entrada
            preco_produto = precos[indice]
            # Inclui a informação do respectivo índice na lista de preços dos produtos
            preco_produtos.append(preco_produto)

            # Recebe uma entrada da quantidade do produto
            quant = int(input(f"Digite a quantidade para '{produto_comp}':"))
            # Inclui a entrada de quantidade na lista de "quantidade"
            quantidade.append(quant)

            # Cria uma variável para guardar o valor total do produto "da vez"
            valor_prod = preco_produto * quant
            # Inclui o valor total do produto da vez na lista de valor dos produtos
            valor_produtos.append(valor_prod)
            print(f"'{produto_comp}' adicionado à compra.")

    # Coloca uma condição na entrada do código: Se o código digitado não estiver na lista de códigos cadastrados
    elif cdg_comp not in codigos:
        print("Produto não encontrado, tente novamente!")

# Calcula o valor total de todas as compras somando os valores individuais dos produtos
valor_total_compra = sum(valor_produtos)

# Imprime todas as listas de compra
print("\n--- Resumo da Compra ---")
print("Códigos comprados:", codigo_comp)
print("Produtos comprados:", produtos_comp)
print("Quantidade de produtos:", quantidade)
print("Preço unitário dos produtos:", preco_produtos)
print(f"Valor total por produto:{valor_produtos:.2f}")
print(f"Valor total das compras: R$ {valor_total_compra:.2f}")

