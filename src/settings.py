from decouple import config


DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0-uc85n.mongodb.net/test?retryWrites=true&w=majority"
