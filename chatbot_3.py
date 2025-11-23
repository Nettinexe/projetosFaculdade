import nltk
import random

# Inicialização do nltk (caso seja a primeira vez que está usando)
nltk.download('punkt')

# Lista de respostas gerais para o chatbot
respostas_iniciais = [
    "Olá! Bem-vindo à nossa loja de carros de luxo. Como posso ajudar você hoje?",
    "Olá! Em que posso ajudar você a encontrar o carro dos seus sonhos?",
    "Oi, sou o assistente virtual da nossa loja de carros de luxo. Em que posso te ajudar?"
]

# Respostas sobre as condições do cliente
respostas_condicao_aceita = [
    "Ótimo! Você escolheu a opção de condições especiais. Vamos ver as opções de carros!",
    "Perfeito! Agora, com as condições especiais, você terá acesso a carros exclusivos.",
    "Muito bem! Com as condições especiais, vamos começar a mostrar as opções de carros para você."
]

respostas_condicao_recusada = [
    "Entendi, você preferiu não aceitar as condições especiais. Vamos ver as opções padrão então.",
    "Sem problemas! Mesmo sem as condições especiais, temos excelentes opções para você.",
    "Tudo bem! Agora vamos ver as opções de carros sem condições especiais."
]

# Respostas sobre modelos de carros
modelos_carros = [
    "Mercedes-Benz S-Class",
    "BMW Série 7",
    "Porsche 911",
    "Audi R8",
    "Lamborghini Huracán"
]

# Função para exibir respostas iniciais
def saudacao_inicial():
    return random.choice(respostas_iniciais)

# Função para perguntar sobre as condições especiais
def perguntar_condicao():
    return "Você gostaria de aproveitar nossas condições especiais de financiamento? (Sim/Não)"

# Função para exibir opções de carros com base na escolha do cliente
def mostrar_opcoes_carros(condicao_aceita):
    if condicao_aceita:
        resposta = random.choice(respostas_condicao_aceita)
    else:
        resposta = random.choice(respostas_condicao_recusada)
    
    carros = "\n".join([f"- {modelo}" for modelo in modelos_carros])
    return f"{resposta}\nAqui estão algumas opções de carros disponíveis:\n{carros}"

# Função principal do chatbot
def chatbot():
    print(saudacao_inicial())
    
    while True:
        resposta_usuario = input("\nVocê: ").strip().lower()
        
        if 'sim' in resposta_usuario:
            print("\nChatbot: Perfeito! Vamos mostrar as opções com condições especiais.")
            print(mostrar_opcoes_carros(True))
        elif 'não' in resposta_usuario:
            print("\nChatbot: Tudo bem, vamos mostrar as opções sem condições especiais.")
            print(mostrar_opcoes_carros(False))
        else:
            print("\nChatbot: Desculpe, não entendi. Por favor, responda com 'Sim' ou 'Não'.")
        
        continuar = input("\nChatbot: Gostaria de ver mais opções? (Sim/Não): ").strip().lower()
        if 'não' in continuar:
            print("\nChatbot: Obrigado por conversar conosco. Até logo!")
            break

# Chamada para o chatbot
chatbot()