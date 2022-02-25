# BIBLIOTESCAS
# =============================
from libs import power_shell
from os import system
from time import sleep
# =============================
#
#
def fun_active_direct():
    while True:
        system('clear') or None
        print("""
        ╔═╗╔═╗╔╦╗╦╦  ╦╔═╗  ╔╦╗╦╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗╦ ╦  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗╔═╗
        ╠═╣║   ║ ║╚╗╔╝║╣    ║║║╠╦╝║╣ ║   ║ ║ ║╠╦╝╚╦╝  ╚═╗║  ╠╦╝║╠═╝ ║ ╚═╗
        ╩ ╩╚═╝ ╩ ╩ ╚╝ ╚═╝  ═╩╝╩╩╚═╚═╝╚═╝ ╩ ╚═╝╩╚═ ╩   ╚═╝╚═╝╩╚═╩╩   ╩ ╚═╝\n
        [01] - Enumerate Domain Users
        [02] - Enumerate Domain Groups
        [03] - Enumerate Members of a Group
        [04] - Detect Service Principal Names
        [05] - Voltar
        [99] - Sair
        """)
        cmd = str(input("===> "))
        if cmd == '1':
            system('clear') or None
            print("""
        ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╦═╗  ╦ ╦╔═╗╦ ╦╦═╗╦╔═╗╔═╗  ╔╦╗╔═╗  ╔╦╗╔═╗╔╦╗╔╗╔╦╔═╗                       
        ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣╠╦╝  ║ ║╚═╗║ ║╠╦╝║║ ║╚═╗   ║║║ ║   ║║║ ║║║║║║║║║ ║                       
        ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╩╚═  ╚═╝╚═╝╚═╝╩╚═╩╚═╝╚═╝  ═╩╝╚═╝  ═╩╝╚═╝╩ ╩╝╚╝╩╚═╝\n

        $domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
        $PDC = ($domainObj.PdcRoleOwner).Name
        $SearchString = "LDAP://"
        $SearchString += $PDC + "/"
        $DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
        $SearchString += $DistinguishedName
        $Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
        $objDomain = New-Object System.DirectoryServices.DirectoryEntry
        $Searcher.SearchRoot = $objDomain
        $Searcher.filter="samAccountType=805306368"

        # To search for specific user, uncomment below
        # $Searcher.filter="name=[user_name]"

        $Searcher.FindAll()
        Foreach($obj in $Result)
        {
        Foreach($prop in $obj.Properties)
        {
        $prop
        }
        Write-Host "------------------------"
        }
        """)
            input("[*] - Pressione ENTER para voltar...")
            fun_active_direct()
            break

        if cmd == '2':
            system('clear') or None
            print("""
        ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╦═╗  ╔═╗╦═╗╦ ╦╔═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔╦╗╔═╗╔╦╗╔╗╔╦╔═╗                        
        ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣╠╦╝  ║ ╦╠╦╝║ ║╠═╝║ ║╚═╗   ║║║╣    ║║║ ║║║║║║║║║ ║                        
        ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╩╚═  ╚═╝╩╚═╚═╝╩  ╚═╝╚═╝  ═╩╝╚═╝  ═╩╝╚═╝╩ ╩╝╚╝╩╚═╝\n


        $domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
        $PDC = ($domainObj.PdcRoleOwner).Name
        $SearchString = "LDAP://"
        $SearchString += $PDC + "/"
        $DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
        $SearchString += $DistinguishedName
        $Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
        $objDomain = New-Object System.DirectoryServices.DirectoryEntry
        $Searcher.SearchRoot = $objDomain
        $Searcher.filter="(objectClass=Group)"
        $Result = $Searcher.FindAll()
        Foreach($obj in $Result)
        {
        $obj.Properties.name
        }
        """)
            input("[*] - Pressione ENTER para voltar...")
            fun_active_direct()
            break

        elif cmd == '3':
            system('clear') or None
            print("""
        ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╦═╗  ╔╦╗╔═╗╔╦╗╔╗ ╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╦ ╦╔╦╗  ╔═╗╦═╗╦ ╦╔═╗╔═╗              
        ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣╠╦╝  ║║║║╣ ║║║╠╩╗╠╦╝║ ║╚═╗   ║║║╣   ║ ║║║║  ║ ╦╠╦╝║ ║╠═╝║ ║              
        ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╩╚═  ╩ ╩╚═╝╩ ╩╚═╝╩╚═╚═╝╚═╝  ═╩╝╚═╝  ╚═╝╩ ╩  ╚═╝╩╚═╚═╝╩  ╚═╝\n


        $domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
        $PDC = ($domainObj.PdcRoleOwner).Name
        $SearchString = "LDAP://"
        $SearchString += $PDC + "/"
        $DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
        $SearchString += $DistinguishedName
        $Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
        $objDomain = New-Object System.DirectoryServices.DirectoryEntry
        $Searcher.SearchRoot = $objDomain

        # change "Secret_Group" to correct group name
        $Searcher.filter="(name=Secret_Group)"
        $Result = $Searcher.FindAll()
        Foreach($obj in $Result)
        {
        $obj.Properties.member
        }
        """)
            input("[*] - Pressione ENTER para voltar...")
            fun_active_direct()
            break
        elif cmd == '4':
            system('clear') or None
            print("""
        ╔╦╗╔═╗╔╦╗╔═╗╔═╗╔╦╗╔═╗╦═╗  ╔╗╔╔═╗╔╦╗╔═╗╔═╗  ╔═╗╦═╗╦╔╗╔╔═╗╦╔═╗╔═╗╦╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦═╗╦  ╦╦╔═╗
        ║║║╣  ║ ║╣ ║   ║ ╠═╣╠╦╝  ║║║║ ║║║║║╣ ╚═╗  ╠═╝╠╦╝║║║║║  ║╠═╝╠═╣║╚═╗   ║║║ ║  ╚═╗║╣ ╠╦╝╚╗╔╝║║ ║
        ═╩╝╚═╝ ╩ ╚═╝╚═╝ ╩ ╩ ╩╩╚═  ╝╚╝╚═╝╩ ╩╚═╝╚═╝  ╩  ╩╚═╩╝╚╝╚═╝╩╩  ╩ ╩╩╚═╝  ═╩╝╚═╝  ╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝\n


        $domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
        $PDC = ($domainObj.PdcRoleOwner).Name
        $SearchString = "LDAP://"
        $SearchString += $PDC + "/"
        $DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
        $SearchString += $DistinguishedName
        $Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
        $objDomain = New-Object System.DirectoryServices.DirectoryEntry
        $Searcher.SearchRoot = $objDomain
        $Searcher.filter="serviceprincipalname=*http*" # change name as needed
        $Result = $Searcher.FindAll()
        Foreach($obj in $Result)
        {
        Foreach($prop in $obj.Properties)
        {
        $prop
        }
        }
        """)
            input("[*] - Pressione ENTER para voltar...")
            fun_active_direct()
            break
        elif cmd == '5':
            break
        elif cmd == '99':
            print("Até logo....")
            exit()
        else:
            print("Comando Inválido!!!")
            sleep(2)
