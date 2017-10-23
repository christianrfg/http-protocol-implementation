# Trabalho Prático 1 de Redes de Computadores

## Introdução
Implementação, em **Python**, de duas aplicações sobre o protocolo HTTP e utilizando somente o método GET.
São implementados um navegador (cliente) e um servidor web (servidor).
Para mais detalhes consultar, logo abaixo, a documentação completa do trabalho.

## Documentação
[PDF](https://github.com/christianrfg/http-protocol-implementation/blob/master/doc.pdf) - Documentação do TP1

## Implementação
O cliente e servidor foram implementados em pastas diferentes, onde na **pasta do servidor** contém os arquivos (url's) de exemplos criados e na **pasta do cliente** possui somente o código do navegador.

### Servidor
O servidor suporta a conexão de multiplos clientes ao mesmo tempo (multithreading) e, primeiramente, envia uma resposta de sucesso (200 OK) ou erro (404 Not Found) de acordo com à URL que o cliente deseja. Após essa confirmação, em caso de sucesso, a URL solicitada é enviada ao cliente e a conexão é fechada e, em caso de erro, é enviado somente a mensagem confirmando que um erro ocorreu.

* Exemplo de Execução do Servidor:

```
python servidor.py public_html 8080
```

Onde public_html é a pasta principal do servidor que conterá os URL's e o número 8080 é a porta na qual o servidor rodará.

* **Observação**: O servidor executará para sempre se não ocorrer uma interrupção para fecha-lo; logo, depende do usuário fechar o servidor (com um key interrupt (Ctrl + C) ou fechando o terminal).

### Navegador (Cliente)
O cliente, que também funciona por linha de comando, executa uma requisição de uma URL (pasta/arquivo) para o servidor que está em execução esperando conexões. Se o servidor retornar uma mensagem de sucesso, ele cria a pasta para o recebimento da URL solicitada (arquivo) e fecha a conexão após o recebimento. Em caso de erro, somente a mensagem de erro é exibida no terminal e, em seguida, a conexão é fechada .

* Exemplo de Execução do Cliente:

```
python navegador.py www.videos.com/teste1.mp4 8080
```

As URL's solicitadas serão salvas na mesma pasta que está contido o arquivo python do cliente.


## Programas Utilizados
* [Python Documentation](https://docs.python.org/3.5/) - Python 3.5
* [PyCharm Site](https://www.jetbrains.com/pycharm/) - PyCharm - Python IDE

## Autores
* **Christian R. F. Gomes** - [christianrfg](https://github.com/christianrfg)
