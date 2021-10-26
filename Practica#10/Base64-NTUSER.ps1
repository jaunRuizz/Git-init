$NTUSER =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/NTUSER.DAT'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($NTUSER)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/encrypt1.txt'
$NTUSER =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/reporte-v10.log'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($NTUSER)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/encrypt2.txt'
$NTUSER =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/reporte-v10.txt'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($NTUSER)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/encrypt3.txt'