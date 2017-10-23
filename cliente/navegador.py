#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:58:45 2017

@author: Christian R. F. Gomes
@title: Navegador (Cliente)
"""

import sys
import socket
import os


URL = sys.argv[1]
TCP_IP = socket.gethostname()
BUFFER_SIZE = 1024

if len(sys.argv) == 3:
    TCP_PORT = int(sys.argv[2])
else:
    TCP_PORT = 80

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect((TCP_IP, TCP_PORT))
tcp_sock.sendall(URL.encode('utf-8'))

HTTP_RCV_CODE = tcp_sock.recv(BUFFER_SIZE)
HTTP_RCV_CODE = HTTP_RCV_CODE.decode('utf-8')
COD_FRA = HTTP_RCV_CODE.split()

if int(COD_FRA[0]) == 200:
    print('Resposta do servidor: ' + HTTP_RCV_CODE)

    # Criação do diretório no cliente, se não existir.
    # Python 3.2+
    os.makedirs(os.path.dirname(URL), exist_ok=True)

    # Python 3.2-
    # if not os.path.exists(os.path.dirname(URL)):
    #     try:
    #         os.makedirs(os.path.dirname(URL))
    #     except OSError as exc:
    #         print('Falha na criação do diretório.')

    with open(URL, 'wb') as f:
        while True:
            # print('Recebendo dados...')
            data = tcp_sock.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
        f.close()
        print('URL solicitada obtida com sucesso.')
        tcp_sock.close()
        print('Conexão fechada.')
else:
    print('Resposta do servidor: ' + HTTP_RCV_CODE)
    tcp_sock.close()
