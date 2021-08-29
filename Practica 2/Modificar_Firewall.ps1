function Modificar_Firewall{
    param([parameter(mandatory)][string] $NameRed)
    process{
        $opc = Read-Host -Prompt "Seleciona una opcion [1] Ver reglas de bloqueo [2] Para publico [3] Para  Privado [4] Cambiar status de perfil de red"
        switch ($opc){
        1 {
          Get-NetFirewallRule 
         break
        } 2 {
         $status=Get-NetFirewallProfile -Name public
         if ($status.enabled){
            write-host "El perfil publico Esta : Activado"
            $op =Read-host "Deseas Desactivarlo ingresa la letra y o n para no "
            if ($op -eq "y"){
                Set-NetFirewallProfile -Name Public -Enabled False
                write-host "El estado de tu red a cambiado "
                Get-NetConnectionProfile
                break
            } else {
                write-host El estado no cambio Adios 
            }
         } else {
             write-host "El perfil publico Esta : Desactivado"
             $op =Read-host "Deseas Activarlo ingresa la letra y o n para no"
             if ($op -eq "y"){
                Set-NetFirewallProfile -Name public -Enabled True
                write-host "El estado de tu red a cambiado "
                Get-NetConnectionProfile
                break
            } else {
                write-host El estado no cambio Adios 
            }
         }
         
       
        } 3 {
         $status=Get-NetFirewallProfile -Name private
         if ($status.enabled){
            write-host "El perfil privado Esta : Activado"
            $op =Read-host "Deseas Desactivarlo ingresa la letra y o n para no "
            if ($op -eq "y"){
                Set-NetFirewallProfile -Name  Private -Enabled False
                write-host "El estado de tu red a cambiado "
                Get-NetConnectionProfile
                break
            } else {
                write-host El estado no cambio Adios 
            }
         } else {
             write-host "El perfil privado Esta : Desactivado"
             $op =Read-host "Deseas Activarlo ingresa la letra y o n para no"
             if ($op -eq "y"){
                Set-NetFirewallProfile -Name private -Enabled True
                write-host "El estado de tu red a cambiado "
                Get-NetConnectionProfile
                break
            } else {
                write-host El estado no cambio Adios 
            }
            }
         
        } 4{
        $perfilActual = Get-NetConnectionProfile -Name $NameRed 
        if ($perfilActual.NetworkCategory -eq "Private")
        {
            write-host El perfil Actual es el Private 
        } else {
            Write-Host El perfil actual es el publico
        }
        $NamePerfil=read-host  ingresa el nombre del perfil al que quieres cambiar 
        Set-NetConnectionProfile -Name $NameRed -NetworkCategory $NamePerfil
        Write-Host El perfil se Actualizo a --> $NamePerfil

        } default {
        
        write-Host "Error 502 (Opcion no valida)"
        } 
        }
        }

}

Modificar_Firewall