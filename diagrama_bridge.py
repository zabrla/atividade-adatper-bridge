from abc import ABC, abstractmethod

class Renderizador(ABC):
    
    @abstractmethod
    def desenhar_forma(self, nome_forma: str, dimensoes: str) -> str:
        pass

class RenderizadorVetor(Renderizador):
    def desenhar_forma(self, nome_forma: str, dimensoes: str) -> str:
        return f"A desenhar {nome_forma} em VETOR (alta precisão) com {dimensoes}."


class RenderizadorPixel(Renderizador):
    def desenhar_forma(self, nome_forma: str, dimensoes: str) -> str:
        return f"A desenhar {nome_forma} em PÍXEIS (rasterização) com {dimensoes}."

class Forma(ABC):

    def __init__(self, renderizador: Renderizador):
        self._renderizador = renderizador

    @abstractmethod
    def desenhar(self) -> str:
        pass

class Circulo(Forma):
    def __init__(self, renderizador: Renderizador, raio: float):
        super().__init__(renderizador)
        self.raio = raio

    def desenhar(self) -> str:
        dimensoes = f"raio de {self.raio} unidades"
        return self._renderizador.desenhar_forma("Círculo", dimensoes)


class Quadrado(Forma):
    def __init__(self, renderizador: Renderizador, lado: float):
        super().__init__(renderizador)
        self.lado = lado

    def desenhar(self) -> str:
        dimensoes = f"lados de {self.lado} unidades"
        return self._renderizador.desenhar_forma("Quadrado", dimensoes)

# testes

if __name__ == "__main__":
    renderizador_vetor = RenderizadorVetor()
    renderizador_pixel = RenderizadorPixel()

    circulo_vetorial = Circulo(renderizador_vetor, 5.0)
    circulo_pixelizado = Circulo(renderizador_pixel, 5.0)

    quadrado_vetorial = Quadrado(renderizador_vetor, 10.0)
    quadrado_pixelizado = Quadrado(renderizador_pixel, 10.0)

    print("--- Renderização Vetorial ---")
    print(circulo_vetorial.desenhar())
    print(quadrado_vetorial.desenhar())
    
    print("\n--- Renderização por Píxeis ---")
    print(circulo_pixelizado.desenhar())
    print(quadrado_pixelizado.desenhar())
