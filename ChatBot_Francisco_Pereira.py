import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

#    if comando in ('olá', 'boa tarde', 'bom dia'):
#        return 'Olá tudo bem!'
#    if comando == 'como estás':
#        return 'Estou bem, obrigado!'
#    if comando == 'como te chamas?':
#        return 'O meu nome é: Bot :)'
#    if comando == 'tempo':
#        return 'Está um dia de sol!'
#    if comando in ('bye', 'adeus', 'tchau'):
#        return 'Gostei de falar contigo! Até breve...'
#    if 'horas' in comando:
#        return f'São: {datetime.now():%H:%M} horas'
#    if 'data' in comando:
#        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'
#
#    return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        ('como estás'): 'Estou bem, obrigado!',
        ('como te chamas?', 'qual é o teu nome?'): 'O meu nome é: Bot :)',
        ('que horas são?', 'horas'): f'São: {datetime.now():%H:%M} horas',
        ('que dia é hoje?', 'data'): f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        ('que dia da semana é hoje?', 'dia da semana'): f'Hoje é: {datetime.now():%A}',
        ('como está o tempo em braga?',): 'Está um dia de sol!',
        ('como está o tempo em londres?',): 'Está a chover!',
        ('qual é a capital de portugal?', 'capital de portugal'): 'A capital de Portugal é Lisboa.',
        ('qual é a capital de espanha?', 'capital de espanha'): 'A capital de Espanha é Madrid.',
        ('qual é a capital de frança?', 'capital de frança'): 'A capital de França é Paris.',
        ('qual é o teu desporto favorito?', 'desporto favorito'): 'O meu desporto favorito é o natação.',
        ('quando é o teu aniversário?', 'aniversário'): 'O meu aniversário é no dia 23 de Julho.',
        ('qual é a tua cor favorita?', 'cor favorita'): 'A minha cor favorita é roxo.',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()