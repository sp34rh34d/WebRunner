#!/bin/bash

cBlack='\033[0;30m'
cRed='\033[0;31m'
cGreen='\033[0;32m'
cOrange='\033[0;33m'
cBlue='\033[0;34m'
cPurple='\033[0;35m'
cCyan='\033[0;36m'
cLightGray='\033[0;37m'
cDarkGray='\033[1;30m'
cLightRed='\033[1;31m'
cLightGreen='\033[1;32m'
cYellow='\033[1;33m'
cLightBlue='\033[1;34m'
cLightPurple='\033[1;35m'
cLightCyan='\033[1;36m'
cWhite='\033[1;37m'
cNothing='\033[0m'

echo -e """
 .S     S.     sSSs   .S_SSSs     .S_sSSs     .S       S.    .S_sSSs     .S_sSSs      sSSs   .S_sSSs    
.SS     SS.   d%%SP  .SS~SSSSS   .SS~YS%%b   .SS       SS.  .SS~YS%%b   .SS~YS%%b    d%%SP  .SS~YS%%b   
S%S     S%S  d%S'    S%S   SSSS  S%S   'S%b  S%S       S%S  S%S   'S%b  S%S   'S%b  d%S'    S%S   'S%b  
S%S     S%S  S%S     S%S    S%S  S%S    S%S  S%S       S%S  S%S    S%S  S%S    S%S  S%S     S%S    S%S  
S%S     S%S  S&S     S%S SSSS%P  S%S    d*S  S&S       S&S  S%S    S&S  S%S    S&S  S&S     S%S    d*S  
S&S     S&S  S&S_Ss  S&S  SSSY   S&S   .S*S  S&S       S&S  S&S    S&S  S&S    S&S  S&S_Ss  S&S   .S*S  
S&S     S&S  S&S~SP  S&S    S&S  S&S_sdSSS   S&S       S&S  S&S    S&S  S&S    S&S  S&S~SP  S&S_sdSSS   
S&S     S&S  S&S     S&S    S&S  S&S~YSY%b   S&S       S&S  S&S    S&S  S&S    S&S  S&S     S&S~YSY%b   
S*S     S*S  S*b     S*S    S&S  S*S   'S%b  S*b       d*S  S*S    S*S  S*S    S*S  S*b     S*S   'S%b  
S*S  .  S*S  S*S.    S*S    S*S  S*S    S%S  S*S.     .S*S  S*S    S*S  S*S    S*S  S*S.    S*S    S%S  
S*S_sSs_S*S   SSSbs  S*S SSSSP   S*S    S&S   SSSbs_sdSSS   S*S    S*S  S*S    S*S   SSSbs  S*S    S&S  
SSS~SSS~S*S    YSSP  S*S  SSY    S*S    SSS    YSSP~YSSY    S*S    SSS  S*S    SSS    YSSP  S*S    SSS  
                     SP          SP                         SP          SP                  SP          
                     Y           Y                          Y           Y                   Y      
Coded by: $cRed Adonis Izaguirre $cNothing Email: $cRed adonis.izaguirre@kapa7.com $cNothing"""

echo -e "Welcome to WebRunner!"
read -e -p "enter url (https://www.example.com): " url 

domain=$(echo $url | sed -e 's,http:\/\/,,g' -e 's,https:\/\/,,g' | sed -e 's/\./ /g' | awk '{print $2"."$3}')

curl -s -k $url | grep -o -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b' | sort | uniq > email.txt
curl -s -k $url | grep -o -E '(https*://|www\.|http*//)[^ ]*' | sed -e 's,\\, ,g' -e 's,", ,g' -e 's,), ,g' -e "s,', ,g" -e 's,>, ,g' -e 's,;, ,g' -e 's/,/ /g' -e 's,}, ,g' -e 's,<, ,g'| awk {'print $1'} | sort | uniq > url.txt

cat url.txt | grep $domain > internalUrl.list

echo -e $cGreen"[+] Looking for urls"$cNothing
while read line;
do
    curl -s -k $line | grep -o -E '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b' | sort | uniq >> email.txt
 	curl -s -k $line | grep -o -E '(https*://|www\.|http*//)[^ ]*' | sed -e 's,\\, ,g' -e 's,", ,g' -e 's,), ,g' -e "s,', ,g" -e 's,>, ,g' -e 's,;, ,g' -e 's/,/ /g' -e 's,}, ,g' -e 's,<, ,g'| awk {'print $1'} | sort | uniq >> url.txt
done < internalUrl.list

echo -e $cGreen"[+] Emails detected"$cNothing
cat email.txt | sort | uniq | nl

echo -e $cGreen"[+] Urls detected"$cNothing
cat url.txt | sort | uniq | nl


