from user import User
from publications import Publication
from usuarioDAO import insert_user, user_exists, get_all_users
from publicationDAO import insert_publication, get_all_publications
import json

def save_users(images):
    for i in images:
        if (i.has_attr( "alt" ) and i['alt'].find("Foto del perfil de")!=-1):
            username = i['alt'].replace("Foto del perfil de ","")
            usr = User(username)
            if (user_exists(usr)==False):
                insert_user(usr)


def get_users():
    users_list=[]
    users=get_all_users()
    
    for i in range (len (users)):
        usr =User(users[i][1])
        usr.profile_url=users[i][2]
        usr.user_id=users[i][0]
        users_list.append(usr)
    
    return users_list

def save_comments(soup):
    data = soup.find('script')
    data= str(data)
    data=data.replace('<script type="text/javascript">window._sharedData = ','')
    data=data.replace(';</script>','')
    print(data)
    #jasonData=json.loads(str(data))
    file1 = open("./scrappingFiles/contet_comments1.json","w", encoding='utf-8') 
    file1.write(data)

    #comments =jasonData['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_parent_comment']['edges']
    #print(len(comments))
    #for i in range (len(comments)):
    #    file1.write(comments[i]['node']['text']+"\n")

    #file1.close()
    
def save_publication(code,user_id):
    post = Publication(code,user_id)
    insert_publication(post)

def get_publications():
    publications_list =[]
    publications=get_all_publications()
    
    for i in range (len (publications)):
        post =Publication(publications[i][3],0)
        post.publication_id = publications[i][0]
        post.publication_url = publications[i][1]
        post.user_id = publications[i][2]

        publications_list.append(post)
    print(publications_list)
    return publications_list


