import random
import string

def generate_email():
    """Генерируем уникальный email"""
    base_part = f"test_{random.randint(1000, 9999)}@example.com"
    return base_part

def generate_password(length=8):
    """Генерация надежного пароля длиной минимум 8 символов."""
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password