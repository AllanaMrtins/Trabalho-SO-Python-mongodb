from repositories.aluno_repository import AlunoRepository
from repositories.monitor_repository import MonitorRepository
from repositories.atendimento_repository import AtendimentoRepository

class Dash_service:
    def __init__(self):
        self.aluno_repo = AlunoRepository()
        self.monitor_repo = MonitorRepository()
        self.atendimento_repo = AtendimentoRepository()

    def resumo_geral(self):
        return{
            "total_alunos" : self.aluno_repo.count(),
            "total_monitores" : self.monitor_repo.count(),
            "total_atendimentos" : self.atendimento_repo.count()
        }
    
    def estatistica(self):
        alunos = self.aluno_repo.count()
        monitores = self.monitor_repo.count()
        atendimentos = self.atendimento_repo.count()

        total = alunos + monitores + atendimentos

        if total == 0:
            return{
                "mensagem": "nenhum dado cadastrado no sistema de minitoria ainda."
            }
        
        return{
            "total_registros": total,
            "alunos_percentual": round((alunos / total) * 100, 2),
            "monitores_percentual": round((monitores / total) * 100, 2),
            "atendimentos_percentual": round((atendimentos / total) * 100, 2)
        }
    
    def relatorio_texto(self):
        resumo = self.resumo_geral()

        return(
            f"DASHBOARD - SISTEMA DE MONITORIA UFPI\n"
            f"----------------------------------------"
            f"Alunos cadastrados: {resumo['total_alunos']}\n"
            f"Monitores ativos: {resumo['total_monitores']}\n"
            f"Atendimentos realizados: {resumo['total_atendimentos']}\n"
        )