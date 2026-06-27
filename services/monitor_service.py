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
