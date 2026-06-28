from repositories.monitor_repository import MonitorRepository

class MonitorService:

    @staticmethod
    def listar():
        return MonitorRepository.listar()

    @staticmethod
    def buscar_por_matricula(matricula):
        return MonitorRepository.buscar_por_matricula(
            matricula
        )

    @staticmethod
    def criar(monitor):
        return MonitorRepository.inserir(monitor)

    @staticmethod
    def salvar(dados):
        # CORRIGIDO: Repassa o dicionário para o método inserir do repositório
        return MonitorRepository.inserir(dados)
    
    @staticmethod
    def contar():
        return MonitorRepository.contar()
    
    @staticmethod
    def buscar_por_disciplina(nome_disciplina):
        return MonitorRepository.buscar_por_disciplina(nome_disciplina)

