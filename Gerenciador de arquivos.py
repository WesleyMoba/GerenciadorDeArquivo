"""
Gerenciador de arquivos

Script feito 100% no terminal, utilizado para organizar diretorios, mover itens e ver arquivos
A principal função dele é organizar os arquivos pela extensoes.
Exemplo: Caso um arquivo seja EXE(executavel) ele ira criar uma pasta, que jogara este arquivo EXE,
 e todos os outros dentro deste diretorio, o codigo está abaixo.
 O script não navega por todos os arquivos do computador, apenas as principais como:
 Desktop(Area de trabalho), Downloads, Imagens, Videos, Musicas.
"""
import os
from shutil import move
from time import sleep

def criar_pasta(localdapasta):
    nome = input('Qual nome você deseja dar para a pasta')
    pasta = localdapasta + f'\\{nome}'
    if not os.path.exists(pasta): #Se nao existir nenhuma pasta com o nome dado pelo usuario
        os.makedirs(pasta) #Ai podemos criar a pasta
    else:
        print('Está pasta já existe!')

def organizar(diretorio):
    for arquivos in os.listdir(diretorio):   #Metodo de listar arquivos de um diretorio
        contador = -1
        for c in arquivos: #Iterar sobre as "Caracteres" dos arquivos do diretorio
            localArquivo = diretorio + f'\\{arquivos}' 
            lista = arquivos
            if lista[contador] == '.': #Usar o contador para descobrir o indice do ponto
                extensao = lista[contador::]
                local = diretorio + f'\\{extensao}'
                break
            else:
                contador -= 1       
        try:                        
            if not os.path.exists(local): 
                os.makedirs(local) 
        except:
            extensao = '7423YUASDUASDSAUDASUQAFA'
            pass
        if extensao in arquivos:                       #Se a extensao existe no arquivo mover o arquivo para pasta correspondete ao arquivo         
            try:#
                move(localArquivo, local)
                print('Executando')
                sleep(1)
            except:
                print('Algo deu errado.')
        else:
            pastaOutros = diretorio + f'\\pastas e outros'
            if not os.path.exists(pastaOutros):
                os.makedirs(pastaOutros)
            move(localArquivo, pastaOutros)
            pass            

def moverArquivo(localdoArquivo, voltar): #Está função não está 100% Otimizada pois tenq ser escrito o nome do arquivo por inteiro e o diretorio tbm
    print('Digite o nome do arquivo por completo, encluindo a extensao') 
    arquivoParaMover = input('Que arquivo você deseja mover?')
    if arquivoParaMover in os.listdir(localdoArquivo):
        local = localdoArquivo + f'\\{arquivoParaMover}'
        print('Arquivo encontrado')
        moverPara = input('Mover para o diretorio: \n')
        try:
            move(local, moverPara)
            print('SUCESSO! você moveu o arquivo')
        except:
            print('Algo deu errado...')
            print('Você digitou o diretorio completo?')
            print(r'EX:  C:\Usuarios\User\Desktop\Python')
            sleep(3)
            return(voltar)
    else:
        print('Arquivo nao encontrado, Retornando...')
        sleep(1)
        return(voltar)

class diretorio:    #Classe criada para ligar todas as funcionalidades e locomover entre os diretorios
    def __init__(self):
        self.nomeUsuario = input('Qual o nome do seu usuario?') #Aqui deve ser inserido o nome do usuario no computador,
        self.telaInicio()                             #Pode ser substituido direto pelo nome do usuario para nao repetir toda hora.
        self.oq_fazer()
    def telaInicio(self): 
        os.system('cls')
        self.local = f"C:\\Users\\{self.nomeUsuario}"
        print(' 1 - Area De Trabalho\n 2 - Downloads \n 3 - Documentos \n 4 - Imagens \n 5 - Musicas \n 6 - Videos ')
        onde_ir = input('Escolha a opção desejada\n')
        if onde_ir == '1':                        
            self.local = self.local + r'\desktop'
        elif onde_ir == '2':
            self.local = self.local + r'\downloads'
        elif onde_ir == '3':
            self.local = self.local + r'\documents'
        elif onde_ir == '4':                       #Adiciona o local que o usuario vai navegando pelas pasta, escolha simples usando if/else
            self.local = self.local + r'\Pictures' #Caso nenhuma a escolha nao esteja entre as opções ele volta ao menu com a funcao return
        elif onde_ir == '5':
            self.local = self.local + r'\music'
        elif onde_ir == '6':
            self.local = self.local + r'\videos'
        else:
            return(self.__init__())
    def oq_fazer(self):
        os.system('cls')
        print('1 - Ver Arquivos\n2 - Organizar\n3 - Criar Pasta\n4 - Mover arquivo\n5 - Voltar') 
        escolherOpcao = input('O que você deseja fazer\n')
        if escolherOpcao == '1':
            os.system('cls')
            for arquivos in os.listdir(self.local): #Cria um looping da lista dos arquivos de onde esta o local
                print(arquivos)
            input('\n\n    Deseja voltar?')
            if input:                   #Voltar ao menu usando uma forma simples de input
                return(self.oq_fazer())
        elif escolherOpcao == '2':
            organizar(diretorio=self.local)
            return(self.__init__)
        elif escolherOpcao == '3':
            criar_pasta(localdapasta=self.local)
            return(self.__init__)
        elif escolherOpcao == '4':
            moverArquivo(localdoArquivo=self.local, voltar=self.__init__)
        else:
            return(self.__init__())

gereciador = diretorio() #Inicia o arquivo, e como tudo esta ligado nessa clase todas as funçõe iniciam normalmente