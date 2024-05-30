# TRABALHO FEITO POR WAGNER SEGALA (1136704) E RAFAEL BOFF (1136392)
from funcoes import aguarde, limparTela
def jogar ():
    print("Iniciando...")
    aguarde(2)
    print(''' 
      _____                                                           
_/ ____\___________   ____ _____       _________    _____   ____  
\   __\/  _ \_  __ \_/ ___\\__  \     / ___\__  \  /     \_/ __ \ 
 |  | (  <_> )  | \/\  \___ / __ \_  / /_/  > __ \|  Y Y  \  ___/ 
 |__|  \____/|__|    \___  >____  /  \___  (____  /__|_|  /\___  >
                         \/     \/  /_____/     \/      \/     \/ ''')
    aguarde(2)
    limparTela()
    nomeDesafiante = input("Nome do desafiante: ")
    nomeCompetidor = input("Nome do Competidor: ")
    print ('Bem vindos', nomeDesafiante, 'e', nomeCompetidor, 'ao jogo da forca!' )
    aguarde (4)
    limparTela()
                     
    palavraChave = input(F'Ao desafiante {nomeDesafiante} que digite a palavra chave: ').upper()
    dica1 = input(F'Ao desafiante {nomeDesafiante} que digite a primeira dica: ')
    dica2 = input(F'Ao desafiante {nomeDesafiante} que digite a segunda dica: ')
    dica3 = input(F'Ao desafiante {nomeDesafiante} que digite a terceira dica: ')
    aguarde (2)
    limparTela()

    palavraEscondida = ['*' for _ in palavraChave]
    erros = 0
    dicas_usadas = 0 

    while '*' in palavraEscondida and erros < 6:
        print('A Palavra é:', ''.join(palavraEscondida))
        print(f'Digite 0 para jogar ou 1, 2, 3 para as respectivas dicas (Você ainda pode usar {3 - dicas_usadas} dicas):')
        opcao = input()

        if opcao in ['1', '2', '3'] and dicas_usadas < 3:
            if opcao == '1' and dica1:
                print('A primeira dica é:', dica1)
                dica1 = None  
            elif opcao == '2' and dica2:
                print('A segunda dica é:', dica2)
                dica2 = None
            elif opcao == '3' and dica3:
                print('A terceira dica é:', dica3)
                dica3 = None
            dicas_usadas += 1
            aguarde(2)
            print("Agora você deve arriscar uma letra.")
            letra = input("Digite uma letra: ").upper()
            if letra in palavraChave:
                for i in range(len(palavraChave)):
                    if palavraChave[i] == letra:
                        palavraEscondida[i] = letra
            else:
                erros += 1
                print(f'Erro: {erros}')
            aguarde(1)
        elif opcao == '0':
            letra = input("Digite uma letra: ").upper()
            if letra in palavraChave:
                for i in range(len(palavraChave)):
                    if palavraChave[i] == letra:
                        palavraEscondida[i] = letra
            else:
                erros += 1
                print(f'Erro: {erros}')
            aguarde(1)
        limparTela()

    if '*' not in palavraEscondida:
        print("Parabéns! Você descobriu a palavra:", ''.join(palavraEscondida))
    else:
        print("Que pena! Você não descobriu a palavra. Era:", palavraChave)
    aguarde(3)
    limparTela()

def repetir():
    while True:
        jogar()
        print('Você chegou ao fim do jogo')
        print('Digite 0 para sair')
        print('Digite 1 para jogar novamente')
        escolha = input()
        limparTela ()
        if escolha == '0':
            break

repetir()