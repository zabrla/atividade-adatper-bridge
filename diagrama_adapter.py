from abc import ABC, abstractmethod

# interfaces

class ReprodutorMidia(ABC):
    @abstractmethod
    def reproduzir(self, tipo_audio: str, nome_arquivo: str):
        pass


class ReprodutorAvancado(ABC):
    @abstractmethod
    def reproduzir_vlc(self, nome_arquivo: str):
        pass

    @abstractmethod
    def reproduzir_mp4(self, nome_arquivo: str):
        pass

class ReprodutorVLC(ReprodutorAvancado):
    def reproduzir_vlc(self, nome_arquivo: str):
        print(f"Reproduzindo arquivo VLC: {nome_arquivo}")

    def reproduzir_mp4(self, nome_arquivo: str):
        pass


class ReprodutorMP4(ReprodutorAvancado):
    def reproduzir_vlc(self, nome_arquivo: str):
        pass

    def reproduzir_mp4(self, nome_arquivo: str):
        print(f"Reproduzindo arquivo MP4: {nome_arquivo}")

# adapter

class AdaptadorMidia(ReprodutorMidia):

    def __init__(self, tipo_audio: str):
        self.reprodutor_avancado = None

        if tipo_audio.lower() == 'vlc':
            self.reprodutor_avancado = ReprodutorVLC()
        elif tipo_audio.lower() == 'mp4':
            self.reprodutor_avancado = ReprodutorMP4()

    def reproduzir(self, tipo_audio: str, nome_arquivo: str):
        if tipo_audio.lower() == 'vlc':
            self.reprodutor_avancado.reproduzir_vlc(nome_arquivo)
        elif tipo_audio.lower() == 'mp4':
            self.reprodutor_avancado.reproduzir_mp4(nome_arquivo)

class ReprodutorAudio(ReprodutorMidia):

    def reproduzir(self, tipo_audio: str, nome_arquivo: str):
        tipo = tipo_audio.lower()
        
        if tipo == 'mp3':
            print(f"Reproduzindo arquivo MP3 nativamente: {nome_arquivo}")
        
        elif tipo in ['vlc', 'mp4']:
            adaptador = AdaptadorMidia(tipo)
            adaptador.reproduzir(tipo, nome_arquivo)
            
        else:
            print(f"Erro: Formato '{tipo_audio}' não é suportado.")

class Principal:
    @staticmethod
    def executar():
        reprodutor = ReprodutorAudio()
        
        print("--- Iniciando o Reprodutor de Músicas ---")
        
        # teste padrao
        reprodutor.reproduzir("mp3", "musica_tema_cain_rpg.mp3")
        
        # teste adapter
        reprodutor.reproduzir("mp4", "gameplay_bg3.mp4")
        reprodutor.reproduzir("vlc", "tutorial_django.vlc")
        
        # teste erro
        reprodutor.reproduzir("avi", "video_antigo.avi")


if __name__ == "__main__":
    Principal.executar()