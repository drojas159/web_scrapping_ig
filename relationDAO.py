from connection import connection

def insert_relation(relation_follow):    
    sql = """INSERT INTO relation_follow(user_id_following,user_id_followed) VALUES(%s,%s)"""
    conn = None
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute(sql, (relation_follow.user_id_following ,relation_follow.user_id_followed,))
        conn.commit()
        cur.close()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def relation_exists(relation_follow):
    conn = connection()
    cur = conn.cursor()
    sql = """select follow_id from public.relation_follow where user_id_following=%s and user_id_followed=%s"""
    cur.execute(sql,(relation_follow.user_id_following ,relation_follow.user_id_followed,))
    rel_exists = cur.fetchone()
    cur.close()
    conn.close()
    if (rel_exists is None ):
        return False
    else:
        return True