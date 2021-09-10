#!/bin/bash
#                                               {*****************************************************************************}
#                                               {                                                                             }
#                                               {                    Sticky Password Autofill Engine                          }
#                                               {                              Chromium Log                                   }
#                                               {                                                                             }
#                                               {                       Copyright (C) 2021 Lamantine Software a.s.            }
#                                               {                                                                             }
#                                               {*****************************************************************************}
#
#
#                   <!--               Para mas informacion sobre los modulos utilizados en Este script visita las siguientes URL           -->
#                   <!--                  https://docs.github.com/en/graphql/guides/forming-calls-with-graphql#authenticating-with-graphql  -->
#                   <!--                      https://docs.github.com/en/rest/overview/resources-in-the-rest-api#basic-authentication       -->
#                   <!--                                     https://docs.github.com/en/rest/overview/api-previews                          -->
#                   <!--                   Para mas informacion sobre los modulos utilizados en Este script visita las siguientes URL       -->
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Esta funcion solicita al servidor los repositorios que tienes en tu git hub 


ver_repos () {
    echo Escribe tu nombre de usuario de Git hub
    read user
    ## Esta linea de codigo hace la llamada a los servidores de github para obtener los repositorios del usuario y los guarda en un txt
    curl -s  "https://api.github.com/users/$user/repos" | grep "^    \"url\""|cut -d "\"" -f 4 | head -n 30
}
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Esta funcion genera los txt con todos los url de cada repositorio 


generar_txt () {
echo Escribe tu nombre de usuario de Git hub
read user
#En esta linea de codigo se le el contenido de repo y se almacenan solo los repositorios existentes en otro txt limpio
curl -s  "https://api.github.com/users/$user/repos" > Repos.txt
    cat repos.txt | grep "\"name\"" |cut -d "\"" -f 4 | head -n 30  > "C:\Users\mcdan\Desktop\Practica_#3\Mis-Repos-Encontrados\repositorios.txt"
    echo Se creo archivo con exito
}
#------------------------------------------------------------------------------------------------------------------------------------------------------
# Esta funcion generara los txt con la informacion de los commits de cada uno de los repositorios de tu cuenta de git hub 


generar_txt_commits () {
    #En esta linea de codigo se le el contenido de repo y se almacenan solo los repositorios existentes en otro txt limpio
    cat repos.txt | grep "\"name\"" |cut -d "\"" -f 4 | head -n 30  > "C:\Users\mcdan\Desktop\Practica_#3\name_repos.txt"
    #segunda solicitud a la api
    echo Escribe tu nombre de usuario de Git hub
    read user
    c=1
    for i in `cat "C:\Users\mcdan\Desktop\Practica_#3\name_repos.txt"`
    do
        curl -s https://api.github.com/repos/$user/$i/commits > "C:\Users\mcdan\Desktop\Practica_#3\commits\commits$c.txt"
        c=$(($c+1))
    done
}

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Esta funcion nos permitira obtener informacion sobre tu usuario


ver_data_user () {
    echo Escribe tu nombre de usuario de Git hub
    read user
    echo Escribe tu token
    read token
    curl -u $user:$token "https://api.github.com/users/$user" > data_user.txt
}

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Esta funcion va a analizar la informacion tecnica de cada uno de los repositorios y va a guardar esta informacion en txt


analizar_repos () {
    echo Escribe tu nombre de usuario de Git hub
    read user
    echo Escribe tu token
    read token
    c=1
    for i in `cat "C:\Users\mcdan\Desktop\Practica_#3\name_repos.txt"`
    do
        curl -u $user:$token "https://api.github.com/repos/$user/$i" > "C:\Users\mcdan\Desktop\Practica_#3\data_rep\data_repo$c.txt"
        c=$(($c+1))
    done
}
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Este es el ciclo while que se encargara de mostrar el menu en todo momento
op=0
while [ $op -ne 9 ]; do
    # Este es el panel de opciones para elejir las diferentes acciones
    
    echo [1] Ver repositorios
    echo [2] Generar txt con repositorios
    echo [3] generar txt de commits
    echo [4] Ver info de tu usuaro
    echo [5] crear informacion tecnica de todos los repos que tienes en txt
    echo [9] Salir del script
    #
    read -p "Seleciona una opcion " op
    # Este es el case que se encargara de llamar a lar funciones segun el usuario elija cada una de las opciones
    case $op  in
        1)
            ver_repos
        ;;
        2)
            generar_txt
        ;;
        3)
            generar_txt_commits
        ;;
        4)
            ver_data_user
        ;;
        5)
          analizar_repos  
        ;;
        9)
            echo Hasta luego cuidate
        ;;
        #...
        *)
            echo Error opcion invalida _521_
        ;;
    esac
done

#                                      #/********************************************************************************#                                     #
#                                      # /**************Este script Fue desarollado por Juan Daniel Luevano Ruiz ********#                                     #
#                                      #  /******************************************************************************#                                     #
#                                      #   /*****************************************************************************#                                     #
#                                      #    /****************************************************************************#                                     #

