from connection import connection


def insert_publication(publication):
    
    sql = """INSERT INTO publications(shortcode,user_id_fk,publication_url) VALUES(%s,%s,%s)"""
    conn = None
    try:
        conn = connection()
        cur = conn.cursor()
        url= "https://www.instagram.com"
        cur.execute(sql, (publication.shortcode,publication.user_id,url+publication.shortcode,))
        conn.commit()
        cur.close()
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_all_publications():
    
    conn = connection()
    cur = conn.cursor()
    sql = """select publication_id,publication_url,user_id_fk,shortcode from public.publications"""
    cur.execute(sql,)
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users