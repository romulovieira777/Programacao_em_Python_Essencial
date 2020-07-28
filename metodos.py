"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto
pode realizar no seus sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir
o objeto a partir da classe.

# OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Duble Underline)

# OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder(underline no início e no fim)
não é aconselhado. Python possui vários métodos com esta forma de nomeclatura e pode ser que mudemos o
comportamento dessas funções mágicas internas da linguagem. Então, evite ao máximo. De prefrência nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por
underline.



class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__liite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcetagem):
        '''Retorna o valor do produto com o desconto'''
        return (self.__valor * (100 - porcetagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


# Métodos de Classe em Python, são conhecidos como Métodos Estatíticos em outras linguagens.

user = Usuario('Felicty', 'Smoke', 'felicty@gmail.com', '123456')

Usuario.conta_usuario()  # Forma correta

user.conta_usuario()  # Possível, mas incorreta


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__liite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcetagem):
        '''Retorna o valor do produto com o desconto'''
        return (self.__valor * (100 - porcetagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user = Usuario('Felicty', 'Smoke', 'felicty@gmail.com', '123456')

print(user._Usuario__gera_usuario())  # Maneira errada



class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__liite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcetagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcetagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método Estatíco

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Felicty', 'Smoke', 'felicity@gmail.com', '123456')

print(user.contador)

print(user.definicao())

"""
