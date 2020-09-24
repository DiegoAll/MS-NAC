# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:39:16 2019
@author: Diego All
"""
import time

#General Params
print("Please enter the number of users to unregister")
nroUsuario = input()

#print("Please enter the file name or path correctly")
#fileName = str(input())

fecha = time.strftime("%y-%m-%d")
#print(fecha)
fechaQuery = "20"+fecha + " " + "03:00:00"
print(fechaQuery)

nombre_archivo = input('Introduce el nombre del archivo: ')
try:
    entrada = open(nombre_archivo)
except FileNotFoundError:
    print('Archivo no encontrado:', nombre_archivo)
    exit()

#entrada = open('usuariosDesregistrosDia9.txt', encoding ='utf-8-sig')
#entrada = open(nombre_archivo, encoding ='utf-8-sig')
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