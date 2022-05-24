import random
import time
from Pokemons import pokemons_disponiveis

rolar_dados: 0
ação_inimigo: 0
pokemon_inimigo = 'Charizard'

print('Pokemons Disponíveis:''\nBlastoise - Easy''\nRaichu - Medium''\nVenosaur - Hard')
pokemon_escolhido = (input('\nDigite o nome do seu Pokemon escolhido: ')).capitalize()

while True:
    if pokemon_escolhido == 'Blastoise' or pokemon_escolhido == 'Venosaur' or pokemon_escolhido == 'Raichu':
        break
    else:
        print('Você não escolheu um nome de Pokemon válido, digite novamente ou digite sair para finalizar o jogo: ')
        pokemon_escolhido = (input('Digite o nome do seu Pokemon escolhido: ')).capitalize()
        if pokemon_escolhido == 'Sair':
            break

vida = pokemons_disponiveis[pokemon_escolhido]['vida']
ataque = pokemons_disponiveis[pokemon_escolhido]['ataque']
defesa = pokemons_disponiveis[pokemon_escolhido]['defesa']
vida_inimigo = pokemons_disponiveis[pokemon_inimigo]['vida']
ataque_inimigo = pokemons_disponiveis[pokemon_inimigo]['ataque']
defesa_inimigo = pokemons_disponiveis[pokemon_inimigo]['defesa']

print(f'Seu pokemon escolhido foi: {pokemon_escolhido}'
      f'\nSua vida é de {vida}'
      f'\nSeu ataque é de {ataque}'
      f'\nSua defesa é de {defesa}')

print('\nA wild Charizard appears!!!')

print(f'\nSeu inimigo é um Charizard!'
      f'\nSua vida é de {vida_inimigo}'
      f'\nSeu ataque é de {ataque_inimigo}'
      f'\nSua defesa é de {defesa_inimigo}')

while True:
    ação = (input('\nDeseja atacar ou defender ou sair? [atk/def/sair]')).capitalize()
    if ação == 'Atk':
        rolar_dados = random.randint(0, 100)
        if rolar_dados >= 90:
            vida_inimigo = vida_inimigo - (ataque*2)
            print(f'CRITICAL HIT! Vida do Charizard: {vida_inimigo}')
        elif rolar_dados >= 20:
            vida_inimigo = vida_inimigo - ataque
            print(f'Acertou! Vida do Charizard: {vida_inimigo}')
        else:
            print(f'Errou seu ataque. Vida do Charizard: {vida_inimigo}')
    elif ação == 'Def':
        vida += defesa
        print(f'{pokemon_escolhido} se curou em: {defesa} pontos! Sua vida é de: {vida}')
    elif ação == 'Sair':
        print('Jogo finalizado.')
        break
    else:
        print('Não escolheu uma opção válida, perdeu o turno...')

    if vida <= 0:
        print(f'O vencedor foi: Charizard!')
        break
    elif vida_inimigo <= 0:
        print(f'O vencedor foi {pokemon_escolhido}!')
        break

    ação_inimigo = random.randint(1, 10)
    print('\nCharizard está pensando no que fazer...')
    time.sleep(3)
    if ação_inimigo <= 7:
        rolar_dados = random.randint(0, 100)
        if rolar_dados >= 90:
            vida = vida - (ataque_inimigo * 2)
            print(f'CRITICAL HIT! A vida do {pokemon_escolhido}: {vida}')
        elif rolar_dados >= 20:
            vida = vida - ataque_inimigo
            print(f'Charizard acertou! A vida do {pokemon_escolhido}: {vida}')
        else:
            print(f'Charizard errou seu ataque. A vida do {pokemon_escolhido}: {vida}')
    elif ação_inimigo >= 8:
        vida_inimigo += defesa_inimigo
        print(f'Charizard se curou em {defesa_inimigo} pontos! Sua vida é de: {vida_inimigo}')

    if vida <= 0:
        print(f'\nO vencedor foi: Charizard!')
        break
    elif vida_inimigo <= 0:
        print(f'\nO vencedor foi {pokemon_escolhido}!')
        break
