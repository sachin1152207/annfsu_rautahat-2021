from database_connection import connection

# Database inilization
conn = connection()
cursor = conn.cursor()

def get_nagar_committes():
    cursor.execute("SELECT `committe_id`,`name`,`president_name`,`group_pic` FROM `all_committes` WHERE `committe_type` = 'Nagar'")
    committes = cursor.fetchall()
    return committes

def get_campus_committes():
    cursor.execute("SELECT `committe_id`,`name`,`president_name`,`group_pic` FROM `all_committes` WHERE `committe_type` = 'Campus'")
    committes = cursor.fetchall()
    return committes

def get_mavi_committes():
    cursor.execute("SELECT `committe_id`,`name`,`president_name`,`group_pic` FROM `all_committes` WHERE `committe_type` = 'Mavi'")
    committes = cursor.fetchall()
    return committes