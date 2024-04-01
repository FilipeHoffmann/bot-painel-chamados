# painelChamados
O bot desenvolvido em Python automatiza a inicialização do painel de chamados da área da saúde no anexo da Prefeitura Municipal de Imbé/RS.

## Bibliotecas necessárias
* PyAutoGUI</br>
* Selenium
  
## Configuração
Para iniciar o script é necessário configurar o arquivo **credenciais.json** que possuí o seguinte formato:

1 - URL do site a ser acessado.</br>
2 - O login de acesso ao site.</br>
3 - A senha de acesso ao site.</br>

## Corpo do arquivo credenciais.json
    {
        "url": "exemplo.com",
        "login": "teste",
        "senha": "teste"
    }