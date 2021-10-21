# Librerias a utilizar
import os 
import smtplib 
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Listas

correos = []
# Agregar lista de correos electronicos

## Funcion fuera de servicio por el momento
'''
def AgregasCorreos():
    op = input("Deseas agregar una lista de correos desde un txt y pasa si n para no: ")
    if op == "y":
        txt = input("ingresa el archivo --> ")
        archivo=open(# Aqui coloca la ruta donde tengas tu txt  +txt, "r")
        archivo.readlines
        for linea in archivo:
            correos.append(linea)
        archivo.close()
        return correos
'''
# Mensaje que enviaremos y el asunto


def Msg():
    Mensaje = input("Ingresa el mensaje que deceas mandar: ")
    Asunto = input("Ingresa el asunto del mensaje: ")
    Mensaje = "Subject: {}\n\n{}".format(Asunto, Mensaje)

    # Esta funcion retorna el mensaje que se enviara al cliente y el Asundo
    return Mensaje

# Esta funcion es para el mensaje   que se mandara con HTML
def Msg_HTML():
    Mensaje = input("Ingresa el mensaje que deceas mandar: ")
    Asunto = input("Ingresa el asunto del mensaje: ")
    Mensaje = "Subject: {}\n\n{}".format(Asunto, Mensaje)

    # Esta funcion retorna el mensaje que se enviara al cliente y el Asundo
    return Mensaje , Asunto
# Recibimos datos del usuario para hacer el login


def DatosGmail():
    correo = input("Ingresa tu correo electronico: --> ")
    password = input("Ingresa tu contraseña: --> ")
    return correo, password
# Iniciamos el servidor y hacemos el login con las credenciales


def Iservidor_Login(correo, password):
        server = smtplib.SMTP("smtp.gmail.com", )

        server.starttls()

        server.login(correo, password)
    
        
        return server 
# Peticion del correo del usuario al que se le mandara el gmail


def CorreoCliente():
    usuario = input("Ingresa el correo del cliente en el \
        siguiente formato --> "+("(Ejemplo@gmail.com): "))

    return usuario


# Enviamos mensaje y cerramos el servidor

#######################################################################################################################
#      Por el  momendo solo se implemento en la funcion EnviarMSG la opcion de mandar el correo electronico           #  
#      a varios usuarios ingresando el correo manualmente en lo que se soluciona la opcion 2 para carfgar             # 
#      automaticamente un txt con todos los correos.                                                                  #                                                
#                                                                                                                     #
#                                                                                                                     #
#                                                                                                                     #  
#######################################################################################################################

# Enviamos mensaje y cerramos el servidor


def EnviarMSG(usuario, Mensaje, server, correo):
    server.sendmail(correo, usuario, Mensaje)
    op=input("Deseas mandarle a otro usuario este correo "+"si/no:")
    while op == "si":
        usuario=""
        usuario = input("Ingresa el correo del cliente en el \
            siguiente formato --> "+("(Ejemplo@gmail.com): "))
        server.sendmail(correo, usuario, Mensaje)
        op=input("Deseas mandarle a otro usuario este correo "+"si/no: ") 
    server.quit()

# Funcion para enviar HTML


def EnviarMSG_HTML(usuario, Mensaje, server, correo, mensaje):
    server.sendmail(correo, usuario, mensaje.as_string())

    server.quit()

# Funcion para enviar multiples correos a clientes 

## Existe un error al pasar la lista con multiples correos verificar antes de entregar codigo Por el momento 
## Solo Funciona la opcion 1 de mandar correos a un solo usuario 
'''
def EnviarCorreosclientes(Mensaje, server, correos, correo):
    
    server.sendmail(correo, correos[0], Mensaje)
        

    server.quit()
'''  

def FuncionHTML(Correo, usuario, Asunto):
    # Estandar
    mensaje = MIMEMultipart("Alternative")
    mensaje["Subject"] = Asunto
    mensaje["From"] = correo
    mensaje["To"] = usuario

    html = f"""
     ## Aqui puedes solocar tu mensaje en HTML 
     
    """

    parte_html = MIMEText(html, "html")

    mensaje.attach(parte_html)

    return mensaje


print("---->> Por el momento solo funciona la opcion 1 <----")
opc = int(input("Deseas mandar un mensaje a un solo usuario o a varios [1] Para un solo usuario \
                [2] Para multiples usuarios [3] Enviar mensaje HTMl: "))
if opc == 1:
    correo, password = DatosGmail()
    server = Iservidor_Login(correo, password)
    Mensaje = Msg()
    usuario = CorreoCliente()
    EnviarMSG(usuario, Mensaje, server, correo)
    print("Correo se envio con exito: ")
elif opc == 2:
    print("Lo siento usuario me encuentro fuera de servicio Estoy --> \
    En Mantenimiento Pero pronto volvere ")
    #coreros = AgregasCorreos()
    #correo, password = DatosGmail(correos)
    #server = Iservidor_Login(correo, password)
    #Mensaje = Msg()
    #EnviarCorreosclientes(correos, correo, Mensaje, server)
elif opc == 3:
    correo, password = DatosGmail()
    server = Iservidor_Login(correo, password)
    Asunto,Mensaje = Msg_HTML()
    usuario = CorreoCliente()
    mensaje=FuncionHTML(usuario,correo,Asunto)
    EnviarMSG_HTML(usuario, Mensaje, server, correo,mensaje)
    print("Correo se envio con exito: ")
else:
    print("opcion no valida intenta de nuevo: :) ")





# Este Script Fu creado por Juan Daniel
# Luevano Ruiz Puedes usarlo para imple-
# mentar,Correos automaticos.

# // Me puedes contactar a --> Mcdany996@gmail.com
