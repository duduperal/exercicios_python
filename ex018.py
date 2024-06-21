from math import cos, sin, tan, radians
ang = int(input("Digite um ângulo: "))
seno = sin(radians(ang))
cose = cos(radians(ang))
tan = tan(radians(ang))

print("O ângulo {:.2f} tem como SENO {:.2f}\n"
      "O ângulo {:.2f} tem como COSSENO {:.2f}\n"
      "O ângulo {:.2f} tem como TANGENTE {:.2f}\n".format(ang, seno, ang, cose, ang, tan))