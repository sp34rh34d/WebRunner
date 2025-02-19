from core.validate import formats
from core.core import msg, random_data, c
from pathlib import Path
import sys, requests, re, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

class url_extractor:
    def __init__(self,target_url,target_url_file,timeout,follow_redirect, cookie, user_agent, tls_validation,proxy_setting, depth):
        self.target_url = target_url
        self.target_url_file = target_url_file
        self.timeout = int(timeout)
        self.follow_redirect = follow_redirect
        self.cookie = cookie
        self.user_agent = user_agent
        self.tls_validation = tls_validation
        self.proxy_setting = proxy_setting
        self.max_depth = int(depth)
        self.urls = []
        self.urls_js = []
        self.urls_img = []

    def scanner(self):
        try:
            single_or_multiple_url = 0
            if self.target_url:
                msg.info(f"starting single scan for url {self.target_url}")
                single_or_multiple_url = 0
            elif self.target_url_file:
                msg.info(f"starting scan for url into the file {self.target_url_file}")
                single_or_multiple_url = 1
            else:
                msg.error("no url detected, use --url or --url-file args")
                sys.exit()

            if single_or_multiple_url == 1 :
                file = Path(self.target_url_file)
                if not file.is_file():
                    msg.error(f"file {self.target_url_file} not found!")
                    sys.exit()
                urls_from_file = open(self.target_url_file,"r").read()
                for url in urls_from_file.split("\n"):
                    if formats.validate_url(url):
                        self.crawl(url,0)
                msg.info("done!")
                
            else:
                if not formats.validate_url(self.target_url):
                    msg.error(f"url {self.target_url} is invalid!")
                    sys.exit()

                if self.is_alive(self.target_url):
                    msg.info(f"Connection success for url {self.target_url}")
                    self.crawl(self.target_url,0)
                    msg.info("done!")
                    r = random_data()
                    filename = "urls_detected_"+ r.RandomStrings() +".txt"
                    with open(filename ,"a") as f:
                        for url in self.urls:
                            f.write(url+"\n")
                        for url in self.urls_js:
                            f.write(url+"\n")
                        for url in self.urls_img:
                            f.write(url+"\n")

                    msg.success(f"file {filename} created!")
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

    def is_alive(self,target_url):
        try:
            headers = {
                "User-Agent" : self.user_agent,
                "cookie" : self.cookie
            }

            proxy_setting = {
                "http" : None,
                "https" : None
            }

            if self.proxy_setting:
                proxy_setting = {
                    "http" : self.proxy_setting,
                    "https" : self.proxy_setting
                }
            res = requests.get(target_url,headers=headers,allow_redirects=self.follow_redirect, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)
            return True
        except Exception as e:
            msg.error(e)
            return False
        
        
    def crawl(self,url, depth, visited_pages=None, visited_js=None, visited_img=None):
        try:
            if visited_pages is None:
                visited_pages = set()
            if visited_js is None:
                visited_js = set()
            if visited_img is None:
                visited_img = set()
        
            if int(depth) > int(self.max_depth) or url in visited_pages or not formats.validate_url(url) or url in self.urls:
                return
            
            visited_pages.add(url)
            self.urls.append(url)
            indent = " " * (depth * 2)
            msg.warning(f"{indent}Level {depth}: {url}")
            
            try:
                headers = {
                    "User-Agent" : self.user_agent,
                    "cookie" : self.cookie
                }

                proxy_setting = {
                    "http" : None,
                    "https" : None
                }

                if self.proxy_setting:
                    proxy_setting = {
                        "http" : self.proxy_setting,
                        "https" : self.proxy_setting
                    }

                response = requests.get(url,headers=headers,allow_redirects=self.follow_redirect, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)
            except Exception as e:
                msg.error(" " * (depth * 2) + f"Error fetching {url}: {e}")
                return
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                new_url = urljoin(url, link['href'])
                self.crawl(new_url, depth + 1, visited_pages)

            for script in soup.find_all('script', src=True):
                js_url = urljoin(url, script['src'])
                if js_url not in visited_js:
                    visited_js.add(js_url)
                    self.urls_js.append(js_url)
                    msg.info(f"{indent}  [{c.Orange}JS{c.Blue}] {js_url}")
        
            for img in soup.find_all('img', src=True):
                img_url = urljoin(url, img['src'])
                if img_url not in visited_img:
                    visited_img.add(img_url)
                    self.urls_img.append(img_url)
                    msg.info(f"{indent}  [{c.Orange}IMG{c.Blue}] {img_url}")
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

