from core.core import *
import requests
import validators
import sys
import concurrent.futures
import urllib3
from parsel import Selector
urllib3.disable_warnings()

class URL_OPTIONS:
	MODULE_NAME="URL extractor"
	TARGET_URL=""
	THREADS=10
	USER_AGENT=""
	NO_TLS_VALIDATION=True
	COOKIE=""
	HELP=False
	TIMEOUT=15
	URLS=[]

class URL_MODULE:
	def main(args):
		print(TerminalColor.Green +'url extractor mode selected.'+TerminalColor.Reset)

		URL_OPTIONS.TARGET_URL=args.url
		URL_OPTIONS.THREADS=args.threads
		URL_OPTIONS.USER_AGENT=args.user_agent
		URL_OPTIONS.NO_TLS_VALIDATION=args.no_tls_validation
		URL_OPTIONS.HELP=args.help
		URL_OPTIONS.COOKIE=args.cookie
		URL_OPTIONS.TIMEOUT=int(args.timeout)

		if URL_OPTIONS.HELP:
			URL_HELP.Help()

		if not URL_OPTIONS.TARGET_URL:
			print(TerminalColor.Red +"target url is required!"+TerminalColor.Reset)
			print(f"{TerminalColor.Orange}example 'python3 WebRunner.py url -u http://www.domain.com'{TerminalColor.Reset}")
			print(f"{TerminalColor.Orange}Type 'python3 WebRunner.py url -h' for commands{TerminalColor.Reset}")
			sys.exit()

		if not validators.url(URL_OPTIONS.TARGET_URL):
			print(TerminalColor.LightRed +"Invalid url!"+TerminalColor.Reset)
			sys.exit()

		Core.Banner()
		URL_MODULE.Banner()

		try:
			print(f'[{TerminalColor.Blue}!{TerminalColor.Reset}] {TerminalColor.Orange}Checking connection for {URL_OPTIONS.TARGET_URL}{TerminalColor.Reset}')
			headers={"User-Agent":f"{URL_OPTIONS.USER_AGENT}","cookie":URL_OPTIONS.COOKIE}

			res = requests.get(URL_OPTIONS.TARGET_URL,headers=headers,allow_redirects=False,timeout=URL_OPTIONS.TIMEOUT,verify=URL_OPTIONS.NO_TLS_VALIDATION)
			print(f'[{TerminalColor.Green}+{TerminalColor.Reset}]{TerminalColor.Green} Connection OK!{TerminalColor.Reset}')

		except requests.exceptions.Timeout:
			print(f"{TerminalColor.Red}Timeout for {URL_OPTIONS.TARGET_URL}{TerminalColor.Reset}")
			sys.exit()
		except requests.exceptions.SSLError:
			print(f"{TerminalColor.Red}SSL verification error! add -k arg to ignore.{URL_OPTIONS.TARGET_URL}{TerminalColor.Reset}")
			print(f"{TerminalColor.Orange}Type 'python3 WebRunner.py url -h' for commands{TerminalColor.Reset}")
			sys.exit()
		except requests.exceptions.TooManyRedirects:
			print(f"{TerminalColor.Red}Too may redirect for {URL_OPTIONS.TARGET_URL}{TerminalColor.Reset}")
			sys.exit()
		except requests.exceptions.ConnectionError as e:
			print(f"{TerminalColor.Red}Connection error: {e}{TerminalColor.Reset}")
			sys.exit()
		except KeyboardInterrupt:
			print(f'{TerminalColor.Red}Process terminated, Ctrl C!{TerminalColor.Reset}                              ')
			sys.exit()
		except requests.exceptions.RequestException as e:
			raise SystemExit(e)
			sys.exit()

		URL_TASK.Threads()


	def Banner():
		Message=f"""- Target: {TerminalColor.Green}{URL_OPTIONS.TARGET_URL}{TerminalColor.Reset}
- Attack mode: {TerminalColor.Green}{URL_OPTIONS.MODULE_NAME}{TerminalColor.Reset}
- User-agent: {TerminalColor.Green}{URL_OPTIONS.USER_AGENT}{TerminalColor.Reset}"""

		if URL_OPTIONS.COOKIE:
			Message=f"""{Message}
- Cookie: {TerminalColor.Green}{URL_OPTIONS.COOKIE}{TerminalColor.Reset}"""

		if URL_OPTIONS.NO_TLS_VALIDATION==False:
			Message=f"""{Message}
- TLS Validation: {TerminalColor.Green}{URL_OPTIONS.NO_TLS_VALIDATION}{TerminalColor.Reset}"""
		
		print(f"""{Message}
======================================================================================================""")


