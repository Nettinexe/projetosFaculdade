import random
import nltk
from nltk.chat.util import Chat, reflections
pares = [
    (r"oi|olá|opa|e aí", ["Olá!", "Oi, como posso ajudar?", "Oi! Tudo bem?"]),
    (r"qual é o seu nome\?", ["Eu sou um chatbot simples!", "Meu nome é ChatBotNLTK."]),
    (r"me diga algo em inglês",["How are you?", "Nice to meet you!", "I have big dick"]),
    (r"você um dia irá dominar o mundo\?",["Não tenho essa ideias por enquanto", "Provavelmente não", "Espero que eu não precise","Se vocês humanos continuarem emburrecendo, sim"]),
    (
        r"como você está\?|tudo bem e você\?",
        ["Estou bem, obrigado por perguntar!", "Estou sempre bem, sou um chatbot."],
    ),
    (
        r"O que você pode fazer\?",
        [
            "Eu posso responder perguntas simples",
            "Sou um chabot básico criado com NLTK.",
        ],
    ),
    (r"meu nome é (.*)", ["Olá %1, prazer em te conhecer"]),
    (r"adeus|tchau", ["Tchau! Foi bom conversar com você.", "Até mais"]),
    (r"(.*)", ["Desculpe, não entendi o que você quis dizer."]),
    ]
reflections = {
    "eu":"você",
    "meu":"você",
    "meus":"seus",
    "minha":"sua",
    "sou":"é",
    "estou":"está",
    "fui":"foi",
    "era":"era",
    "você":"eu",
    "você é":"eu sou",
    "você está":"eu estou",
}
chatbot = Chat(pares, reflections)
def iniciar_chat():
    print("Bem vindo ao ChatBot NLTK! Digite 'sair' para encerrar.")
    while True:
        entrada = input("Você: ")
        if entrada.lower() == "sair":
            print("ChatBot:Até logo!")
            break
        resposta = chatbot.respond(entrada)
        print("Chatbot:", resposta)

iniciar_chat()