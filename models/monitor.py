class Monitor:
    def __init__(self, matricula, nome, email, disciplina, horario):
        self.__matricula = matricula
        self.__nome = nome
        self.__email = email
        self.__disciplina = disciplina
        self.__horario = horario

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
    def disciplina(self):
        return self.__disciplina

    @property
    def horario(self):
        return self.__horario

    def to_dict(self):
        return {
            "matricula": self.__matricula,
            "nome": self.__nome,
            "email": self.__email,
            "disciplina": self.__disciplina,
            "horario": self.__horario
        }