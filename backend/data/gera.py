import pandas as pd
import random

produtivo_templates = [
    "Preciso de ajuda para {acao}.",
    "Estou com dificuldade para {acao}, poderiam me orientar?",
    "Gostaria de abrir um chamado de suporte para {acao}.",
    "Meu sistema apresentou um problema ao {acao}. Preciso de assistência.",
    "Poderiam me auxiliar a {acao}?",
    "Não consigo {acao}. Solicito suporte urgente.",
    "Estou enfrentando dificuldades para {acao}, alguém pode me ajudar?"
]

improdutivo_templates = [
    "Muito obrigado pela atenção.",
    "Feliz aniversário e parabéns pelo excelente trabalho!",
    "Agradeço pelo ótimo serviço prestado.",
    "Desejo um excelente fim de semana a toda a equipe!",
    "Parabéns pelo trabalho de todos, está cada vez melhor!",
    "Agradeço pela paciência e suporte fornecidos.",
    "Obrigado por todo o apoio até agora!"
]

acoes = [
    "acessar o sistema", "emitir relatório", "resetar minha senha",
    "instalar o aplicativo", "gerar relatórios", "atualizar meus dados",
    "recuperar minha conta", "consertar erro no login", "configurar a impressora"
]

def generate_emails(n_produtivo=1000, n_improdutivo=1000):
    emails = []
    labels = []

    for _ in range(n_produtivo):
        template = random.choice(produtivo_templates)
        acao = random.choice(acoes)
        email = template.format(acao=acao)
        emails.append(email)
        labels.append("Produtivo")

    for _ in range(n_improdutivo):
        template = random.choice(improdutivo_templates)
        emails.append(template)
        labels.append("Improdutivo")

    combined = list(zip(emails, labels))
    random.shuffle(combined)
    emails, labels = zip(*combined)

    df = pd.DataFrame({
        "email": emails,
        "label": labels
    })

    return df

df = generate_emails(1200, 1200)

df.to_csv("emails_dataset.csv", index=False, encoding="utf-8")
print("Dataset gerado e salvo em emails_dataset.csv")
