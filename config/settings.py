import os

class Settings:
    MONGO_URI = os.getenv(
        "MONGO_URI", "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME", "sigmon"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY", "sigmon_ufpi_2026"
    )