class TerminalColor:
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

class Core:	
	def Banner():
		print(f"""
 .S     S.     sSSs   .S.SSSs     .S.sSSs     .S      S.    .S.sSSs     .S.sSSs      sSSs   .S.sSSs    
.SS     SS.   d**SP  .SS~SSSSS   .SS~YS**b   .SS      SS.  .SS~YS**b   .SS~YS**b    d**SP  .SS~YS**b   
S*S     S*S  d*S'    S*S   SSSS  S*S   'S*b  S*S      S*S  S*S   'S*b  S*S   'S*b  d*S'    S*S   'S*b  
S*S     S*S  S*S     S*S    S*S  S*S    S*S  S*S      S*S  S*S    S*S  S*S    S*S  S*S     S*S    S*S  
S*S     S*S  S&S     S*S SSSS%P  S*S    d*S  S&S      S&S  S*S    S&S  S*S    S&S  S&S     S*S    d*S  
S&S     S&S  S&S_Ss  S&S  SSSY   S&S   .S*S  S&S      S&S  S&S    S&S  S&S    S&S  S&S_Ss  S&S   .S*S  
S&S     S&S  S&S~SP  S&S    S&S  S&S_sdSSS   S&S      S&S  S&S    S&S  S&S    S&S  S&S~SP  S&S_sdSSS   
S&S     S&S  S&S     S&S    S&S  S&S~YSY*b   S&S      S&S  S&S    S&S  S&S    S&S  S&S     S&S~YSY*b   
S*S     S*S  S*b     S*S    S&S  S*S   'S*b  S*b      d*S  S*S    S*S  S*S    S*S  S*b     S*S   'S*b  
S*S  .  S*S  S*S.    S*S    S*S  S*S    S*S  S*S.    .S*S  S*S    S*S  S*S    S*S  S*S.    S*S    S*S  
S*S.sSs.S*S   SSSbs  S*S SSSSP   S*S    S&S   SSSbssdSSS   S*S    S*S  S*S    S*S   SSSbs  S*S    S&S  
SSS*SSS*S*S    YSSP  S*S  SSY    S*S    SSS    'SSPYSS'    S*S    SSS  S*S    SSS    YSSP  S*S    SSS  
                     SP          SP                        SP          SP                  SP          
                     Y           Y                         Y           Y                   Y   
Coded by:{TerminalColor.Red} sp34rh34d {TerminalColor.Reset} Email:{TerminalColor.Red} adonis.izaguirre@kapa7.com / adons@outlook.com {TerminalColor.Reset}
twitter: {TerminalColor.Red}@spearh34d{TerminalColor.Reset}
Welcome to WebRunner v1.0 [{TerminalColor.Green}https://github.com/sp34rh34d/WebRunner{TerminalColor.Reset}]
======================================================================================================""")
