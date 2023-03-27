class HELP_MODULE:
	def main():
		print("""

Usage:
    python3 WebRunner.py [module] [args]

Modules
	url         Extract url from a website
	email       Extract emails from a website
	regx        Allows you to create your own searches using RegEx on a website
	clone       Allow you make a website copy to local folder (usefull for phishing labs) # educational purposes only
	help        Help about any command


Examples:
	url extractor
	use: python3 WebRunner.py url -u https://www.domain.com

	email extractor
	use: python3 WebRunner.py email -u https://www.domain.com

	RegEx query example to extract THM{T3ST_M3SS4G3}
	use: python3 WebRunner.py regx -u https://www.domain.com -s "THM[A-Z0-9_{}]{6,}"

	Clone a website
	use: python3 WebRunner.py clone -u https://www.domain.com -n mysite

	show help menu for a module
	use: python3 WebRunner.py url -h

""")