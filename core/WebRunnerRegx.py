from core.core import *
import requests
import validators
import sys
import concurrent.futures
import urllib3
from parsel import Selector
urllib3.disable_warnings()
import re

class REGX_OPTIONS:
	MODULE_NAME="Regx search module"
	TARGET_URL=""
	USER_AGENT=""
	NO_TLS_VALIDATION=True
	COOKIE=""
	HELP=False
	STRING=""
	TIMEOUT=15
	THREADS=10

class REGX_MODULE:

	def main(args):
		print(TerminalColor.Green +'regx search mode selected.'+TerminalColor.Reset)

		REGX_OPTIONS.TARGET_URL=args.url
		REGX_OPTIONS.USER_AGENT=args.user_agent
		REGX_OPTIONS.NO_TLS_VALIDATION=args.no_tls_validation
		REGX_OPTIONS.HELP=args.help
		REGX_OPTIONS.COOKIE=args.cookie
		REGX_OPTIONS.STRING=args.string
		REGX_OPTIONS.TIMEOUT=int(args.timeout)

		if REGX_OPTIONS.HELP:
			REGX_HELP.Help()

		if not REGX_OPTIONS.TARGET_URL or not REGX_OPTIONS.STRING:
			print(TerminalColor.Red +"target url and string are required!"+TerminalColor.Reset)
			print(f"{TerminalColor.Orange}example: python3 WebRunner.py regx -u http://www.domain.com -s 'text-to-find'{TerminalColor.Reset}")
			print(f"{TerminalColor.Orange}Type 'python3 WebRunner.py regx -h' for commands{TerminalColor.Reset}")
			sys.exit()

		if not validators.url(REGX_OPTIONS.TARGET_URL):
			print(TerminalColor.LightRed +"Invalid url!"+TerminalColor.Reset)
			sys.exit()

		Core.Banner()
		REGX_MODULE.Banner()

		try:
			print(f'[{TerminalColor.Blue}!{TerminalColor.Reset}] {TerminalColor.Orange}Checking connection for {REGX_OPTIONS.TARGET_URL}{TerminalColor.Reset}')
			headers={"User-Agent":f"{REGX_OPTIONS.USER_AGENT}","cookie":REGX_OPTIONS.COOKIE}

			res = requests.get(REGX_OPTIONS.TARGET_URL,headers=headers,allow_redirects=False,timeout=REGX_OPTIONS.TIMEOUT,verify=REGX_OPTIONS.NO_TLS_VALIDATION)
			print(f'[{TerminalColor.Green}+{TerminalColor.Reset}]{TerminalColor.Green} Connection OK!{TerminalColor.Reset}')

		except requests.exceptions.Timeout:
			print(f"{TerminalColor.Red}Timeout for {REGX_OPTIONS.TARGET_URL}{TerminalColor.Reset}")
			sys.exit()
		except requests.exceptions.SSLError:
			print(f"{TerminalColor.Red}SSL verification error! add -k arg to ignore.{REGX_OPTIONS.TARGET_URL}{TerminalColor.Reset}")
			print(f"{TerminalColor.Orange}Type 'python3 WebRunner.py regx -h' for commands{TerminalColor.Reset}")
			sys.exit()
		except requests.exceptions.TooManyRedirects:
			print(f"{TerminalColor.Red}Too may redirect for {REGX_OPTIONS.TARGET_URL}{TerminalColor.Reset}")
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

		REGX_TASK.Threads()


	def Banner():
		Message=f"""- Target: {TerminalColor.Green}{REGX_OPTIONS.TARGET_URL}{TerminalColor.Reset}
- Attack mode: {TerminalColor.Green}{REGX_OPTIONS.MODULE_NAME}{TerminalColor.Reset}
- User-agent: {TerminalColor.Green}{REGX_OPTIONS.USER_AGENT}{TerminalColor.Reset}
- String: {TerminalColor.Green}{REGX_OPTIONS.STRING}{TerminalColor.Reset}"""

		if REGX_OPTIONS.COOKIE:
			Message=f"""{Message}
- Cookie: {TerminalColor.Green}{REGX_OPTIONS.COOKIE}{TerminalColor.Reset}"""

		if REGX_OPTIONS.NO_TLS_VALIDATION==False:
			Message=f"""{Message}
- TLS Validation: {TerminalColor.Green}{REGX_OPTIONS.NO_TLS_VALIDATION}{TerminalColor.Reset}"""
		
		print(f"""{Message}
======================================================================================================""")


