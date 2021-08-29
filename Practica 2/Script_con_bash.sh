#!/bin/bash
# Esta funcion ayuda a crear archivos txt
function crea_Archivo(){
  ruta=/home/danylsti/Escritorio
  echo Escribe el nombre del archivo que deseas crear
  read input 
  touch $ruta/$input.txt
  echo "Deseas Crear otro txt y para si n para no (y/n)"
  read op2
  y=1
  n=2
  while [[ $op2 -eq 1 ]];
  do
    echo Escribe el nombre del archivo que deseas crear
    read input 
    touch $ruta/$input.txt
    echo "Deseas Crear otro txt y para si n para no (y/n)"
    read input
    op2=input
      
  done
}
# Esta funcion ayuda a crear Carpetas 
function Crea_Directorio(){
  ruta=/home/danylsti/Escritorio
  echo Escribe el nombre de la carpeta que deseas crear
  read input 
  mkdir $ruta/$input
  echo "Deseas Crear otra Carpeta y para si n para no (y/n)"
  read op2
  y=1
  n=2
  while [[ $op2 -eq 1 ]];
  do
    echo Escribe el nombre de la carpeta que deseas crear
    read input 
    touch $ruta/$input.txt
    echo "Deseas Crear otra Carpeta y para si n para no (y/n)"
    read input
    op2=input
    done
}
# Esta funcion ayuda a preparar el entorno git se le pasa como parametro la ruta y el nombre de la carpeta a crear
function Descargar_repo() {    
    cd /home/danylsti/$1
    mkdir $2
    cd /home/danylsti/Escritorio/$2
    #git clone https://github.com/jaunRuizz/Git-init.git
    #clear
    #echo Se clono repositorio correctamente.
    git init 
    git remote add origin $3
    git status
    git remote -v
    clear
    git pull --rebase origin master    
    git push -u origin master
    clear
    echo Todo Esta listo para usar git En tu carpeta nueva 
    #touch Archivo.txt
    #git add Archivo.txt
    #git commit -m "Este Archivo Fue subido Con un Script desde linux 26/08/2021"
    #git push -u origin master 
    #clear
    #echo Se subio tu nuevo archivo correctamente 

}
# Menu que se imprime en la linea de comando para recibir una opcion
echo Puedes pasar parametros para la opcion 4 ejemplo "(Script.sh Ruta Name-Carpeta))"
echo elije una opcion [1] Para crear archivos [2] Para crear carpetas [3] Listar los archivos actuales [4] Preparar entorno git
read input
op=$input
# El swicht para manipular las diferentes opciones 
case $op in
  1)
    crea_Archivo 
  ;;
  2)
    Crea_Directorio 
  ;;
  3)
    for i in $(ls)
    do 
      echo $i
    done
  ;;
  4)
  
    Descargar_repo $1 $2 $3
  ;;
#...
  *)
    echo Error 5996 Opcion no valida 
  ;;
esac

