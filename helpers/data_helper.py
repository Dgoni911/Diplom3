import random
import string

class DataHelper:
    @staticmethod
    def generate_email():
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        domain = ''.join(random.choices(string.ascii_lowercase, k=6))
        return f"{username}@{domain}.com"
    
    @staticmethod
    def generate_password():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    @staticmethod
    def generate_name():
        return ''.join(random.choices(string.ascii_letters, k=10))