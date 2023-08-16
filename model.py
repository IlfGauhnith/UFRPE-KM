class User:
    def __init__(self, username, password, nome=None, profile_pic_path=None):
        self.username = username
        self.password = password
        self.nome = nome
        self.profile_pic_path = profile_pic_path

    def __str__(self):
        return f"username: {self.username}, password: {self.password}, nome: {self.nome}"


class Beach:
    def __init__(self, nome, descricao, pic_path):
        self.nome = nome
        self.descricao = descricao
        self.pic_path = pic_path
