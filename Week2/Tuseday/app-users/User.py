


class User:
    all_users = {}
    all_user_post = {}



    def __init__(self, name, email_address, dob, user_name):
        self.name = name
        self.email = email_address
        self.dob = dob
        self.user_name = user_name
        self.post = {}
        self.post_number = 0

    def __str__(self):
        return f"""
            Name: {self.name}
            Email: {self.email}
            DOB: {self.dob}
        """

    def update_global_post(self):
        User.all_user_post[self.email] = self.post
        
    def print_post(self):
        if len(self.post) > 0:
            print(f"Here are the post for {self.name}")
            for key,value in self.post.items():
                print(f"post # {key} - {value}")

    def delete_post(self):
        post_delete_number = input(f"Please select a post number to delete {self.post}")
        self.post.pop(int(post_delete_number))
        self.update_global_post()

    def new_post(self):
        new_content = Post(input(f"Hi {self.name}, what would you like to post? - "))
        self.post[self.post_number] = new_content
        User.add_post({self.email: {self.post_number: new_content}})
        self.post_number += 1

    @classmethod
    def add_post(cls, post):
        cls.all_user_post = post

class Post:

    def __init__(self, content):
        self.content = content
        
    
    def __str__(self):
        return self.content
    

user1 = User(name='Kevin',email_address='kevinlbelk229@gmail.com',dob= '02/29/84', user_name= 'KLB')
user2 = User(name='Sheena', email_address='sheena@gmail.com',dob= '01/17/1984', user_name= 'Sheen')
user3 = User(name='Zella', email_address='zella@gmail.com',dob= '05/17/2013', user_name= 'Honey')

user1.new_post()
user2.new_post()

user1.print_post()
print(User.all_user_post)

def user_interface():
    help = """
        help - displays this help text
        create_post - creates a new post
        my_post - displays all of your posts
        all_post - displays everyones posts
        switch_user - logs you out
        delete_post - lets you delete a post
        quit - ends the program
        """
    print(help)
    user = input("Welcome. Please login - ")
    while user != None:
        command = input(f"Hello {user}! What would you like to do? - ")
        if command == 'help':
            print(help)
        elif command == 'create_post':
            pass
        elif command == 'my_post':
            pass
        elif command == 'all_post':
            pass
        elif command == 'switch_user':
            pass
        elif command == 'delete_post':
            pass
        elif command == 'quit':
            break

# user_interface()