class Aluno:
    def __init__(self,matricula,nome,email,curso,periodo):
        self.__matricula = matricula
        self.__nome = nome
        self.__email = email
        self.__curso = curso
        self.__periodo = periodo

    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def curso(self):
        return self.__curso

    @property
    def periodo(self):
        return self.__periodo

    def to_dict(self):
        return {
            "matricula": self.__matricula,
            "nome": self.__nome,
            "email": self.__email,
            "curso": self.__curso,
            "periodo": self.__periodo
        }