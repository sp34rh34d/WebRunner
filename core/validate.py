import re

class formats:
    def validate_url(url):
        url_pattern = re.compile(
            r'^(https?:\/\/)'
            r'(?:(?:\d{1,3}\.){3}\d{1,3}'
            r'|'                                
            r'[\da-z\.-]+\.[a-z\.]{2,6})'
            r'(?::\d{1,5})?'
            r'(\/[^\s]*)?$'  
        )
        
        if url_pattern.match(url):
            return True
        
    def validate_email(text):
        email_pattern = re.compile(
            r'[\w\.-]+@[\w\.-]{7,}'
        )

        return email_pattern.findall(text)