class email_extractor:
    def __init__(self,target_url,target_url_file,timeout,follow_redirect, cookie, user_agent, tls_validation,proxy_setting, depth):
        self.target_url = target_url
        self.target_url_file = target_url_file
        self.timeout = int(timeout)
        self.follow_redirect = follow_redirect
        self.cookie = cookie
        self.user_agent = user_agent
        self.tls_validation = tls_validation
        self.proxy_setting = proxy_setting
        self.max_depth = int(depth)
        self.emails = []
        self.urls = []

    def is_alive(self,target_url):
        try:
            headers = {
                "User-Agent" : self.user_agent,
                "cookie" : self.cookie
            }

            proxy_setting = {
                "http" : None,
                "https" : None
            }

            if self.proxy_setting:
                proxy_setting = {
                    "http" : self.proxy_setting,
                    "https" : self.proxy_setting
                }
            res = requests.get(target_url,headers=headers,allow_redirects=self.follow_redirect, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)
            return True
        except Exception as e:
            msg.error(e)
            return False
        
    def scanner(self):
        try:
            single_or_multiple_url = 0
            if self.target_url:
                msg.info(f"starting single scan for url {self.target_url}")
                single_or_multiple_url = 0
            elif self.target_url_file:
                msg.info(f"starting scan for url into the file {self.target_url_file}")
                single_or_multiple_url = 1
            else:
                msg.error("no url detected, use --url or --url-file args")
                sys.exit()

            if single_or_multiple_url == 1 :
                file = Path(self.target_url_file)
                if not file.is_file():
                    msg.error(f"file {self.target_url_file} not found!")
                    sys.exit()
                urls_from_file = open(self.target_url_file,"r").read()
                for url in urls_from_file.split("\n"):
                    if formats.validate_url(url):
                        self.crawl(url,0)
                msg.info("done!")
                
            else:
                if not formats.validate_url(self.target_url):
                    msg.error(f"url {self.target_url} is invalid!")
                    sys.exit()

                if self.is_alive(self.target_url):
                    msg.info(f"Connection success for url {self.target_url}")
                    self.crawl(self.target_url,0)
                    msg.info("done!")
                    r = random_data()
                    filename = "extracted_emails_"+ r.RandomStrings() +".txt"
                    with open(filename ,"a") as f:
                        for email in self.emails:
                            f.write(email+"\n")
                    msg.success(f"file {filename} created!")
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

    def crawl(self,url, depth, visited_pages=None, visited_js=None, visited_img=None):
        try:
            if visited_pages is None:
                visited_pages = set()
            if visited_js is None:
                visited_js = set()
        
            if int(depth) > int(self.max_depth) or url in visited_pages or not formats.validate_url(url) or url in self.urls:
                return
            
            visited_pages.add(url)
            self.urls.append(url)
            try:
                headers = {
                    "User-Agent" : self.user_agent,
                    "cookie" : self.cookie
                }

                proxy_setting = {
                    "http" : None,
                    "https" : None
                }

                if self.proxy_setting:
                    proxy_setting = {
                        "http" : self.proxy_setting,
                        "https" : self.proxy_setting
                    }

                response = requests.get(url,headers=headers,allow_redirects=self.follow_redirect, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)
                detected_emails = formats.validate_email(response.text)
                if detected_emails:
                    msg.warning(f"url: {url} contains:")
                    msg.success(detected_emails)
                    for email in detected_emails:
                        if email not in self.emails:
                            self.emails.append(email)
                            
            except Exception as e:
                msg.error(" " * (depth * 2) + f"Error fetching {url}: {e}")
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                new_url = urljoin(url, link['href'])
                self.crawl(new_url, depth + 1, visited_pages)

            for script in soup.find_all('script', src=True):
                js_url = urljoin(url, script['src'])
                self.crawl(js_url, depth + 1, visited_pages)
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

