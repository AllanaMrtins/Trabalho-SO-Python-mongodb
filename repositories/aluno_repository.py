from database.connection import MongoConnection

class AlunoRepository:
    collection = MongoConnection.get_database()["alunos"]

    @staticmethod
    def inserir(aluno):
        if isinstance(aluno, dict):
            return AlunoRepository.collection.insert_one(aluno)
        
        return AlunoRepository.collection.insert_one(aluno.to_dict())

    @staticmethod
    def listar():
        return list(AlunoRepository.collection.find({}, {"_id": 0}))

    @staticmethod
    def buscar_por_matricula(matricula):
        return AlunoRepository.collection.find_one(
            {"matricula": matricula},
            {"_id": 0}
        )
        
    @staticmethod
    def aluno_esta_matriculado_na_disciplina(matricula_aluno, disciplina):
        aluno = AlunoRepository.collection.find_one(
            {
                "matricula": matricula_aluno,
                "disciplina": disciplina
            }
        )
        return aluno is not None
    
    @staticmethod
    def contar():
        return AlunoRepository.collection.count_documents({})
