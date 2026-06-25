from database.connection import MongoConnection

def replica_status():
    db = MongoConnection.get_database()

    try:
        result = db.command("replSetGetStatus")
        return result
    
    except Exception as error:

        return {
            "status": "erro",
            "mensagem": str(error)
        }