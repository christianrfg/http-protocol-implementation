#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:58:45 2017

@author: Christian R. F. Gomes
@title: Cliente (Navegador)
"""

import socket
import sys
from threading import Thread
import time

PATH_URL = sys.argv[1]
TCP_IP = socket.gethostname()
BUFFER_SIZE = 1024

if len(sys.argv) == 3:
    TCP_PORT = int(sys.argv[2])
else:
    TCP_PORT = 80


class ClientThread(Thread):
    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        print('[+] Nova thread por ' + ip + ' na porta ' + str(port))

    def run(self):
        URL_RCV = self.conn.recv(BUFFER_SIZE)
        URL_RCV = URL_RCV.decode('utf-8')
        FILE_PATH = PATH_URL + "/" + URL_RCV
        print('URL solicitada pelo navegador (cliente): ' + URL_RCV)

        try:
            f = open(FILE_PATH, 'rb')
            l = f.read(BUFFER_SIZE)
            # Envia código de estado + frase
            self.conn.sendall('200 OK'.encode('utf-8'))
            time.sleep(0.1)

            while l:
                # print('Enviando arquivo solicitado...')
                self.conn.sendall(l)
                l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    self.conn.close()
                    print('[-] Arquivo enviado com sucesso, conexão fechada.\n')
                    break
        except (OSError, IOError) as e:
            # Envia código de estado + frase
            print('[-] Arquivo solicitado não existe; enviando mensagem de erro 404.\n')
            self.conn.sendall('404 Not Found'.encode('utf-8'))
            self.conn.close()


tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_sock.bind((TCP_IP, TCP_PORT))
threads = []

print('Server escutando...')

while True:
    tcp_sock.listen(5)
    print('Esperando por conexões...')

    (conn, (ip, port)) = tcp_sock.accept()  # Estabelece conexao com o cliente
    print('Conexão feita por ', (ip, port))
    conn.settimeout(60)  # Cliente é desconectado depois de 60s de inatividade
    new_thread = ClientThread(ip, port, conn)
    new_thread.start()
    threads.append(new_thread)

for t in threads:
    t.join()
