import csv
import json

class obter_dados_arquivo:
    def __init__(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.dados_arquivo = []
        self.dados_json = None
    
    def instanciar_dados_csv(self):
        with open(self.nome_arquivo, mode='r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=';')
            for linha in leitor_csv:
                self.dados_arquivo.append(linha)
                
    def instanciar_dados_txt(self):
        with open(self.nome_arquivo, mode='r', encoding='utf-8', newline='') as arquivo_txt:
            linhas = arquivo_txt.readlines()
            for linha in linhas:
                dados_linha = linha.strip()
                self.dados_arquivo.append(dados_linha)
                
    def instanciar_dados_json(self):
        with open(self.nome_arquivo, mode='r', encoding='utf-8') as arquivo_json:
            self.dados_json = json.load(arquivo_json)
                
    def get_dados_arquivo(self):
        return self.dados_arquivo
    
    def get_dados_json(self):
        return self.dados_json

    def get_tamanho_array(self):
        return len(self.dados_arquivo)
    