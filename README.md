# WebRunner
This scraping/crawling and website cloner tool will help you to extract all url, emails on a website, allows you create your own searches using RegEx on a website and create a website copy for your phishing labs (educational purposes only)

<h3>Modules</h3>
<li>url         -Extract url from a website</li>
<li>email       -Extract emails from a website</li>
<li>regx        -Allows you to create your own searches using RegEx on a website</li>
<li>clone       -Allows you make a website copy to local folder (usefull for phishing labs) # educational purposes only</li>
<li>help        -Help about any command</li>
<br>

install requirements
```
pip3 install -r requirements.txt
```

show module help menu
```
 python3 WebRunner.py [module] -h 
 example: python3 WebRunner.py url -h
```
optional arguments:
```
  -u, --url                 set target url
  -s, --string              set RegEx query
  -a, --user-agent          set user-agent 'DirRunner v1.0' by default
  -t, --threads             set threads
  -h, --help                show this message
  -c, --cookie              set cookies to use for the requests
  -k, --no-tls-validation   skip TLS certificate verification
  -n, --name                set project name 
  -f, --folder              set destination folder 
      --timeout             HTTP Timeout (default 15s)
```
CLONE
```
 python3 WebRunner.py clone -u https://www.domain.com -n mysite
```
<img width="1380" alt="Screenshot 2023-03-27 at 11 50 29" src="https://user-images.githubusercontent.com/94752464/228036051-38e2cc74-3d6d-43f5-936a-1ec5c2bfaccb.png">


URL extractor mode
```
  python3 WebRunner.py url -u https://www.domain.com
```
<img width="1068" alt="Screenshot 2023-03-17 at 15 30 11" src="https://user-images.githubusercontent.com/94752464/226087071-73365be1-cd61-44cb-8391-a2e9da5d2c5b.png">

Emails extractor mode
```
  python3 WebRunner.py email -u https://www.domain.com
```


RegEx mode, example for extract THM{T3ST_M3SSAG3} on a website, use https://regexr.com for help
```
  python3 WebRunner.py regx -u https://www.domain.com -s "THM[A-Z0-9_{}]{6,}"
```

<img width="1002" alt="Screenshot 2023-03-17 at 15 00 36" src="https://user-images.githubusercontent.com/94752464/226087156-cffd05f5-295f-4998-8a68-c55af8a53606.png">


