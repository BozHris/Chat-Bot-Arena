import mysql.connector

# Establish a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1611bobo",
    database="votes"
)

cursor = conn.cursor()

# Insert a vote
cursor.execute("INSERT INTO chat_bot_votes (vote) VALUES ('Claude')")
conn.commit()
