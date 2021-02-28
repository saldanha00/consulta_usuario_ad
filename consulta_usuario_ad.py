from pypsexec.client import Client
import sys
import os

###Autor: Lucas Ferreira
####Exemplo de utilização:
###python3 atualiza_grupo_ad.py usuarios_vip


##Variaveis Globais
user = sys.argv[1] ##Param must be an valid user in domain.
usuario = "" ## user@domain
senha = "" ##password for connection
servidor = "" ##IP address of DC used for consults

def main():
        chamada = ConsultaUsuarioAD()
        chamada.ConsultaUsuarioAD(servidor,usuario,senha,user)

class ConsultaUsuarioAD:

    def ConsultaUsuarioAD(self,servidor,usuario,senha,user):
        c = Client("%s"%servidor, username="%s"%usuario, password="%s"%senha)
        c.connect()

        try:
            c.create_service()
            stdout, stderr, rc = c.run_executable("cmd.exe",
                                                  arguments="/c net user %s" %user)
            arquivo = open("user.txt","wb")
            arquivo.write(stdout)
            arquivo.close()
            os.system("cat user.txt")

        finally:
            c.remove_service()
            c.disconnect()


if __name__ == '__main__':
        main()
