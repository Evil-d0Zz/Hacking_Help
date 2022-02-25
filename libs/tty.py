# BIBLIOTESCAS
# =============================
from os import system
from time import sleep
# =============================
#
#
# Funçao do tty spawn shell


def fun_tty():
    while True:
        system('clear') or None
        print(f"""
            ╔╦╗╔╦╗╦ ╦  ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦  
             ║  ║ ╚╦╝  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║  
             ╩  ╩  ╩   ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n
        - Muitas vezes, durante os testes de penetração, você pode obter um shell sem ter tty, mas deseja interagir ainda mais com o sistema. Aqui estão alguns comandos que permitirão que você gere um shell tty. Obviamente, parte disso dependerá do ambiente do sistema e dos pacotes instalados.\n
            [01] - Python spawn shell
            [02] - TTY totalmente interativo
            [03] - Spawn shell do sistema operacional
            [04] - Bash spawn shell
            [05] - Perl spawn shell
            [06] - Ruby spawn shell
            [07] - Lua spawn shell
            [08] - IRB spawn shell
            [09] - VI spawn shell
            [10] - Nmap spawn shell
            [11] - Menu
            [99] - Sair
            """)
        cmd = str(input("===> "))

        if cmd == '1':
            system('clear') or None
            print("""
    ╔═╗╦ ╦╔╦╗╦ ╦╔═╗╔╗╔  ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦  
    ╠═╝╚╦╝ ║ ╠═╣║ ║║║║  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║  
    ╩   ╩  ╩ ╩ ╩╚═╝╝╚╝  ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n
        
        -python -c 'import pty; pty.spawn("/bin/bash")'
            
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '2':
            system('clear') or None
            print("""
    ╔╦╗╔╦╗╦ ╦  ╔╦╗╔═╗╔╦╗╔═╗╦  ╔╦╗╔═╗╔╗╔╔╦╗╔═╗  ╦╔╗╔╔╦╗╔═╗╦═╗╔═╗╔╦╗╦╦  ╦╔═╗  
     ║  ║ ╚╦╝   ║ ║ ║ ║ ╠═╣║  ║║║║╣ ║║║ ║ ║╣   ║║║║ ║ ║╣ ╠╦╝╠═╣ ║ ║╚╗╔╝║ ║  
     ╩  ╩  ╩    ╩ ╚═╝ ╩ ╩ ╩╩═╝╩ ╩╚═╝╝╚╝ ╩ ╚═╝  ╩╝╚╝ ╩ ╚═╝╩╚═╩ ╩ ╩ ╩ ╚╝ ╚═╝\n
    - Todos os passos para estabilizar seu shell

    O primeiro passo:

    python3 -c 'import pty;pty.spawn("/bin/bash")

    - Vamos usa Python para gerar um shell bash com melhores recursos. Neste ponto, nosso shell parecerá um pouco mais bonito, mas ainda não poderemos usar o preenchimento automático de guias ou as teclas de seta.

    O passo dois é:

    export TERM=xterm

    - Isso nos dará acesso a comandos de termos como clear.

    Finalmente (e mais importante) vamos fazer o background do shell usando:

    Ctrl + Z

    De volta ao nosso próprio terminal, usamos:

    stty raw -echo; fg

    - Isso faz duas coisas: primeiro, desliga nosso próprio eco de terminal que nos dá acesso à guia autocompletes, as teclas de seta e Ctrl + C para matar processos

    stty rows 38 columns 116        
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '3':
            system('clear') or None
            print("""
    ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦    ╔╦╗╔═╗  ╔═╗╦╔═╗╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔═╗╦═╗╔═╗╔═╗╦╔═╗╔╗╔╔═╗╦  
    ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║     ║║║ ║  ╚═╗║╚═╗ ║ ║╣ ║║║╠═╣  ║ ║╠═╝║╣ ╠╦╝╠═╣║  ║║ ║║║║╠═╣║  
    ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝  ═╩╝╚═╝  ╚═╝╩╚═╝ ╩ ╚═╝╩ ╩╩ ╩  ╚═╝╩  ╚═╝╩╚═╩ ╩╚═╝╩╚═╝╝╚╝╩ ╩╩═╝\n
            - echo os.system("/bin/bash")
                """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '4':
            system('clear') or None
            print("""
    ╔╗ ╔═╗╔═╗╦ ╦  ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦  
    ╠╩╗╠═╣╚═╗╠═╣  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║  
    ╚═╝╩ ╩╚═╝╩ ╩  ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n        
            - Bash spawn shell:
            /bin/sh -i
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '5':
            system('clear') or None
            print("""
    ╔═╗╔═╗╦═╗╦    ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦  
    ╠═╝║╣ ╠╦╝║    ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║  
    ╩  ╚═╝╩╚═╩═╝  ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n
            - Perl spawn shell:
            perl —e 'exec "/bin/sh";'
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '6':
            system('clear') or None
            print("""
    ╦═╗╦ ╦╔╗ ╦ ╦  ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦  
    ╠╦╝║ ║╠╩╗╚╦╝  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║  
    ╩╚═╚═╝╚═╝ ╩   ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n
            - Ruby spawn shell:
            ruby: exec "/bin/sh"
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '7':
            system('clear') or None
            print("""
    ╦  ╦ ╦╔═╗  ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦  
    ║  ║ ║╠═╣  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║  
    ╩═╝╚═╝╩ ╩  ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n
            - Lua spawn shell:
            lua: os.execute("/bin/sh")
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '8':
            system('clear') or None
            print("""
    ╦╦═╗╔╗   ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦       
    ║╠╦╝╠╩╗  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║       
    ╩╩╚═╚═╝  ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n 
        - IRB spawn shell:
            exec "/bin/sh"       
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '9':
            system('clear') or None
            print("""
    ╦  ╦╦  ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦         
    ╚╗╔╝║  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║         
     ╚╝ ╩  ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n 
            - VI spawn shell:
            :!bash\n
            :set shell=/bin/bash:shell  
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '10':
            system('clear') or None
            print("""
    ╔╗╔╔╦╗╔═╗╔═╗  ╔═╗╔═╗╔═╗╦ ╦╔╗╔  ╔═╗╦ ╦╔═╗╦  ╦  
    ║║║║║║╠═╣╠═╝  ╚═╗╠═╝╠═╣║║║║║║  ╚═╗╠═╣║╣ ║  ║  
    ╝╚╝╩ ╩╩ ╩╩    ╚═╝╩  ╩ ╩╚╩╝╝╚╝  ╚═╝╩ ╩╚═╝╩═╝╩═╝\n
            - Nmap spawn shell: !sh
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_tty()
            break
        elif cmd == '11':
            break
        elif cmd == '99':
            print("Até logo....")
            exit()

        else:
            print("Comando Inválido!!!")
            sleep(2)
