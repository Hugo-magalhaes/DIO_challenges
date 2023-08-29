
# import json
# ! Só pode usar se pagar um dólar

import openai
import pandas as pd
import requests

# Extract

df = pd.read_csv(r'C:/Users/Hugo Martins/Downloads/Usuários - Página1.csv')

users_id = df['User ID'].tolist()
# print(users_id)

# Load

api_url = 'https://sdw-2023-prd.up.railway.app'


def get_user(id_):
    reponse = requests.get(f'{api_url}/users/{id_}')
    return reponse.json() if reponse.status_code == 200 else None


users = [user for id in users_id if (user := get_user(id)) is not None]
# print(json.dumps(users, indent=2))


openai.api_key = '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'


def generate_reponses(user):
    completion = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {
                'role': 'system',
                'content': 'Você é um especialista em sistema bancário'
            },
            {
                'role': 'user',
                'content': f'Crie uma mensagem para {user["name"]} \
            sobre a importância da saúde financeira (máximo de 100 caracteres)'
            }
        ]
    )
    return completion.choices[0].message.contet.strip('\"')  # type: ignore


def update_news_user(user, new: None | str):
    if new is not None:
        reponse = requests.put(f'{api_url}/users/{user["id"]}', json=user)
        return True if reponse.status_code == 200 else False


for user in users:
    news = generate_reponses(user)
    print(news)

    success = update_news_user(user, news)
    print(f'User {user["name"]} updated? {success}')
