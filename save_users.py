def save_users(images):
    for i in images:
        if i.has_attr( "alt" ):
            print (i['alt'].replace("Foto del perfil de ",""))
