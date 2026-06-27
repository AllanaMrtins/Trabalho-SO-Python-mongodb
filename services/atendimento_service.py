from repositories.aluno_repository import AlunoRepository
from repositories.monitor_repository import MonitorRepository
from repositories.atendimento_repository import AtendimentoRepository


class AtendimentoService:

    @staticmethod
    def listar():
        return AtendimentoRepository.listar()

    @staticmethod
    def criar(atendimento):

        # REGRA 1: monitor deve pertencer à disciplina
        if not MonitorRepository.monitor_pertence_a_disciplina(
            atendimento.monitor_matricula,
            atendimento.disciplina
        ):
            raise Exception("Monitor não ministra esta disciplina.")

        # REGRA 2: aluno deve estar matriculado na disciplina
        if not AlunoRepository.aluno_esta_matriculado_na_disciplina(
            atendimento.aluno_matricula,
            atendimento.disciplina
        ):
            raise Exception("Aluno não está matriculado nesta disciplina.")

        return AtendimentoRepository.inserir(atendimento)
