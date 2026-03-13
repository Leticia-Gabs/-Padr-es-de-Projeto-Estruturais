# Subsistemas complexos (Classes que fazem o trabalho pesado)

class Luzes:
    def desligar(self):
        print("Luzes: Apagando as luzes para o filme...")


class Som:
    def ligar(self):
        print("Som: Ligando o sistema Surround 5.1...")


class Projetor:
    def ligar(self):
        print("Projetor: Iniciando transmissão em 4k...")


# A FACADE
class HomeTheaterFacade:
    def __init__(self, luzes, som, projetor):
        self.luzes = luzes
        self.som = som
        self.projetor = projetor

    def assistir_filme(self):
        print("\n--- Preparando o cinema em casa ---")
        self.luzes.desligar()
        self.som.ligar()
        self.projetor.ligar()
        print("--- Tudo pronto! Bom filme! ---\n")


# Código do Cliente
if __name__ == "__main__":
    
    # Instanciamos os subsistemas
    l = Luzes()
    s = Som()
    p = Projetor()

    # Usamos a Fachada para simplificar a vida do usuário
    home_theater = HomeTheaterFacade(l, s, p)
    home_theater.assistir_filme()
