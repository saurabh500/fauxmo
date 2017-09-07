#!/bin/sh

curl 'http://192.168.1.69/toggle.php' -H 'Origin: http://192.168.1.69' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8,ms;q=0.6' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://192.168.1.69/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'outletId=3&outletStatus=off' --compressed
