# BIBLIOTESCAS
# =============================
from libs import active_direct
from libs import shell
from libs import linux
from libs import tty
from libs import lfi
from libs import xss
from libs import sqli
from libs import power_shell
from libs import trans_file
from os import system
from time import sleep
# =============================
#
#
# Funçao menu


def menu():
    while True:
        system('clear') or None
        print("""
              _nnnn_  
              dGGGGMMb 
            @p~qp~~qMb
            M|@||@) M|
            @,----.JM|
            JS^\__/  qKL
          dZP        qKRb
          dZP          qKKb
        fZP  N3w.elf   SMMb
        HZM            MMMM
        FqM            MMMM
      __| ".        |\dS"qML
      |    `.       | `' \Zq
      _)      \.___.,|     .'
      \____   )MMMMMP|   .'
          `-'       `--' 
          [01] - Shell Reverse
          [02] - Comandos Úteis Do Linux
          [03] - TTY SPAWN SHELL
          [04] - Comandos Úteis Do Powershell
          [05] - Transferência de arquivo
          [06] - LFI
          [07] - XSS
          [08] - SQL Injection
          [09] - Active Directory Script's
          [99] - Sair""")

        cmd = str(input("===> "))
        if cmd == '1':
            shell.fun_shell_rev()
        elif cmd == '2':
            linux.fun_linux()
        elif cmd == '3':
            tty.fun_tty()
        elif cmd == '4':
            power_shell.fun_power_shell()
        elif cmd == '5':
            trans_file.fun_trans_file()
        elif cmd == '6':
            lfi.fun_lfi()
        elif cmd == '7':
            xss.fun_xss()
        elif cmd == '8':
            sqli.fun_sqli()
        elif cmd == '9':
            active_direct.fun_active_direct()
        elif cmd == '99':
            print("Até logo...")
            exit()
        else:
            print("Comando Inválido!!!")
            sleep(2)

menu()
