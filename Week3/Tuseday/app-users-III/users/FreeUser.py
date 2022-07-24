from users.User import User

# override the post method so they can only make 2 post

class FreeUser(User):

    def new_post(self):
        if self.post_number < 2:
            return super().new_post()
        else:
            return 'You have reached your maximum number of post'
