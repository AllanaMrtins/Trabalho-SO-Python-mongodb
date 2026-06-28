from repositories.aluno_repository import AlunoRepository

class AlunoService:

    @staticmethod
    def listar():
        return AlunoRepository.listar()

    @staticmethod
    def buscar_por_matricula(matricula):
        return AlunoRepository.buscar_por_matricula(
            matricula
        )

    @staticmethod
    def criar(aluno):
        return AlunoRepository.inserir(aluno)
    
    @staticmethod
    def salvar(dados):
        # Repassa o dicionário vindo do Flask para o método criar que você já possui
        return AlunoService.criar(dados)
    
    @staticmethod
    def contar():
        return AlunoRepository.contar()

