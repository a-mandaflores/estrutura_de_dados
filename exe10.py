#Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
#programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
#computador e determinar o vencedor.
import random as rd

escolha = input('Escolha entre Pedra, Papel e Tesoura\n1 - Pedra\n2- Papel\n3 - Tesoura')
if escolha == '1':
    escolha = 'Pedra'
elif escolha == '2':
    escolha = 'Papel'
else: escolha = 'Tesoura'

computador = ['Pedra', 'Papel', 'Tesoura']
resultado = rd.choice(computador)


if escolha == resultado:
    print(f'Empatou, você e o computador escolheram {escolha}')
elif escolha == 'Pedra' and resultado == 'Tesoura':
    print(f'Você ganho. Você escolheu {escolha} e o pc escolheu {resultado}')
elif escolha == 'Papel' and resultado == 'Pedra':
    print(f'Você ganho. Você escolheu {escolha} e o pc escolheu {resultado}')
elif escolha == 'Tesoura' and resultado == 'Papel':
    print(f'Você ganho. Você escolheu {escolha} e o pc escolheu {resultado}')
else: print(f'Você perdeu. Você escolheu {escolha} e o pc escolheu {resultado}')


