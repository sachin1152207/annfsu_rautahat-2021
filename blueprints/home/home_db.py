from database_connection import connection

# Database inilization
conn = connection()
cursor = conn.cursor()


def hero_description():
    cursor.execute("SELECT description from hero_description")
    hero_description = cursor.fetchall()
    return hero_description

def get_members():
    cursor.execute("SELECT * FROM `district_committe_members` WHERE `id` BETWEEN 1 AND 4;")
    members = cursor.fetchall()
    # print(members)
    return members

def get_member_word():
    cursor.execute("SELECT `name`,`post`,`text`,`profile_src`, `date` FROM `member_words` ORDER BY `date` DESC LIMIT 5;")
    members_word = cursor.fetchall()
    return members_word


