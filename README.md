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
* Bypass 403 Scanner
* SQLi Scanner

### Scraping module
```
Uses Scraping mode

Usage:
    python3 WebRunner.py scraping [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --depth                     Set depth level to scan


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    -h, --help                  Show this message
```

<img width="1536" alt="Screenshot 2025-02-19 at 6 22 17 PM" src="https://github.com/user-attachments/assets/af2b126f-4a28-4b2a-9184-98bd805615c0" />


### Email extractor module
```
Uses Email extractor mode

Usage:
    python3 WebRunner.py email-extractor [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --depth                     Set depth level to scan


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    -h, --help                  Show this message
```

<img width="1582" alt="Screenshot 2025-02-19 at 6 25 34 PM" src="https://github.com/user-attachments/assets/f457154f-60cc-4437-8864-0a215c15b30a" />

### RegEx Query module
```
Uses Regx mode

Usage:
    python3 WebRunner.py regx [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --regx                      Set RegEx query to seek into every http response
    --depth                     Set depth level to scan


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    -h, --help                  Show this message
```

<img width="1572" alt="Screenshot 2025-02-19 at 6 29 15 PM" src="https://github.com/user-attachments/assets/894f6624-7f7c-49da-a03a-4e196db6a105" />

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
    --proxy                     Set proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    -h, --help                  Show this message
```

<img width="1515" alt="Screenshot 2025-02-19 at 6 35 49 PM" src="https://github.com/user-attachments/assets/bb1fd46b-96d1-47da-bc0f-7f57d5a7f89f" />

![Screenshot 2025-02-19 at 6 38 17 PM](https://github.com/user-attachments/assets/52b57fe4-0e63-42ce-89db-8659d97b1749)


### Path Traversal mode
When scan a single URL this should ends with ```/```, example ```https://www.example.com/```. You can scan an specific GET parameter in the URL using ```FUZZ``` string, example ```https://www.example.com/image?filename=FUZZ```. When you specify the URL ```https://www.example.com/path/javascript.js``` the URL for scan will be ```https://www.example.com/path/```.

```
Uses Path Traversal mode

Usage:
    python3 WebRunner.py traversal [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --threads                   Set threads
    --depth                     Set depth level to scan
    --min-depth                 This can help for traversal payloads, if u dont wanna set ../ and wanna start with ../../../ for payloads
    --os                        Set target Operation System (windows/linux/all)
    --custom-path               Set a custom path to create payloads example path "cgi-bin/", every payload will start as "cgi-bin/../../../etc/passwd"
    --custom-traversal-string   Set a custom traversal string to create payloads example path "....//", every payload will start as ""....//....//etc/passwd"
    -v,--verbose                Show all requested URLs with the payload used


Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    -h, --help                  Show this message
```

<img width="1341" alt="Screenshot 2025-02-19 at 6 53 06 PM" src="https://github.com/user-attachments/assets/3b6f99ac-d59d-4be7-83cb-8a116c9f684f" />

With ```--custom-path``` and ```--custom-traversal-string``` args.

<img width="1673" alt="Screenshot 2025-02-19 at 6 55 54 PM" src="https://github.com/user-attachments/assets/976ef623-48bc-4094-9682-1fa9bd2278ed" />
