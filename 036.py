from random import choice

def jogo_pedra_papel_tesoura(escolha_jogador):
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha_computador = choice(escolhas)

    print(f'Você escolheu: {escolha_jogador}')
    print(f'O computador escolheu: {escolha_computador}')

    if escolha_jogador == escolha_computador:
        return 'Empate!'
    elif (  
        (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or
        (escolha_jogador == 'papel' and escolha_computador == 'pedra') or
        (escolha_jogador == 'tesoura' and escolha_computador == 'papel')
    ):
        return 'Você venceu!'
    else:
        return 'Você perdeu!'
def menu():

    # Solicitar escolha do jogador
    escolha_usuario = input('Escolha pedra, papel ou tesoura: ').lower()

    # Verificar se a escolha do jogador é válida
    if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
        print('Escolha inválida. Por favor, escolha pedra, papel ou tesoura.')
    else:
        # Executar o jogo e imprimir o resultado
        resultado = jogo_pedra_papel_tesoura(escolha_usuario)
        print(resultado)
while True:
    menu()
