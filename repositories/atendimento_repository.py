from database.connection import MongoConnection

class AtendimentoRepository:

    collection = MongoConnection.get_database()["atendimentos"]

    @staticmethod
    def inserir(atendimento):
        return AtendimentoRepository.collection.insert_one(
            atendimento.to_dict()
        )

    @staticmethod
    def listar():
        return list(
            AtendimentoRepository.collection.find(
                {},
                {"_id": 0}
            )
        )

    @staticmethod
    def buscar_por_monitor(matricula_monitor):
        return list(
            AtendimentoRepository.collection.find(
                {"monitor_matricula": matricula_monitor},
                {"_id": 0}
            )
        )

    @staticmethod
    def buscar_por_aluno(matricula_aluno):
        return list(
            AtendimentoRepository.collection.find(
                {"aluno_matricula": matricula_aluno},
                {"_id": 0}
            )
        )
