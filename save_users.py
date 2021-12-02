def save_users(images,users):
    for i in images:
        if (i.has_attr( "alt" ) and i['alt'].find("Foto del perfil de")!=-1):
            username = i['alt'].replace("Foto del perfil de ","")
            if username in users == True:
                users[username]= users[username] +1
            else:
                users[username]=1
    return users
