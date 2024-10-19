# Importando a biblioteca openAI -> no terminal = pip install openai
import openai

# Chave gerada no openai.com
api_key = "Sua API vem aqui!"

# Declarando a api_key da openAi como nossa api_key
openai.api_key = api_key

# Função para iniciar conversa com chatGPT e declarando uma lista (apenas declarando)
def enviar_conversa(mensagem, Lista_mensagens=[]):
    
    # Armazena todas as nossas conversas
    # append -> inserir conteúdo dentro de uma lista
    Lista_mensagens.append(
        {"role":"user", "content": mensagem}
        )
    
    # variável resposta
    # resposta dada pelo chatGPT será armazenada na lista
    resposta = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages= Lista_mensagens,
    )
    
    # Obtém apenas o conteúdo
    # Message.content -> traz apenas a resposta que o chatGPT devolve (documentação chatGPT)
    return resposta.choices[0].message.content

# lista de mensagens criada como vazia
lista_mensagens = []
while True:
    texto = input("Digite sua mensagem:")
    
    # quando o usuário digitar sair, abandona o chatbot
    if texto == "sair":
        break
    else:
        # caso contrário, obtém as respostas do chatGPT
        resposta = enviar_conversa(texto, lista_mensagens)
        # Cria um histórico das conversas
        lista_mensagens.append({'role': 'user', 'content': resposta})
        print("Chatbot:", resposta)