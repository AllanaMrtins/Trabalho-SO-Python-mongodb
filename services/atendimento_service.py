from repositories.aluno_repository import AlunoRepository
from repositories.monitor_repository import MonitorRepository
from repositories.atendimento_repository import AtendimentoRepository


class AtendimentoService:

    @staticmethod
    def listar():
        return AtendimentoRepository.listar()

    @staticmethod
    def criar(atendimento):

        monitor_valido = (
            MonitorRepository.monitor_pertence_a_disciplina(
                atendimento.monitor_matricula,
                atendimento.disciplina
            )
        )

        if not monitor_valido:
            raise Exception(
                "O monitor não é responsável por esta disciplina."
            )

        aluno_valido = (
            AlunoRepository.aluno_esta_matriculado_na_disciplina(
                atendimento.aluno_matricula,
                atendimento.disciplina
            )
        )

        if not aluno_valido:
            raise Exception(
                "O aluno não está matriculado nesta disciplina."
            )

        AtendimentoRepository.inserir(
            atendimento
        )

        return {
            "status": "sucesso",
            "mensagem": "Atendimento registrado com sucesso."
        }
