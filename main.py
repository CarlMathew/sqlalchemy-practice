from dotenv import load_dotenv
import os
from connect_to_db import SQLClass
from models import Person, Job
from credentials import Credentials

user, password, host, port, database = Credentials()
db = SQLClass(user, password, host, port, database)




search_results = db.search(Person, Person.firstname.like("C%"))



# jb1 = Job("pk412", "developer", 24224.22)
# p3 = Person(3, "Carl", "Morada", 22, "M", "pk412")
# db.insert_query(p3)
db.update_many(Person, Person.firstname == "Carl", firstname = "Carlito", age = 27)