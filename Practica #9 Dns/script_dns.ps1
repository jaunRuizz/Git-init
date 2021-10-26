$comando=ipconfig /displaydns
echo $comando > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/data-dns.txt'
$dns =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/data-dns.txt'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($dns)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/encrypt.txt'