import re

class Validation:
    def is_valid_email(self, email):
        if not re.search('[@.]', email):
            return False
        return True

        # pattern = ''
        # return re.match(pattern, email) is not None

    def is_valid_password(self, password):
        if len(password) < 5:
            return False
        if not any(c.isdigit() for c in password):  # проверка на наличие хотя бы одной цифры
            return False
        if not re.search('[@_!#$%^&*(){}~:/?-]', password):
            return False
        return True