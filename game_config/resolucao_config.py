from pygame import display

# Essa classe se dedica a configurar a resolucao do jogo

class ResolucaoConfig(object):
    def __init__(self) -> None:
        
        self.largura_janela, self.altura_janela = 1280, 720 # Largura  e altura de Incializacao do jogo

        # Cria-se a estrutura necessária para gerar uma janela do tamanho x ( especifico do pygames )
        self.display_proporcao_janela = display.set_mode((self.largura_janela, self.altura_janela))

        self.dicionario_de_resolucoes = {
            'user_set':'',
            '240p':'426x240',
            '360p':'640x360',
            '480p':'854x480',
            '720p':'1280x720',
            '1080p':'1920x1080',
            '1440p':'2560x1440',
            '2160p':'3840x2160'
        }

    def get_pygame_display(self):
        return self.display_proporcao_janela

    def calcular_imagem_x_resolucao(self, proporcao: tuple):
        largura = proporcao[0]
        altura = proporcao[1]

        if largura - altura > 0:
            razao_de_proporcao = ( self.altura_janela / altura )
            largura = largura * razao_de_proporcao
            altura = altura * razao_de_proporcao
            return (largura, altura)
        else:
            razao_de_proporcao = ( self.largura_janela / largura )
            largura = largura * razao_de_proporcao
            altura = altura * razao_de_proporcao
            return (largura, altura)

    def get_resolucoes_possiveis(self):
        return self.dicionario_de_resolucoes

    def get_proporcoes_para_resolucao(self, dict_chave):
        valor = self.dicionario_de_resolucoes[dict_chave]
        achouX = False
        for i in valor:
            if i == 'x':
                achouX = True
                continue
            if achouX:
                altura += i
            else:
                largura += i

        return (largura, altura)

    def set_resolucao_jogo(self, largura, altura):
        pass

    def get_eixos_centrais(self, proporcao: tuple):
        centro_x = proporcao[0]/2
        centro_y = proporcao[1]/2

        centro_x_janela = self.largura_janela/2
        centro_y_janela =self.altura_janela/2

        eixo_x = centro_x_janela - centro_x
        eixo_y = centro_y_janela - centro_y
        return (eixo_x, eixo_y)