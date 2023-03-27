import pywebcopy 
from core.core import *
import string
import sys
import validators
import random

class CLONE_OPTIONS:
	MODULE_NAME="Clone module"
	TARGET_URL=""
	FOLDER="projects/"
	NAME=""
	HELP=False

class CLONE_MODULE:

	def main(args):
		print(TerminalColor.Green +'clone mode selected.'+TerminalColor.Reset)

		CLONE_OPTIONS.TARGET_URL=args.url
		CLONE_OPTIONS.FOLDER=args.folder
		CLONE_OPTIONS.NAME=args.name
		CLONE_OPTIONS.HELP=args.help

		Core.Banner()
		CLONE_MODULE.Banner()

		if CLONE_OPTIONS.HELP:
			CLONE_HELP.Help()

		if not CLONE_OPTIONS.NAME:
			CLONE_OPTIONS.NAME=CLONE_MODULE.RandomStrings()

		if not CLONE_OPTIONS.FOLDER:
			CLONE_OPTIONS.FOLDER="projects/"

		if not CLONE_OPTIONS.TARGET_URL:
			print(f'{TerminalColor.Red}target url is requered{TerminalColor.Reset}')
			sys.exit()

		if not validators.url(CLONE_OPTIONS.TARGET_URL):
			print(TerminalColor.LightRed +"Invalid url!"+TerminalColor.Reset)
			sys.exit()


		pywebcopy.save_website(
			url=CLONE_OPTIONS.TARGET_URL,
			project_folder=CLONE_OPTIONS.FOLDER,
			project_name=CLONE_OPTIONS.NAME,
			bypass_robots=True,
			debug=True,
			open_in_browser=False,
			delay=None,
			threaded=False,
		)

	def Banner():
		print(f"""- Target: {TerminalColor.Green}{CLONE_OPTIONS.TARGET_URL}{TerminalColor.Reset}
- Attack mode: {TerminalColor.Green}{CLONE_OPTIONS.MODULE_NAME}{TerminalColor.Reset}
- Project name: {TerminalColor.Green}{CLONE_OPTIONS.NAME}{TerminalColor.Reset}
- Destination folder: {TerminalColor.Green}{CLONE_OPTIONS.FOLDER}{TerminalColor.Reset}
======================================================================================================""")


	def RandomStrings(size=10, chars=string.ascii_lowercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))

class CLONE_HELP:
		def Help():
			print("""Clone websites - Help menu

Uses Clone websites mode

Usage:
  python3 WebRunner.py clone [args]

Args
	-u, --url                set target url (required)
	-f, --folder             set destination folder 
	-n, --cookie             set project name 
	-h, --help               show this message

Examples:

	clone websites
	python3 WebRunner.py clone -u https://www.domain.com -n mysite
				""")
			sys.exit()