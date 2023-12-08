import random
import matplotlib.pyplot as plt


def look(valores, cabeca_atual):
    percurso_total = 0
    movimentos = [cabeca_atual]

    # cria uma lista dos valores ≥ 500 e outra com o resto
    blocos_superiores = [dado for dado in valores if dado >= cabeca_atual]
    blocos_inferiores = [dado for dado in valores if dado < cabeca_atual]

    for bloco in sorted(blocos_superiores):
        percurso_total += abs(cabeca_atual - bloco)
        cabeca_atual = bloco
        movimentos.append(cabeca_atual)

    for bloco in sorted(blocos_inferiores, reverse=True):
        percurso_total += abs(cabeca_atual - bloco)
        cabeca_atual = bloco
        movimentos.append(cabeca_atual)

    return percurso_total, movimentos


def c_look(valores, cabeca_atual):
    percurso_total = 0
    movimentos = [cabeca_atual]

    # cria uma lista dos valores ≥ 500 e outra com o resto
    blocos_superiores = [dado for dado in valores if dado >= cabeca_atual]
    blocos_inferiores = [dado for dado in valores if dado < cabeca_atual]

    for bloco in sorted(blocos_superiores):
        percurso_total += abs(cabeca_atual - bloco)
        cabeca_atual = bloco
        movimentos.append(cabeca_atual)

    for bloco in sorted(blocos_inferiores):
        percurso_total += abs(cabeca_atual - bloco)
        cabeca_atual = bloco
        movimentos.append(cabeca_atual)

    return percurso_total, movimentos


# gerar 10 números aleatórios
pedidos = random.sample(range(1000), 10)
cabeca_inicial = 500

# chama as funções
look_resultado, look_movimentos = look(pedidos, cabeca_inicial)
c_look_resultado, c_look_movimentos = c_look(pedidos, cabeca_inicial)

# resultados finais
print(f'Pedidos gerados: {pedidos}')
print(f'LOOK - Deslocamento total: {look_resultado}')
print(f'C-LOOK - Deslocamento total: {c_look_resultado}')

# continuação
input('\nPressione ENTER para gerar o gráfico: ')

# criação do gráfico
plt.plot(look_movimentos, label='Look', marker='o', color='green')
for i, txt in enumerate(look_movimentos):
    plt.annotate(txt, (i, txt), textcoords="offset points", xytext=(0, 5), ha='center')

plt.plot(c_look_movimentos, label='C-Look', marker='x', color='red')
for i, txt in enumerate(c_look_movimentos):
    plt.annotate(txt, (i, txt), textcoords="offset points", xytext=(0, 5), ha='center')

# rótulos
plt.title(f'Comparação entre LOOK ({look_resultado} blocos) e C-LOOK ({c_look_resultado} blocos)'
          f'\nPedidos: {list(pedidos)}')
plt.xlabel('Valores (índice)')
plt.ylabel('Blocos')
plt.legend()
plt.show()