class regx:
    def __init__(self,target_url,target_url_file,timeout,follow_redirect, cookie, user_agent, tls_validation,proxy_setting, depth, regx_string):
        self.target_url = target_url
        self.target_url_file = target_url_file
        self.timeout = int(timeout)
        self.follow_redirect = follow_redirect
        self.cookie = cookie
        self.user_agent = user_agent
        self.tls_validation = tls_validation
        self.proxy_setting = proxy_setting
        self.max_depth = int(depth)
        self.regx_string = regx_string
        self.urls = []

    def is_alive(self,target_url):
        try:
            headers = {
                "User-Agent" : self.user_agent,
                "cookie" : self.cookie
            }

            proxy_setting = {
                "http" : None,
                "https" : None
            }

            if self.proxy_setting:
                proxy_setting = {
                    "http" : self.proxy_setting,
                    "https" : self.proxy_setting
                }
            res = requests.get(target_url,headers=headers,allow_redirects=self.follow_redirect, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)
            return True
        except Exception as e:
            msg.error(e)
            return False
        
    def scanner(self):
        try:
            single_or_multiple_url = 0
            if self.target_url:
                msg.info(f"starting single scan for url {self.target_url}")
                single_or_multiple_url = 0
            elif self.target_url_file:
                msg.info(f"starting scan for url into the file {self.target_url_file}")
                single_or_multiple_url = 1
            elif not self.regx_string:
                msg.error("no regx string not detected, use --regx arg")
                sys.exit()
            else:
                msg.error("no url detected, use --url or --url-file args")
                sys.exit()

            if single_or_multiple_url == 1 :
                file = Path(self.target_url_file)
                if not file.is_file():
                    msg.error(f"file {self.target_url_file} not found!")
                    sys.exit()
                urls_from_file = open(self.target_url_file,"r").read()
                for url in urls_from_file.split("\n"):
                    if formats.validate_url(url):
                        self.crawl(url,0)
                msg.info("done!")
                
            else:
                if not formats.validate_url(self.target_url):
                    msg.error(f"url {self.target_url} is invalid!")
                    sys.exit()

                if self.is_alive(self.target_url):
                    msg.info(f"Connection success for url {self.target_url}")
                    self.crawl(self.target_url,0)
                    msg.info("done!")
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

    def crawl(self,url, depth, visited_pages=None, visited_js=None, visited_img=None):
        try:
            
            if visited_pages is None:
                visited_pages = set()
            if visited_js is None:
                visited_js = set()
            if visited_img is None:
                visited_img = set()
        
            if int(depth) > int(self.max_depth) or url in visited_pages or not formats.validate_url(url) or url in self.urls:
                return
            
            visited_pages.add(url)
            self.urls.append(url)
            try:
                headers = {
                    "User-Agent" : self.user_agent,
                    "cookie" : self.cookie
                }

                proxy_setting = {
                    "http" : None,
                    "https" : None
                }

                if self.proxy_setting:
                    proxy_setting = {
                        "http" : self.proxy_setting,
                        "https" : self.proxy_setting
                    }

                response = requests.get(url,headers=headers,allow_redirects=self.follow_redirect, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)
                detected_regx = re.findall(self.regx_string,response.text)

                if detected_regx:
                    msg.warning(f"url: {url} contains:")
                    msg.success(detected_regx)
            except Exception as e:
                msg.error(" " * (depth * 2) + f"Error fetching {url}: {e}")
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                new_url = urljoin(url, link['href'])
                self.crawl(new_url, depth + 1, visited_pages)

            for script in soup.find_all('script', src=True):
                js_url = urljoin(url, script['src'])
                self.crawl(js_url, depth + 1, visited_pages)
        
            for img in soup.find_all('img', src=True):
                img_url = urljoin(url, img['src'])
                self.crawl(img_url, depth + 1, visited_pages)

        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

class clone:
    def __init__(self,target_url,timeout,user_agent,tls_validation,proxy_setting,project_name):
        self.target_url = target_url
        self.project_name = project_name
        self.timeout = int(timeout)
        self.user_agent = user_agent
        self.tls_validation = tls_validation
        self.proxy_setting = proxy_setting

    def save(self,url, content, base_dir='site'):
        try:
            parsed = urlparse(url)
            path = parsed.path if parsed.path not in ("", "/") else "/index.html"
            
            if not path or path == "/":
                path = "/index.html"
            elif path.endswith("/"):
                path = path + "index.html"
            elif not os.path.splitext(path)[1]:
                path += ".html"
    
            file_path = os.path.join(base_dir, parsed.netloc, path.lstrip('/'))
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(content)
            msg.info(f"Saved: {file_path}")
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

    def scanner(self):
        try:
            visited = set()
            queue = deque([self.target_url])
            domain = urlparse(self.target_url).netloc

            while queue:
                url = queue.popleft()
                if url in visited:
                    continue
                visited.add(url)

                try:
                    headers = {
                        "User-Agent" : self.user_agent
                    }

                    proxy_setting = {
                        "http" : None,
                        "https" : None
                    }

                    if self.proxy_setting:
                        proxy_setting = {
                            "http" : self.proxy_setting,
                            "https" : self.proxy_setting
                        }

                    response = requests.get(url,headers=headers, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)
                except Exception as e:
                    return

                r = random_data()
                if not self.project_name:
                    self.project_name = r.RandomStrings()

                self.save(url, response.content, self.project_name)

                if 'text/html' not in response.headers.get('Content-Type', ''):
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')

                for tag in soup.find_all(['a', 'img', 'script', 'link']):
                    attr = 'href' if tag.name in ['a', 'link'] else 'src'
                    next_url = tag.get(attr)
                    if not next_url:
                        continue
                    next_url = urljoin(url, next_url)
                    if urlparse(next_url).netloc == domain and next_url not in visited:
                        queue.append(next_url)
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()
