import argparse
from os import system
from time import sleep
from subprocess import run

#Variaveis
site = ('wget -qO - http://checkip.amazonaws.com')
arq = ('ips.txt')  #TODO Criação de arquivo para armazenamento de ips automatico ou por meio de argumentos
                   #TODO Teste de urls padrões para o (site) caso checkip.amazonaws.com não funcione

#Define o novo ip e lê o ip do arquivo
def readFile():

    with open(arq, "r") as file:
        saveNewIp = file.read()
        file.close
    return saveNewIp

#Formata a data para saida do notify
def dateFormat():

    date = run("date +'%H-%M-%S:'", shell=True, capture_output=True, text=True)
    wget = run(site, shell=True, capture_output=True, text=True)
    format = date.stdout+wget.stdout
    return format

#Lê o ip do comando wget (site)
def testIp():
    wget = run(site, shell=True, capture_output=True, text=True)
    return wget.stdout

#Notifica o começo da execução do programa
system('echo "[+] Notificando Novos IPs" | notify')

try:

    while (True):
        #Lê o arquivo, testa o ip atual e compara os dois
        if readFile() != testIp():
            #Se diferente escreve o novo ip no arquivo
            system(site+' > '+arq)
            #Envia a notificação formatada com data e novo ip
            system('echo "IP Modificado ás: '+dateFormat()+'" | notify -bulk')
        else:
            sleep(30)

except:
    #Notifica o encerramento do programa
    system('echo "[-] Notificando Novos IPs Encerrado!" | notify')
