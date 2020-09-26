# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:45:55 2019
NAC MANAGEMENT SCRIPTS
@author: Diego All
"""
import os
import time

#print("Path at terminal when executing this file")
#print(os.getcwd() + "\n")

def unregNodes(nroUsuario, nombre_archivo):
    fecha = time.strftime("%y-%m-%d")
    #print(fecha)
    fechaQuery = "20"+fecha + " " + "03:00:00"
    print(fechaQuery)
    
    salida = open(nombre_archivo+'_Query.txt', 'w')
    
    proyeccion = "select distinct node.pid, node.mac,IF(SUBSTRING(node.computername, 2, 4) REGEXP '^[0-9]+$', SUBSTRING(node.computername, 2, 4), 'Validar-manualmente') as CodSucursal, locationlog.switch_ip,node.status, node.regdate, node.unregdate from node, locationlog where ("
    proyeccionComparacion = "select distinct node.pid from node, locationlog where ("
    filtroAdicional = ") and node.status ='reg' and node.mac =locationlog.mac and voip!='yes' group by pid;"
    filtroAdicionalOrder = ") and node.status ='reg' and node.mac =locationlog.mac and voip!='yes' order by pid;"
    usuario = ''
    desregistrar = "node.pid like " + usuario + "and"
    
    querydesregistrar = ''
    #nroUsuario = 64
    
    cont = 1
    linea=entrada.readline()
    
    #Conjunto Usuarios a desregistrar cronograma
    usuariosCronograma = set()
    #Conjunto usuarios de la consulta
    usuariosQuery = set()
    
    while linea != '':
        print(linea)
        usuariosCronograma.add(linea)
        usuario = "'" + linea #+ "'"
        usuario = usuario.strip('\n')
        if(nroUsuario != cont):
            desregistrar = "node.pid like " + usuario + "' "+ "or "
        else:
            desregistrar = "node.pid like " + usuario + "' "
            
        querydesregistrar = querydesregistrar + desregistrar
        cont = cont + 1
        linea=entrada.readline()
    
    querySeleccion = proyeccion+querydesregistrar+filtroAdicional
    queryComparacion = proyeccionComparacion+querydesregistrar+filtroAdicional
    queryMACs = proyeccion+querydesregistrar+filtroAdicionalOrder
    
    print(querydesregistrar)
    print(cont)
    print(type(querydesregistrar))
    print(querySeleccion)
    salida.write(querySeleccion+'\n')
    print("\n")
    print("\n")
    salida.write(queryComparacion+'\n')
    print("\n")
    print("\n")
    salida.write(queryMACs)
    entrada.close()
    
    print ("Usuarios a desregistrar del cronograma")
    print(type(usuariosCronograma))
    print(len(usuariosCronograma))
    print(usuariosCronograma)
    
    print("\n")
    
    updateNxLHead="update node,locationlog set unregdate='"+fechaQuery+"'"+" where (("
    updateNxLFoot="and node.status ='reg' and node.mac =locationlog.mac and voip!='yes');"
    
    print("\n")
    
    updateNHead="update node set unregdate='"+fechaQuery+"'"+" where (("
    updateNFoot=" and node.status='reg' and voip!='yes');"
        
    updateNxL = updateNxLHead+querydesregistrar+")"+updateNxLFoot
    updateN = updateNHead+querydesregistrar+")"+updateNFoot
    
    print(updateNxL)
    print("\n")
    print(updateN)
    
    salida.write(updateNxL+'\n')
    salida.write(updateN+'\n')
    salida.close()


def snortG3N(id_change, initialSID, IoCsFile):
   
    #Rule structure
    ruleHeader = {'action':'alert', 'protocol':'udp', 'srcIP':'any', 'srcPort':'any'
                  , 'direction':'->', 'dstIP':'any', 'dstPort':'53'}
    
    header = ruleHeader['action']+" "+ruleHeader['protocol']+" "+ruleHeader['srcIP']+" "+ruleHeader['srcPort']+" "+ruleHeader['direction']+" "+ruleHeader['dstIP']+" "+ruleHeader['dstPort']
    print(header)
    
    #Rule Options
    msg = 'msg:\"LOCAL-RULES' + str(id_change) +"\"; "
    content = "content:" + "; "
    nocase = "nocase" + "; "
    sid = initialSID
    rev = "rev:1" + ";"
    
    domain = ""
    contentAux = ""
    #entrada1 = open('definitivosSOC.txt', 'r')
    #entrada1 = open('/home/diego/codes/ms-nac/definitivosSOC.txt', 'r')
    entrada1 = open(IoCsFile, 'r')
    
    
    outputFile = "contents" + ".txt"
    salida = open(outputFile,'w')
    salida2 = open("IoCsTest_SnortRules.txt",'w')
    
    linea1=entrada1.readline()
    print(linea1)
    
    cont=0 
    while linea1 != '':
        
        domain = linea1.strip()
        msg = 'msg:\"LOCAL-RULES SOC ' + str(id_change) + " sid:" +str(sid) + " Domain:" + domain +"\"; "
        data = linea1.strip().split('.') #Return a list with the información
        n = len(data[0])
    #    print("El valor de n es: ",n)
        for item in data:  
            print((item))
            n = len(item)
            print(n)
            jex=hex(n).split('x')[1]
            
            if(n<16):
                jex = "0"+jex 
            
         #   print("El valor en hexa es: ", jex)   
            
            contentAux = contentAux + "|"+ jex +"|" + item
            print(contentAux)
        
        content = contentAux 
        print("el content es: ", content)
        salida.write(content +'\n')
        rule = header + "(" + msg + "content:\""+content +"\"; " + nocase + "sid:"+str(sid) + "; " + rev + ")" +'\n'
        salida2.write(rule) 
    
        cont=cont+1
        linea1=entrada1.readline()
        contentAux = ""
        aux = ""
        content = ""
        sid = sid + 1

def about():
    disclaimer = """    ##################################################
    ##                                              ##
    ##              *** DISCLAIMER ***              ##
    ##                                              ##
    ##################################################"""
    
    text = """     This scripts compendium can be used to help manage
     a productive environment of a NAC solution based on packetfence
     4.3 and Snort 2.9"""
    
    responsability = "     We are not responsible for the use that is given to this utility or information."
    version = "v. 1.2"
    print("")
    print(disclaimer)
    print("")
    print("         MANAGEMENT SCRIPTS NAC")
    print("")
    print("          "+version)
    print("")
    print("")
    print(text)
    print("")
    print("")
    print(responsability)
    print("")

