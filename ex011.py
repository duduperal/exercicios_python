lp = float(input("Largura da parede: "))
ap = float(input("Altura da parede: "))
area = lp * ap
tinta = area / 2
print("Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.3f}m²".format(lp, ap, area))
print("Para pintar essa parede, você precisará de {:.1f}l de tinta".format(tinta))