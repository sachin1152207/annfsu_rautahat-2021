from database_connection import connection

# Database inilization
conn = connection()
cursor = conn.cursor()


def get_members():
    cursor.execute("SELECT * FROM `district_committe_members` ")
    members = cursor.fetchall()
    return members

def about_description():
    cursor.execute("SELECT * FROM `about` ")
    about_desc = cursor.fetchall()
    return about_desc[0]