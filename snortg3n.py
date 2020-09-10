#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sys

#General Params
id_change = "895695"
initialSID = 20032

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
entrada1 = open('definitivosSOC.txt', 'r')

outputFile = "contents" + ".txt"
salida = open(outputFile,'w')
salida2 = open("FirmasIoCsSOCBColNuevos.txt",'w')

linea1=entrada1.readline()
print(linea1)

cont=0 
while linea1 != '':
    
    domain = linea1.strip()
    msg = 'msg:\"LOCAL-RULES SOC ' + str(id_change) + " sid:" +str(sid) + " Domain:" + domain +"\"; "
    data = linea1.strip().split('.') #Return a list with the información
    n = len(data[0])
    print("El valor de n es: ",n)
    for item in data:  
        print((item))
        n = len(item)
        print(n)
        jex=hex(n).split('x')[1]
        
        if(n<16):
            jex = "0"+jex 
        
        print("El valor en hexa es: ", jex)   
        
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
    
