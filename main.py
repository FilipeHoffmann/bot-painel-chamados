import obter_dados_arquivo
import acessar_painel

if __name__ == "__main__":
    obter_dados = obter_dados_arquivo.obter_dados_arquivo("credenciais.json")
    obter_dados.instanciar_dados_json()
    credenciais = obter_dados.get_dados_json()
    painel = acessar_painel.acessar_painel(credenciais)
    painel.abrir_navegador()