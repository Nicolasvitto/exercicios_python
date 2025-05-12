class ValidadorTriangulo:
    @staticmethod
    def valida_triangulo(lado1, lado2, lado3):
        return (
            lado1 < lado2 + lado3 and
            lado2 < lado1 + lado3 and
            lado3 < lado1 + lado2
        )