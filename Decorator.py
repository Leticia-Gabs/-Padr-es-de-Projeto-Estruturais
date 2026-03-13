# Interface/Base do Componente
class Cafe:
    def get_descricao(self):
        return "Café Simples"

    def get_preco(self):
        return 5.0


# Decorador Base
class CafeDecorator(Cafe):
    def __init__(self, cafe_decorado):
        self.cafe_decorado = cafe_decorado

    def get_descricao(self):
        return self.cafe_decorado.get_descricao()

    def get_preco(self):
        return self.cafe_decorado.get_preco()


# Decorador Concreto 1: Leite
class ComLeite(CafeDecorator):
    def get_descricao(self):
        return self.cafe_decorado.get_descricao() + ", com Leite"

    def get_preco(self):
        return self.cafe_decorado.get_preco() + 2.0


# Decorador Concreto 2: Caramelo
class ComCaramelo(CafeDecorator):
    def get_descricao(self):
        return self.cafe_decorado.get_descricao() + ", com Caramelo"

    def get_preco(self):
        return self.cafe_decorado.get_preco() + 1.5


# Código do Cliente
if __name__ == "__main__":
    
    # Pedido 1: Café simples
    meu_cafe = Cafe()
    print(f"Pedido: {meu_cafe.get_descricao()} | Preço: R${meu_cafe.get_preco()}")

    # Pedido 2: Café com leite e caramelo (Encadeando decoradores)
    cafe_especial = Cafe()
    cafe_especial = ComLeite(cafe_especial)
    cafe_especial = ComCaramelo(cafe_especial)

    print(f"Pedido: {cafe_especial.get_descricao()} | Preço: R${cafe_especial.get_preco()}")
