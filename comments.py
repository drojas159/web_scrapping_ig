class Comment:
    
    comment_id =0
    text  = ""
    user_id = 0
    publication_id = 0
    emoji = ""

    def __init__(self,  text, user_id, publication_id):
        self.text = text
        self.user_id = user_id
        self.publication_id = publication_id
