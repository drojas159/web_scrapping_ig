class Publication:
    
    publication_id =0
    publication_url  = ""
    caption = ""
    user_id = 0
    
    def __init__(self,  shortcode, user_id):
        self.shortcode = shortcode
        self.user_id = user_id