class REGX_TASK:

	def Threads():
		try:
			headers={"User-Agent":f"{REGX_OPTIONS.USER_AGENT}","cookie":REGX_OPTIONS.COOKIE}
			r=requests.get(REGX_OPTIONS.TARGET_URL,headers=headers,allow_redirects=False,timeout=REGX_OPTIONS.TIMEOUT,verify=REGX_OPTIONS.NO_TLS_VALIDATION)
			selector = Selector(text=r.text)
			tag_a=selector.xpath(".//@href").getall()
			tag_scripts=selector.xpath('.//@src').getall()

			urls=[]

			urls.append(REGX_OPTIONS.TARGET_URL)
		
			for a in tag_a:
				if 'http' in a:
					urls.append(a)
				else:
					build_url=f"{REGX_OPTIONS.TARGET_URL}/{a}"
					build_url2=build_url.replace('//','/')
					urls.append(build_url2.replace(':/','://'))

			for s in tag_scripts:
				if 'http' in s:
					urls.append(s)
				else:
					build_url=f"{REGX_OPTIONS.TARGET_URL}/{s}"
					build_url2=build_url.replace('//','/')
					urls.append(build_url2.replace(':/','://'))

			check_urls=list(dict.fromkeys(urls))

			# print('Looking for RegEx {}'.format(REGX_OPTIONS.STRING))

			print(f'[{TerminalColor.Blue}!{TerminalColor.Reset}] {TerminalColor.Orange}Looking for regx {REGX_OPTIONS.STRING} ...{TerminalColor.Reset}')
			with concurrent.futures.ThreadPoolExecutor(max_workers=int(REGX_OPTIONS.THREADS)) as executor:
				future_to_url = {executor.submit(REGX_TASK.Search,url): url for url in check_urls}

				for future in concurrent.futures.as_completed(future_to_url):
					future.result()

		except KeyboardInterrupt:
			print(f'{TerminalColor.Red}Process terminated, Ctrl C!{TerminalColor.Reset}                              ')
			sys.exit()
		except:
			pass

	def Search(URL=""):
		try:
			headers={"User-Agent":f"{REGX_OPTIONS.USER_AGENT}","cookie":REGX_OPTIONS.COOKIE}
			r=requests.get(URL,headers=headers,allow_redirects=False,timeout=REGX_OPTIONS.TIMEOUT,verify=REGX_OPTIONS.NO_TLS_VALIDATION)
			string = re.findall(REGX_OPTIONS.STRING,r.text)

			if string:
				print(f"{TerminalColor.Green}Match on{TerminalColor.Reset}: {TerminalColor.Blue}{URL}{TerminalColor.Reset}")
				for s in string:
					print(f"[{TerminalColor.Green}+{TerminalColor.Reset}] {TerminalColor.Green}{s}{TerminalColor.Reset}")

		except KeyboardInterrupt:
			print(f'{TerminalColor.Red}Process terminated, Ctrl C!{TerminalColor.Reset}                              ')
			sys.exit()
		except:
			pass
		
		
class REGX_HELP:
		def Help():
			print("""Regx search - Help menu

Uses Regx search mode

Usage:
  python3 WebRunner.py regx [args]

Args
	-u, --url                set target url (required)
	-s, --string             build your own regx search (required)
	-a, --user-agent         set user agent, by default (WebRunner v1.0)
	-c, --cookie             set cookie for http requests
	-t, --threads            set threads
	-k, --no-tls-validation  not ssl check
	    --timeout            set timeout for http requests
	-h, --help               show this message

Examples:

	regx search looking for THM{T3ST_M3SS4G3}
	python3 WebRunner.py regx -u https://www.domain.com -s "THM[A-Z0-9_{}]{6,}"
				""")
			sys.exit()









