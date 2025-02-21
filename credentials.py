from dotenv import load_dotenv
import os


def Credentials():
    load_dotenv()
    username = os.getenv("user")
    password = os.getenv("password")
    hostname = os.getenv("host")
    sport = os.getenv("port")
    database =  os.getenv("database")

    return username, password, hostname, sport, database