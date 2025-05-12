from ValidadorTriangulo import ValidadorTriangulo

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.l1 = lado1
        self.l2 = lado2
        self.l3 = lado3

    def tipo(self):
        if not ValidadorTriangulo.valida_triangulo(self.l1, self.l2, self.l3):
            return "Os lados não formam um triângulo."
        if self.l1 == self.l2 == self.l3:
            return "Triângulo EQUILÁTERO"
        elif self.l1 == self.l2 or self.l1 == self.l3 or self.l2 == self.l3:
            return "Triângulo ISÓSCELES"
        else:
            return "Triângulo ESCALENO"
