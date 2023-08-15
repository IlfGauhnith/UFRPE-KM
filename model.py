class User:

    def __init__(self, username, password, nome):
        self.username = username
        self.password = password
        self.nome = nome

    def __str__(self):
        return f"username: {self.username}, password: {self.password}, nome: {self.nome}"