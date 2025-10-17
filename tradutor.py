from deep_translator import GoogleTranslator, MyMemoryTranslator, LingueeTranslator

def chatbot():
    print("Ola! Sou um chatbot de")
    while True:
        texto = input("\nDigite io texto para traduzir:")
        if texto.lower() == "sair":
            print("Ate logo!")
            break 
        idioma_destino = input("Para qual edioma voce quer traduzir (ex: en, es, pt, de)")
        try:
            traduçao = GoogleTranslator(source='auto', traget=idioma_destino).translate(texto)
            translated = MyMemoryTranslator(source='portuguese', target="english").translate(texto)
            translated_word = LingueeTranslator(source='portuguese', target="english"). translate(texto)
            print(f"traduçao:{traduçao}")
            print(f"traduçao 2: {translated}")
            print(f"traduçao 3: {translated_word}")
        except Exception as e:
            print(f"Erro na traduçao: {e}")    

        chatbot()    