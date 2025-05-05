largura = float(input("coloque a largura da parede: "))
altura = float(input("coloque a altura da parede: "))
area = largura * altura
tinta = area / 2
print("sua parede tem a dimensão de {} x {} e sua área é de {:.2f}M².".format(largura, altura, area))
print("Para pintar a parede, você precisará de {:.2f}L de tinta.".format(tinta))
