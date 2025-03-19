from datetime import datetime
import random, string
from stem import Signal
from stem.control import Controller

class c:
	Black = '\033[30m'
	Red = '\033[31m'
	Green = '\033[32m'
	Orange = '\033[33m'
	Blue = '\033[34m'
	Purple = '\033[35m'
	Reset = '\033[0m'
	Cyan = '\033[36m'
	LightGrey = '\033[37m'
	DarkGrey = '\033[90m'
	LightRed = '\033[91m'
	LightGreen = '\033[92m'
	Yellow = '\033[93m'
	LightBlue = '\033[94m'
	Pink = '\033[95m'
	LightCyan = '\033[96m'

class tor_conf:
	def change_ip():
		try:
			c = Controller.from_port(port=9051)
			c.authenticate()
			c.signal(Signal.NEWNYM)
			c.close()
		except:
			msg.error("You need to set ControlPort 9051 and CookieAuthentication 1 in torrc file")

class msg:
	def error(msg):
		print(f"[{c.Red}*{c.Reset}] {datetime.now()} - {c.Red}{msg}{c.Reset}")

	def info(msg):
		print(f"[{c.Blue}i{c.Reset}] {datetime.now()} - {c.Blue}{msg}{c.Reset}")

	def success(msg):
		print(f"[{c.Green}+{c.Reset}] {datetime.now()} - {c.Green}{msg}{c.Reset}")

	def warning(msg):
		print(f"[{c.Orange}!{c.Reset}] {datetime.now()} - {c.Orange}{msg}{c.Reset}")

	def normal(msg):
		print(f"[{c.Blue}!{c.Reset}] {datetime.now()} - {c.Reset}{msg}{c.Reset}")

