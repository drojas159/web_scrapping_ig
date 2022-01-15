class Relation_follow:
    
    follow_id =0
    user_id_following = 0
    user_id_followed = 0
    type_relation = 0

    def __init__(self,  user_id_following, user_id_followed, type_relation):
        self.user_id_following = user_id_following
        self.user_id_followed = user_id_followed
        self.type_relation = type_relation
