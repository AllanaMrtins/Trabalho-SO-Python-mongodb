from database.connection import MongoConnection

class MonitorRepository:

    collection = MongoConnection.get_database()["monitores"]

    @staticmethod
    def inserir(monitor_dict):
        return MonitorRepository.collection.insert_one(monitor_dict)

    @staticmethod
    def listar():
        return list(
            MonitorRepository.collection.find(
                {},
                {"_id": 0}
            )
        )

    @staticmethod
    def buscar_por_matricula(matricula):
        return MonitorRepository.collection.find_one(
            {"matricula": matricula},
            {"_id": 0}
        )
    
    @staticmethod
    def monitor_pertence_a_disciplina(
        matricula_monitor,
        disciplina
    ):
        monitor = MonitorRepository.collection.find_one(
            {
                "matricula": matricula_monitor,
                "disciplina": disciplina
            }
        )

        return monitor is not None
    
    @staticmethod
    def contar():
        return MonitorRepository.collection.count_documents({})
    
    @staticmethod
    def buscar_por_disciplina(nome_disciplina):
        # Procura um monitor que lecione a disciplina ignorando maiúsculas/minúsculas
        return MonitorRepository.collection.find_one(
            {"disciplina": {"$regex": f"^{nome_disciplina}$", "$options": "i"}},
            {"_id": 0}
        )

