class User:
    all_user_post = {}

    def __init__(self, name, email, dob, username):
        self.name = name
        self. email = email
        self.dob = dob
        self.username = username
        self.post_number = 0
        self.post = {}

    def __str__(self):
        return f"""
            Name: {self.name}
            Email: {self.email}
            DOB: {self.dob}
            Username: {self.username}
        """

    def update_global_post(self):
        User.all_user_post[self.username] = self.post

    def print_post(self):
        if len(self.post) > 0:
            print(f"Here are the post for {self.name}")
            for key,content in self.post.items():
                print(f"post number {key} - {content}")

    def delete_post(self):
        post_delete_number = input(f"Please select a post number to delete - {self.print_post()}")
        self.post.pop(int(post_delete_number))
        self.update_global_post()
        return f" Post number {post_delete_number} has been deleted"

    def new_post(self):
        new_content = input(f"Hi {self.name} what would you like to post? - ")
        self.post[self.post_number] = new_content
        self.post_number += 1
        self.update_global_post()
        return f"New post number {self.post_number - 1} has been posted"




