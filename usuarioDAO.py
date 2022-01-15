from connection import connection


def insert_user(user):
    
    sql = """INSERT INTO users(user_name,profile_url) VALUES(%s,%s)"""
    conn = None
    try:
        conn = connection()
        cur = conn.cursor()
        url= "https://www.instagram.com/"
        cur.execute(sql, (user.user_name.upper() ,url+user.user_name,))
        conn.commit()
        cur.close()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def user_exists(user):
    conn = connection()
    cur = conn.cursor()
    sql = """select user_id,user_name from public.users where user_name=%s"""
    cur.execute(sql,(user.user_name.upper() ,))
    user_db = cur.fetchone()
    cur.close()
    conn.close()
    if (user_db is None ):
        return False
    else:
        return True

def get_all_users():
    conn = connection()
    cur = conn.cursor()
    sql = """select user_id,user_name,profile_url from public.users"""
    cur.execute(sql,)
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

