class Atendimento:

    def __init__(
        self,
        aluno_matricula,
        monitor_matricula,
        disciplina,
        data,
        horario,
        local,
        descricao,
        status
    ):
        self.__aluno_matricula = aluno_matricula
        self.__monitor_matricula = monitor_matricula
        self.__disciplina = disciplina
        self.__data = data
        self.__horario = horario
        self.__local = local
        self.__descricao = descricao
        self.__status = status

    @property
    def aluno_matricula(self):
        return self.__aluno_matricula

    @property
    def monitor_matricula(self):
        return self.__monitor_matricula

    @property
    def disciplina(self):
        return self.__disciplina

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def local(self):
        return self.__local

    @property
    def descricao(self):
        return self.__descricao

    @property
    def status(self):
        return self.__status

    def to_dict(self):
        return {
            "aluno_matricula": self.__aluno_matricula,
            "monitor_matricula": self.__monitor_matricula,
            "disciplina": self.__disciplina,
            "data": self.__data,
            "horario": self.__horario,
            "local": self.__local,
            "descricao": self.__descricao,
            "status": self.__status
        }