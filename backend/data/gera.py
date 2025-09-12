import pandas as pd
import random

respostas_produtivo_templates = [
    "Olá! Entendi sua solicitação sobre {acao}. Nossa equipe irá analisar e retornar em breve.",
    "Obrigado por entrar em contato. Para {acao}, siga os passos descritos no manual ou aguarde que iremos lhe auxiliar.",
    "Recebemos seu chamado sobre {acao}. Estamos verificando e entraremos em contato em seguida.",
    "Agradecemos o aviso. Nossa equipe de suporte já está ciente do problema ao {acao}.",
    "Claro! Para {acao}, por favor, verifique se há mensagens de erro na tela e nos envie uma captura, assim podemos ajudar melhor.",
    "Estamos à disposição. Assim que tivermos mais informações sobre {acao}, retornaremos seu contato."
]

respostas_produtivo_genericas = [
    "Obrigado pelo seu contato, nossa equipe está analisando sua solicitação.",
    "Recebemos sua mensagem e em breve retornaremos com mais informações.",
    "Sua solicitação foi registrada, vamos verificar e entraremos em contato.",
    "Estamos avaliando seu pedido, obrigado pela paciência.",
    "Sua mensagem foi recebida, nosso time de suporte irá lhe auxiliar."
]

respostas_improdutivo_templates = [
    "Nós que agradecemos pela sua mensagem. Desejamos um excelente dia!",
    "Muito obrigado pelas palavras, ficamos felizes com seu reconhecimento.",
    "Agradecemos a gentileza, seguimos à disposição.",
    "Desejamos também um ótimo fim de semana para você!",
    "Ficamos felizes com seu feedback positivo, muito obrigado!"
]

acoes = [
    "acessar o sistema", "emitir relatório", "resetar sua senha",
    "instalar o aplicativo", "gerar relatórios", "atualizar seus dados",
    "recuperar sua conta", "consertar erro no login", "configurar a impressora"
]

def generate_email_responses(n_produtivo=1000, n_improdutivo=1000):
    emails = []
    respostas = []

    for _ in range(n_produtivo):
        acao = random.choice(acoes)

        if random.random() < 0.7:  
            resposta = random.choice(respostas_produtivo_templates).format(acao=acao)
            email = f"Preciso de ajuda para {acao}."
        else:
            resposta = random.choice(respostas_produtivo_genericas)
            email = f"Estou enfrentando um problema no sistema, podem me ajudar?"

        emails.append(email)
        respostas.append(resposta)

    improdutivo_emails = [
        "Muito obrigado pela atenção.",
        "Feliz aniversário e parabéns pelo excelente trabalho!",
        "Agradeço pelo ótimo serviço prestado.",
        "Desejo um excelente fim de semana a toda a equipe!",
        "Parabéns pelo trabalho de todos, está cada vez melhor!",
        "Agradeço pela paciência e suporte fornecidos.",
        "Obrigado por todo o apoio até agora!"
    ]

    for _ in range(n_improdutivo):
        email = random.choice(improdutivo_emails)
        resposta = random.choice(respostas_improdutivo_templates)
        emails.append(email)
        respostas.append(resposta)

    combined = list(zip(emails, respostas))
    random.shuffle(combined)
    emails, respostas = zip(*combined)

    df = pd.DataFrame({
        "email": emails,
        "resposta": respostas
    })

    return df


df = generate_email_responses(1000, 1000)
df.to_csv("emails_respostas_dataset.csv", index=False, encoding="utf-8")
print("Dataset de respostas gerado e salvo em emails_respostas_dataset.csv")
