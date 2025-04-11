import random

respostas_por_categoria = {
    "pedido": [
        "Seu pedido está a caminho... ou pelo menos a gente espera! 🚚",
        "Pedido enviado! Se não chegar, a culpa é do universo. 🪐"
    ],
    "valores": [
        "Dinheiro é coisa séria... mas esse valor aí tá comédia. 💸",
        "O sistema errou o valor. Vamos corrigir isso já! 💰"
    ],
    "transacao": [
        "Transação em andamento... tipo fila de banco. 🏦",
        "Aguenta aí que já já o pagamento vai! 💳"
    ],
    "outros": [
        "Essa aí me pegou desprevenido, mas vou dar um jeito! 🤔",
        "Hmm... não entendi muito bem, mas tô aqui pra ajudar! 😅"
    ]
}

def gerar_resposta(categoria):
    if categoria in respostas_por_categoria:
        return random.choice(respostas_por_categoria[categoria])
    return random.choice(respostas_por_categoria["outros"])
