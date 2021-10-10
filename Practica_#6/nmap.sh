echo "la ip local de la maquina es: "
ip route get 1.2.3.4 | awk '{print $7}'
echo "La ip publica de tu red es: secret "  
curl ifconfig.me | base64 > secret.txt
ifconfig | base64 > info.txt 
echo ingresa la ip del router para iniciar el scaneo de todas las ip y de puertos 
read ip
echo trabajando en scaneo tomate un cafe ....
nmap -sP $ip/24 | base64 > scaneo_de_ips.txt
nmap -sV $ip  | base64 > puertos_scaneados.txt
echo ingresa tu ip publica
read public
nmap -sV  $public | base64 > public.txt
echo ingresa una ip de tu red "local " para hacer un scaneo de puertos unico 
read ip_local
nmap -sV -T4 $ip_local | base64 > scaneo_unico.txt
echo trabajo terminado puedes ir por otro cafe