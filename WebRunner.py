#!/usr/bin/env python3

import argparse
from core.traversal import *
from core.extractor import url_extractor, email_extractor, regx, clone
from core.core import menu

parser = argparse.ArgumentParser(add_help=False)
### attack mode
parser.add_argument('mode',help='Set attack mode (traversal,scraping,regx,email-extractor)')

### General args
parser.add_argument('--url',help='Set a single target URL')
parser.add_argument('--url-file',help='Set txt file with multiple targets URL')
parser.add_argument('--user-agent',help='Set user agent header for every http request',default="WebRunner v2.0 agent")
parser.add_argument('-k','--no-tls-validation',action='store_false')
parser.add_argument('-r','--follow-redirect',action='store_true')
parser.add_argument('-c','--cookie',help='Set cookies to use for the requests')
parser.add_argument('--timeout',default=int(10),help='Time each thread waits between requests (10s by default)')
parser.add_argument('--proxy',help='Set proxy setting for all requests, use <http://proxy:port> or <http://username:passwd@proxy:port>')
parser.add_argument('--rnd-ip',action='store_true',help="Changes TOR proxy IP for every requests")
parser.add_argument('--max-depth',help='this can help for traversal payloads or scrapping/crawling',default=int(3))
parser.add_argument('-h','--help',action='store_true',help="")

### args for traversal
parser.add_argument('--os',help='Set target Operation System (windows/linux/all)',default="linux")
parser.add_argument('-t','--threads',default=int(10),help='Set threads')
parser.add_argument('--min-depth',help='this can help for traversal payloads, if u dont wanna set ../ and wanna start with ../../../ for payloads',default=int(1))
parser.add_argument('--custom-path',help='Set a custom path to create payloads example path "cgi-bin/", every payload will start as "cgi-bin/../../../etc/passwd')
parser.add_argument('--custom-traversal-string',help='Set a custom traversal string to create payloads example path "....//", every payload will start as ""....//....//etc/passwd. Comma-separated list of items')
parser.add_argument('--custom-file',help='Set a custom file disclosure to create payloads example "etc/custom_file.txt", every payload will end as "../../../etc/custom_file.txt". Comma-separated list of items"')
parser.add_argument('-v','--verbose',action='store_true',help='Show all requested URLs with the payload used ')

### args for clone mode
parser.add_argument('-n','--name',help='Set project name for clone module.')

### arg for regx mode
parser.add_argument('--regx',help='Set regx string to search into target website.')


args = parser.parse_args()
custom_path_list = args.custom_path.split(',') if args.custom_path else []
custom_traversal_strings_list = args.custom_traversal_string.split(',') if args.custom_traversal_string else []
custom_file = args.custom_file.split(',') if args.custom_file else []

ATTACK_MODE=args.mode
help_menu = menu(args.mode,args.user_agent,args.url,args.url_file,args.cookie,args.no_tls_validation,args.follow_redirect,args.timeout,args.proxy,args.max_depth,args.regx,args.os,args.name,args.min_depth,args.threads,args.verbose,custom_path_list,custom_traversal_strings_list,custom_file,args.rnd_ip)

if ATTACK_MODE=='traversal':
	if args.help:
		help_menu.traversal_help()
		sys.exit()
	help_menu.print()
	traversal_mode = traversal(args.url,args.url_file,args.timeout,args.follow_redirect,args.cookie,args.user_agent,args.no_tls_validation,args.proxy,args.max_depth,args.os,args.threads,args.min_depth,args.verbose,custom_path_list,custom_traversal_strings_list,custom_file,args.rnd_ip)
	traversal_mode.scanner()

elif ATTACK_MODE=='scraping':
	if args.help:
		help_menu.scraping_help()
		sys.exit()
	help_menu.print()
	scraping = url_extractor(args.url,args.url_file,args.timeout,args.follow_redirect, args.cookie, args.user_agent,args.no_tls_validation,args.proxy,args.max_depth,args.rnd_ip)
	scraping.scanner()

elif ATTACK_MODE=='email-extractor':
	if args.help:
		help_menu.email_extractor_help()
		sys.exit()
	help_menu.print()
	extractor = email_extractor(args.url,args.url_file,args.timeout,args.follow_redirect, args.cookie, args.user_agent,args.no_tls_validation,args.proxy,args.max_depth,args.rnd_ip)
	extractor.scanner()

elif ATTACK_MODE=='regx':
	if args.help:
		help_menu.regx_help()
		sys.exit()
	help_menu.print()
	regx_seek = regx(args.url,args.url_file,args.timeout,args.follow_redirect, args.cookie, args.user_agent,args.no_tls_validation,args.proxy,args.max_depth,args.regx,args.rnd_ip)
	regx_seek.scanner()

elif ATTACK_MODE=='clone':
	if args.help:
		help_menu.clone_help()
		sys.exit()
	help_menu.print()
	clone_mode = clone(args.url,args.timeout,args.user_agent,args.no_tls_validation,args.proxy,args.name,args.rnd_ip)
	clone_mode.scanner()

else:
	msg.error("Attack mode is required! You can use [ scraping | email-extractor | regx | clone | traversal ]")