#Main Menu
opciones=["1", "2", "3", "4", "5", "6"]

while True:
    
    print(''' __  __ ____        _   _    _    ____ 
|  \/  / ___|      | \ | |  / \  / ___|
| |\/| \___ \ _____|  \| | / _ \| |    
| |  | |___) |_____| |\  |/ ___ \ |___ 
|_|  |_|____/      |_| \_/_/   \_\____|

'''+ "      v. 1.2")
    print("")
    print("By DiegoAll \n"+"contact: dposadallano@gmail.com")
    print('''
    MANAGEMENT SCRIPTS NAC
    1. Unregister Nodes
    2. Serverkey Extractor
    3. SnortG3N
    4. sid-msg.map Calc
    5. About
    6. Exit
    ''')
        
    opcion=input("Choose an action (1,2,3,4,5,6) ")
    if not(opcion in opciones):
        print("No seleccionó ninguna opción válida")
        input("Pulse para continuar")
        continue
    if opcion=="1":
        try:
            print("Unregister Nodes")
            nroUsuarios=int(input("Please enter the number of users to unregister: "))
            
            nombre_archivo = input('Please enter the unreg users file name: ')
            try:
                entrada = open(nombre_archivo, encoding ='utf-8-sig')
                unregNodes(nroUsuarios, nombre_archivo)
                
            except FileNotFoundError:
                print('Archivo no encontrado:', nombre_archivo)
                continue  
        except:
            print("Alguno de los valores no es correcto")
            input("Pulse para ir al menú")
            continue
    if opcion=='2':
        try:
            print("ServerKey Extractor")
        except:
            print("Que mas pues parcero")
            input("Pulse para ir al menú")
            continue
    if opcion=='3':
        try:
            print("SnortG3N")
            #id_change, initialSID, IoCsFile
            id_change=int(input("Please enter the change id: "))
            initialSID=int(input("Please enter the initial SID for the new rules: "))
            
            IoCsFile = input('Please enter the IoCs file name: ')
            try:
                entrada = open(IoCsFile, encoding ='utf-8-sig')
                snortG3N(id_change, initialSID, IoCsFile)
                
            except FileNotFoundError:
                print('Archivo no encontrado:', IoCsFile)
                continue  
        except:
            print("Alguno de los valores no es correcto")
            input("Pulse para ir al menú")
            continue
    
    if opcion=='5':
        about()
        input("Pulse para ir al menú")
        continue
              
    if opcion=='6':
        break
print("See you later")  



