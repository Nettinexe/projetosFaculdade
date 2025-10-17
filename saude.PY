# Listas para armazenar as senhas de cada categoria
cat1 = []  # Categoria 1: Idosos com convênio
cat2 = []  # Categoria 2: Idosos sem convênio
cat3 = []  # Categoria 3: Não idosos com convênio
cat4 = []  # Categoria 4: Não idosos sem convênio

# Variáveis que armazenam a última senha gerada para cada categoria
ultima_sh_cat1 = 100  # Senha inicial da categoria 1
ultima_sh_cat2 = 200  # Senha inicial da categoria 2
ultima_sh_cat3 = 300  # Senha inicial da categoria 3
ultima_sh_cat4 = 400  # Senha inicial da categoria 4

# Função que verifica a idade e o convênio e adiciona a senha à categoria correta
def verificar_paciente(idade, convenio):
    global ultima_sh_cat1, ultima_sh_cat2, ultima_sh_cat3, ultima_sh_cat4  # Permite modificar as variáveis globais

    # Inicializa variáveis de nova senha (não obrigatórias aqui, mas estão sendo usadas)
    nova_sh1 = 0
    nova_sh2 = 0
    nova_sh3 = 0
    nova_sh4 = 0

    # Define a categoria com base na idade e convênio
    if idade >= 65 and convenio == 1:  # Idoso com convênio → Categoria 1
        nova_sh1 = ultima_sh_cat1 + 1
        ultima_sh_cat1 = nova_sh1
        cat1.append(nova_sh1)

    elif idade >= 65 and convenio == 2:  # Idoso sem convênio → Categoria 2
        nova_sh2 = ultima_sh_cat2 + 1
        ultima_sh_cat2 = nova_sh2
        cat2.append(nova_sh2)

    elif idade < 65 and convenio == 1:  # Não idoso com convênio → Categoria 3
        nova_sh3 = ultima_sh_cat3 + 1
        ultima_sh_cat3 = nova_sh3
        cat3.append(nova_sh3)

    elif idade < 65 and convenio == 2:  # Não idoso sem convênio → Categoria 4
        nova_sh4 = ultima_sh_cat4 + 1
        ultima_sh_cat4 = nova_sh4
        cat4.append(nova_sh4)

# Início do loop para cadastrar vários pacientes
while True:
    print("\n---Cadatro de senhas---\n")
    idade = int(input("Digite a idade do paciente:"))

    # Se a idade for negativa, encerra o cadastro
    if idade < 0:
        print("\n---Idade inválida---\n---Encerrando o programa---")
        break

    # Coleta a informação do convênio
    print("\n---Convênio---\n---Digite 1=Sim ou 2=Não---\n")
    convenio = int(input("Digite se o paciente tem ou nâo convênio:"))

    # Se o valor do convênio for inválido, emite aviso e não executa o cadastro
    if convenio not in [1, 2]:
        print("\n---Convênio Invalido---\n---Tente novamente---")
    
    # Chama a função para classificar o paciente e adicionar a senha
    verificar_paciente(idade, convenio)

    # Mostra as senhas cadastradas até o momento
    print("\n---Senhas cadastradas---\n")
    print("Categoria 1 (Idosos que possuem convênio):", cat1)
    print("Categoria 2 (Idosos que não possuem convênio):", cat2)
    print("Categoria 3 (Não idosos que possuem convênio):", cat3)
    print("Categoria 4 (Não idosos que não possuem convênio):", cat4)

# Após sair do laço de cadastro, mostra mensagem de início do atendimento
print("\n--- Início do atendimento ---\n")

# Enquanto qualquer uma das listas ainda tiver pacientes
while cat1 or cat2 or cat3 or cat4:

    # Atender Categoria 1
    while cat1:
        senha = cat1.pop(0)
        print(f"Atendendo senha da Categoria 1: {senha}")
        print("---")

    # Atender Categoria 2
    while cat2:
        senha = cat2.pop(0)
        print(f"Atendendo senha da Categoria 2: {senha}")
        print("---")

    # Atender Categoria 3
    while cat3:
        senha = cat3.pop(0)
        print(f"Atendendo senha da Categoria 3: {senha}")
        print("---")

    # Atender Categoria 4
    while cat4:
        senha = cat4.pop(0)
        print(f"Atendendo senha da Categoria 4: {senha}")
        print("---")

print("\n--- Fim do programa ---")



    