from gpt4all import GPT4All
from pathlib import Path

# Caminho para o modelo .gguf
modelo = Path("\Projetos Programação\Python\Grandes modelos de linguagem e langchain\gptallLlama-3.2-1B-Instruct-BF16.gguf").resolve()

# Verifica se o modelo existe
if not modelo.exists():
    print(f"❌ Modelo não encontrado em: {modelo}")
    exit()

# Inicializa o modelo com GPT4All (modo CPU)
llm = GPT4All(
    model_name=modelo.name,          # Nome do arquivo do modelo
    model_path=str(modelo.parent),   # Caminho até a pasta onde o modelo está
    allow_download=False,            # Não baixa outro modelo automaticamente
    verbose=True                     # Mostra mais detalhes ao carregar
)

# Prompt base
prompt_base = (
    "Você é um assistente especializado em recomendar filmes e séries de forma simpática e direta.\n"
    "Sempre responda em português do Brasil, com no máximo 3 parágrafos.\n"
    "Faça perguntas se quiser entender melhor o gosto do usuário.\n"
)

print("🎬 CineBot iniciado com DeepSeek! Digite 'sair' para encerrar.\n")

# Loop de conversa
while True:
    pergunta = input("Você: ")
    if pergunta.strip().lower() == "sair":
        print("CineBot: Até logo!")
        break

    # Cria o prompt para o modelo com o contexto do assistente
    prompt = f"{prompt_base}Usuário: {pergunta}\nCineBot:"
    
    # Gera resposta com no máximo 300 tokens
    resposta = llm.generate(prompt=prompt, max_tokens=300)
    
    # Imprime a resposta
    print("CineBot:", resposta.strip())
