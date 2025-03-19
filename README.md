# WebRunner
WebRunner is a powerful and versatile reconnaissance scanner designed for web security assessments. It performs comprehensive website scans by extracting key information such as URLs, email addresses, and custom data defined by regular expressions. With configurable crawl depth, users can tailor the scanning process—from shallow overviews to deep, exhaustive analysis—making it ideal for both quick reconnaissance and in-depth security evaluations.
Additionally, WebRunner can clone entire websites, providing an offline replica for further analysis, and it includes specialized scanning features to identify vulnerabilities like path traversal. 

### Install
```
git clone https://github.com/sp34rh34d/WebRunner.git
cd DirRunner
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
chmod +x WebRunner.py
```

### One line Installation
```
git clone https://github.com/sp34rh34d/WebRunner.git && cd WebRunner && python3 -m venv env && source env/bin/activate && pip3 install -r requirements.txt && chmod +x WebRunner.py
```

## Features
* Web Scraping/Crawler [url | email | RegEx Query]
* Web Cloner
* Path Traversal Scanner

## Pending features
* 403 Bypass Scanner
* SQLi Scanner

## TOR 
You can use TOR project to create your HTTP Proxy with parameter ```HTTPTunnelPort 9055```, and use that port with argument ```--proxy http://127.0.0.1:9055```, if u wanna change your IP for every request, you can use the arg ```--rnd-ip```, but you will need to especify a torrc file, create it with the following parameter.
```
#torrc file content
HTTPTunnelPort 9055
CookieAuthentication 1
ControlPort 9051
```
Then just run ```tor -f torrc```

### Scraping module
```
Uses Scraping mode

Usage:
    python3 WebRunner.py scraping [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --max-depth                 Set depth level to scan


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set http proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    --rnd-ip                    Changes TOR proxy IP for every requests (torcc file required)
    -h, --help                  Show this message
```

![Screenshot 2025-03-19 at 10 25 03 AM](https://github.com/user-attachments/assets/8a3ffb2f-5614-41da-b3e0-a12463ef662d)



### Email extractor module
```
Uses Email extractor mode

Usage:
    python3 WebRunner.py email-extractor [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --max-depth                 Set depth level to scan


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set http proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    --rnd-ip                    Changes TOR proxy IP for every requests (torcc file required)
    -h, --help                  Show this message
```

![Screenshot 2025-03-19 at 10 26 37 AM](https://github.com/user-attachments/assets/5199e24e-6bf8-4015-9d0d-6d4e49efc3a2)


### RegEx Query module
```
Uses Regx mode

Usage:
    python3 WebRunner.py regx [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --regx                      Set RegEx query to seek into every http response
    --max-depth                 Set depth level to scan


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set http proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    --rnd-ip                    Changes TOR proxy IP for every requests (torcc file required)
    -h, --help                  Show this message
```

![Screenshot 2025-03-19 at 10 30 20 AM](https://github.com/user-attachments/assets/c54a757a-dadd-45c6-8b87-d3edd2b29f67)


### Clone mode
```
Uses Clone mode

Usage:
    python3 WebRunner.py clone [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --name                      Set project name


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set http proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    --rnd-ip                    Changes TOR proxy IP for every requests (torcc file required)
    -h, --help                  Show this message
```

<img width="1515" alt="Screenshot 2025-02-19 at 6 35 49 PM" src="https://github.com/user-attachments/assets/bb1fd46b-96d1-47da-bc0f-7f57d5a7f89f" />

![Screenshot 2025-02-19 at 6 38 17 PM](https://github.com/user-attachments/assets/52b57fe4-0e63-42ce-89db-8659d97b1749)


### Path Traversal mode
When scan a single URL this should ends with ```/```, example ```https://www.example.com/```. You can scan a specific GET parameter in the URL using ```FUZZ``` string, example ```https://www.example.com/image?filename=FUZZ```. When you specify the URL ```https://www.example.com/path/javascript.js``` the URL for scan will be ```https://www.example.com/path/```.

```
Uses Path Traversal mode

Usage:
    python3 WebRunner.py traversal [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --threads                   Set threads
    --max-depth                 Set depth level to scan
    --min-depth                 This can help for traversal payloads, if u dont wanna set ../ and wanna start with ../../../ for payloads
    --os                        Set target Operation System (windows/linux/all)
    --custom-path               Set a custom path to create payloads example path "cgi-bin/", every payload will start as "cgi-bin/../../../etc/passwd"
    --custom-traversal-string   Set a custom traversal string to create payloads example path "....//", every payload will start as ""....//....//etc/passwd"
    --custom-file               Set a custom file disclosure to create payloads example "etc/custom_file.txt", every payload will end as "../../../etc/custom_file.txt". Comma-separated list of items"
    -v,--verbose                Show all requested URLs with the payload used


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set http proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    --rnd-ip                    Changes TOR proxy IP for every requests (torcc file required)
    -h, --help                  Show this message
```

![Screenshot 2025-03-19 at 12 58 47 PM](https://github.com/user-attachments/assets/5edad741-a3a4-4ff6-a6d6-cfca9ed2ad6e)


With ```--custom-path```, ```--custom-traversal-string``` and ```--custom-file``` args.

![Screenshot 2025-03-19 at 1 02 48 PM](https://github.com/user-attachments/assets/dfd6472b-1864-41a0-90bd-bdf314f157c2)


Using TOR project for HTTP Proxy with args ```--proxy http://127.0.0.1:9055``` and random IP with arg ```--rnd-ip```, torrc file is required for this, check TOR section to see the conf for the torrc file.

![Screenshot 2025-03-19 at 1 09 02 PM](https://github.com/user-attachments/assets/b2a92246-7687-4743-85b6-5c9d5371c44f)

Requests from TOR Network
![Screenshot 2025-03-19 at 1 10 48 PM](https://github.com/user-attachments/assets/38f5a85c-1237-4ff3-a7b8-800c70ef6e42)