class URL_TASK:

	def Threads():
		try:
			headers={"User-Agent":f"{URL_OPTIONS.USER_AGENT}","cookie":URL_OPTIONS.COOKIE}
			r=requests.get(URL_OPTIONS.TARGET_URL,headers=headers,allow_redirects=False,timeout=URL_OPTIONS.TIMEOUT,verify=URL_OPTIONS.NO_TLS_VALIDATION)
			selector = Selector(text=r.text)
			tag_a=selector.xpath(".//@href").getall()
			tag_scripts=selector.xpath('.//@src').getall()

			urls=[]
		
			for a in tag_a:
				if 'http' in a:
					urls.append(a)
					URL_OPTIONS.URLS.append(a)
				else:
					build_url=f"{URL_OPTIONS.TARGET_URL}/{a}"
					build_url2=build_url.replace('//','/')
					urls.append(build_url2.replace(':/','://'))
					URL_OPTIONS.URLS.append(build_url2.replace(':/','://'))

			for s in tag_scripts:
				if 'http' in s:
					urls.append(s)
					URL_OPTIONS.URLS.append(s)
				else:
					build_url=f"{URL_OPTIONS.TARGET_URL}/{s}"
					build_url2=build_url.replace('//','/')
					urls.append(build_url2.replace(':/','://'))
					URL_OPTIONS.URLS.append(build_url2.replace(':/','://'))

			check_urls=list(dict.fromkeys(urls))

			print(f"[{TerminalColor.Blue}!{TerminalColor.Reset}] {TerminalColor.Orange}Looking for urls...{TerminalColor.Reset}")
			with concurrent.futures.ThreadPoolExecutor(max_workers=int(URL_OPTIONS.THREADS)) as executor:
				future_to_url = {executor.submit(URL_TASK.ExtracURLs,url): url for url in check_urls}

				for future in concurrent.futures.as_completed(future_to_url):
					future.result()

			for url in list(dict.fromkeys(URL_OPTIONS.URLS)):
				if validators.url(url):
					print(f"[{TerminalColor.Green}+{TerminalColor.Reset}] {TerminalColor.Green}{url}{TerminalColor.Reset}")

		except KeyboardInterrupt:
			print(f'{TerminalColor.Red}Process terminated, Ctrl C!{TerminalColor.Reset}                              ')
			sys.exit()
		except:
			pass

	def ExtracURLs(URL=""):

		try:
			headers={"User-Agent":f"{URL_OPTIONS.USER_AGENT}","cookie":URL_OPTIONS.COOKIE}
			r=requests.get(URL,headers=headers,allow_redirects=False,timeout=URL_OPTIONS.TIMEOUT,verify=URL_OPTIONS.NO_TLS_VALIDATION)
			selector = Selector(text=r.text)
			tag_a=selector.xpath(".//@href").getall()
			tag_scripts=selector.xpath('.//@src').getall()
		
			for a in tag_a:
				if 'http' in a:
					URL_OPTIONS.URLS.append(a)
				else:
					build_url=f"{URL_OPTIONS.TARGET_URL}/{a}"
					build_url2=build_url.replace('//','/')
					URL_OPTIONS.URLS.append(build_url2.replace(':/','://'))

			for s in tag_scripts:
				if 'http' in s:
					URL_OPTIONS.URLS.append(s)
				else:
					build_url=f"{URL_OPTIONS.TARGET_URL}{s}"
					build_url2=build_url.replace('//','/')
					URL_OPTIONS.URLS.append(build_url2.replace(':/','://'))

		except KeyboardInterrupt:
			print(f'{TerminalColor.Red}Process terminated, Ctrl C!{TerminalColor.Reset}                              ')
			sys.exit()
			
		except:
			pass


class URL_HELP:
		def Help():
			print("""URL Extractor - Help menu

Uses URL Extractor mode

Usage:
  python3 WebRunner.py url [args]

Args
	-u, --url                set target url (required)
	-a, --user-agent         set user agent, by default (WebRunner v1.0)
	-c, --cookie             set cookie for http requests
	-t, --threads            set threads
	-k, --no-tls-validation  not ssl check
	    --timeout            set timeout for http requests
	-h, --help               show this message

Examples:

	url extractor
	python3 WebRunner.py url -u https://www.domain.com
				""")
			sys.exit()
		



