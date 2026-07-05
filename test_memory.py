from memory.database import create_database
from memory.memory import remember, recall

create_database()

remember("college", "DSCE")

print("Stored College:", recall("college"))