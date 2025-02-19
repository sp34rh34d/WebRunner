#!/usr/bin/env python3

import requests,sys
from urllib.parse import urlparse, parse_qs,urlunparse,urlencode
from parsel import Selector
import concurrent.futures
import validators
from core import *
import urllib3
urllib3.disable_warnings()

class path_traversal_options:
	path_traversal_commands_path="wordlist/path_traversal.txt"
	target_url=""
	urls_detected=[]
	urls_procesed=[]
	threads=50

class path_traversal_module:

	def main(args):
		if args.url=="":
			print("target url required")
			sys.exit()

		path_traversal_options.target_url=args.url

		try:
			path_traversal_module.run_base_url()
			path_traversal_module.ExtracURLs(path_traversal_options.target_url)
			check_urls=list(dict.fromkeys(path_traversal_options.urls_detected))

			with concurrent.futures.ThreadPoolExecutor(max_workers=int(path_traversal_options.threads)) as executor:
				future_to_url = {executor.submit(path_traversal_module.ExtracURLs,url): url for url in check_urls}

				for future in concurrent.futures.as_completed(future_to_url):
					future.result()

			urls1=list(dict.fromkeys(path_traversal_options.urls_detected))
			for x in urls1:
				path_traversal_module.detecting_path_traversal(x)
			
		except KeyboardInterrupt:
			sys.exit()
#		except:
#			pass

	def ExtracURLs(URL=""):

		try:
			headers={"User-Agent":"sp34rh34d"}
			r=requests.get(URL,headers=headers)
			selector = Selector(text=r.text)
			tag_a=selector.xpath(".//@href").getall()
			tag_scripts=selector.xpath('.//@src').getall()
		
			for a in tag_a:
				if 'http' in a:
					path_traversal_options.urls_detected.append(a)
				else:
					build_url=f"{path_traversal_options.target_url}/{a}"
					build_url2=build_url.replace('//','/')
					path_traversal_options.urls_detected.append(build_url2.replace(':/','://'))

			for s in tag_scripts:
				if 'http' in s:
					path_traversal_options.urls_detected.append(s)
				else:
					build_url=f"{path_traversal_options.target_url}{s}"
					build_url2=build_url.replace('//','/')
					path_traversal_options.urls_detected.append(build_url2.replace(':/','://'))

		except KeyboardInterrupt:
			sys.exit()
			
		except:
			pass

	def detect_get_parameters(url):
		print("checking for parameters on url...",url)
		parsed_url = urlparse(url)
		parameters = parse_qs(parsed_url.query)
		print("done!")
		return parameters

	def get_url_context(url):
		parsed_url = urlparse(url)
		return f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

	def change_get_parameter(url,parameter_name,new_value):
		parsed_url = urlparse(url)
		parameters = parsed_url.query.split('&')

		updated_parameters = []
		parameter_modified = False

		for param in parameters:
			name, value = param.split('=')
			if name == parameter_name:
				updated_parameters.append(f"{name}={new_value}")
				parameter_modified = True
			else:
				updated_parameters.append(param)

		if not parameter_modified:
			updated_parameters.append(f"{parameter_name}={new_value}")

		modified_url = urlunparse((
			parsed_url.scheme,
			parsed_url.netloc,
			parsed_url.path,
			parsed_url.params,
			'&'.join(updated_parameters),
			parsed_url.fragment
		))

		return modified_url

	def check_site(url):
		new_parsed_url=urlparse(url)
		target_parsed_url=urlparse(path_traversal_options.target_url)
		if new_parsed_url.netloc==target_parsed_url.netloc:
			return True
		else:
			return False

	def run(url,key,payload="",response_length=0):
		try:
			new_url=path_traversal_module.change_get_parameter(url,key,payload)
			headers={"User-Agent":"sp34rh34d"}
			new_request=requests.get(new_url,timeout=5,headers=headers,verify=False)
			new_response_code=new_request.status_code
			new_response_length=0

			for key,value in new_request.headers.items():
				if key =='Content-Length':
					new_response_length=value

			if new_response_code==200 and new_response_length != response_length:
				print(f"{c.Red}path traversal detected{c.Reset}, payload:", new_url)
		except:
			pass

	def run2(url,payload="",response_length=0):
		try:
			headers={"User-Agent":"sp34rh34d"}
			new_request=requests.get(url,timeout=5,headers=headers,verify=False)
			new_response_code=new_request.status_code
			new_response_length=0

			for key,value in new_request.headers.items():
				if key =='Content-Length':
					new_response_length=value

			if new_response_code==200 and new_response_length != response_length:
				print(f"{c.Red}path traversal detected{c.Reset}, payload:", url)
		except:
			pass


	def run_base_url():
		parsed_url = urlparse(path_traversal_options.target_url)
		url_context=f"{parsed_url.scheme}://{parsed_url.netloc}/"

		headers={"User-Agent":"sp34rh34d"}
		r=requests.get(url_context,timeout=5,headers=headers,verify=False)
		response_length=0

		for key,value in r.headers.items():
			if key =='Content-Length':
				response_length=value

		try:
			print("processing:",url_context)
			with concurrent.futures.ThreadPoolExecutor(max_workers=int(path_traversal_options.threads)) as executor:
				f = open(path_traversal_options.path_traversal_commands_path,'r')
				future_to_url = {executor.submit(path_traversal_module.run2(url_context,payload,response_length)): payload for payload in f.read().split("\n")}

				for future in concurrent.futures.as_completed(future_to_url):
					future.result()
		except:
			pass

	def detecting_path_traversal(url):
		if not validators.url(url):
			return 0

		url_context=path_traversal_module.get_url_context(url)

		if url_context in path_traversal_options.urls_procesed:
			pass
		elif not path_traversal_module.check_site(url):
			pass
		else:
			parameters=path_traversal_module.detect_get_parameters(url)
			if len(parameters) > 0 :
				print("processing url:",url)
				headers={"User-Agent":"sp34rh34d"}
				r=requests.get(url,timeout=5,headers=headers,verify=False)

				response_length=0
				for key,value in r.headers.items():
					if key =='Content-Length':
			 			response_length=value

				print("parameters detected:",len(parameters))
				for key in parameters:
					print("testing parameter:",key)

					try:
						with concurrent.futures.ThreadPoolExecutor(max_workers=int(path_traversal_options.threads)) as executor:
							f = open(path_traversal_options.path_traversal_commands_path,'r')
							future_to_url = {executor.submit(path_traversal_module.run(url,key,payload,response_length)): payload for payload in f.read().split("\n")}

							for future in concurrent.futures.as_completed(future_to_url):
								future.result()
					except:
						pass

		path_traversal_options.urls_procesed.append(url_context)