class random_data:
	def RandomStrings(self, size=10, chars=string.ascii_lowercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	
class menu:
	def __init__(self,module,user_agent, url, url_file, cookie, tls_validation, follow_redirect, timeout, proxy, depth,regx,os,name,min_depth,threads,verbose,custom_path=[],custom_traversal_strings=[],custom_file=[],change_tor_ip=False):
		self.module = module
		self.user_agent = user_agent
		self.url = url
		self.url_file = url_file
		self.cookie = cookie
		self.tls_validation = tls_validation
		self.follow_redirect = follow_redirect
		self.timeout = timeout
		self.proxy = proxy
		self.depth = depth
		self.regx = regx
		self.os = os
		self.name = name
		self.min_depth = min_depth
		self.threads = threads
		self.verbose = verbose
		self.custom_traversal_strings = custom_traversal_strings
		self.custom_path = custom_path
		self.custom_file = custom_file
		self.change_tor_ip = change_tor_ip

	def print(self):
		self.WebRunnerBanner()
		Message=f"""
- Attack mode: {c.Green}{self.module}{c.Reset}
- User-agent: {c.Green}{self.user_agent}{c.Reset}
- TLS Validation: {c.Green}{self.tls_validation}{c.Reset}
- Follow redirect: {c.Green}{self.follow_redirect}{c.Reset}
- Timeout: {c.Green}{self.timeout}{c.Reset}
- Max Depth: {c.Green}{self.depth}{c.Reset}
- Min Depth: {c.Green}{self.min_depth}{c.Reset}"""

		if self.url:
			Message=f"""{Message}
- Target url: {c.Green}{self.url}{c.Reset}"""
		else:
			Message=f"""{Message}
- Target url file: {c.Green}{self.url_file}{c.Reset}"""

		if self.cookie:
			Message=f"""{Message}
- Cookie: {c.Green}{self.cookie}{c.Reset}"""

		if self.proxy:
			Message=f"""{Message}
- Proxy: {c.Green}{self.proxy}{c.Reset}"""

		if self.proxy and self.change_tor_ip:
			Message=f"""{Message}
- Random TOR IP: {c.Green}{self.change_tor_ip}{c.Reset}"""
			
		if self.os:
			Message=f"""{Message}
- OS: {c.Green}{self.os}{c.Reset}"""

		if self.name:
			Message=f"""{Message}
- Project name: {c.Green}{self.name}{c.Reset}"""

		if self.regx:
			Message=f"""{Message}
- RegEx : {c.Green}{self.regx}{c.Reset}"""
			
		if self.threads and self.module == "traversal":
			Message=f"""{Message}
- Threads : {c.Green}{self.threads}{c.Reset}"""
		
		if self.verbose and self.module == "traversal":
			Message=f"""{Message}
- Verbose : {c.Green}{self.verbose}{c.Reset}"""
			
		if self.custom_path and self.module == "traversal":
			Message=f"""{Message}
- Custom path : {c.Green}{self.custom_path}{c.Reset}"""
			
		if self.custom_traversal_strings and self.module == "traversal":
			Message=f"""{Message}
- Custom traversal strings : {c.Green}{self.custom_traversal_strings}{c.Reset}"""
			
		if self.custom_file and self.module == "traversal":
			Message=f"""{Message}
- Custom file disclosure : {c.Green}{self.custom_file}{c.Reset}"""

			
		print(f"""{Message}
======================================================================================================""")
		


	def WebRunnerBanner(self):
		print(f""" 
██╗    ██╗███████╗██████╗ ██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
 
Coded by:{c.Red} sp34rh34d {c.Reset}
twitter: {c.Red}@spearh34d{c.Reset}
Welcome to WebRunner v2.0 [{c.Green}https://github.com/sp34rh34d/WebRunner{c.Reset}]
======================================================================================================""")
		

	def help_general(self):
		print("""
Global Flags:
    --user-agent                Set user-agent header, 'DirRunner v1.0' by default
    -c, --cookie                Set cookies to use for every HTTP requests
    -k, --no-tls-validation     Skip TLS certificate verification
    -r, --follow-redirect       Follow redirects
    --timeout                   HTTP Timeout (default 10s)
    --proxy                     Set proxy setting for every HTTP request [<https://proxy:port> or <https://username:passwd@proxy:port>]
    --rnd-ip                    Changes TOR proxy IP for every requests (torcc file required)
    -h, --help                  Show this message
""")
		
	def email_extractor_help(self):
		print("""
Uses Email extractor mode

Usage:
    python3 WebRunner.py email-extractor [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --max-depth                 Set depth level to scan
""")
		self.help_general()
	
	def scraping_help(self):
		print("""
Uses Scraping mode

Usage:
    python3 WebRunner.py scraping [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --max-depth                 Set depth level to scan
""")
		self.help_general()
	
	def regx_help(self):
		print("""
Uses Regx mode

Usage:
    python3 WebRunner.py regx [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --regx                      Set RegEx query to seek into every http response
    --max-depth                 Set depth level to scan
""")
		self.help_general()

	def clone_help(self):
		print("""
Uses Clone mode

Usage:
    python3 WebRunner.py clone [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --name                      Set project name
""")
		self.help_general()

	def traversal_help(self):
		print("""
Uses Path Traversal mode

Usage:
    python3 WebRunner.py traversal [flags]
		
Flags:
    --url                       Set target URL single mode
    --url-file                  Load targets URL from txt file
    --threads                   Set threads
    --max-epth                  Set depth level to scan
    --min-depth                 This can help for traversal payloads, if u dont wanna set ../ and wanna start with ../../../ for payloads
    --os                        Set target Operation System (windows/linux/all)
    --custom-path               Set a custom path to create payloads example path "cgi-bin/", every payload will start as "cgi-bin/../../../etc/passwd"
    --custom-traversal-string   Set a custom traversal string to create payloads example path "....//", every payload will start as ""....//....//etc/passwd"
    --custom-file               Set a custom file disclosure to create payloads example "../../mycustomfile.txt", every payload will end as ""mycustomfile.txt. Comma-separated list of items"
    -v,--verbose                Show all requested URLs with the payload used
""")
		self.help_general()