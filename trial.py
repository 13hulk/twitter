# Account Creation

class User:
    def __init__(self, name, userid, age, posts=None):
        self.name = name
        self.userid = userid
        self.age = age
        self.posts = posts

    def __repr__(self):
        return User(self.name, self.userid, self.age, self.posts)


# users
user1 = User("Ullas Zingade", "ubz", 23)
user2 = User("Vikas Zingade", "vikasbz", 27)
user3 = User("Seema MJ", "smj", 26)
all_users = [user1, user2, user3]


class Tweet:
    def __init__(self, post, like=0):
        self.post = post
        self.like = like

    def __repr__(self):
        return f"\nUser Post : {self.post} \nLikes : {self.like}"


print("\nUsers Available :")
print(f"\n{user1.name}\n{user2.name}\n{user3.name}")
while True:
    current_user = None
    inp_user_id = input("\nEnter your User ID : ")

    for i in all_users:
        if inp_user_id == i.userid:
            current_user = i.name
            print(f"\nActive User : {current_user} \nUser ID : {i.userid} \nUser Age : {i.age} \nUser Posts : {i.posts}")

            while True:
                ch = input("\n1. New Post \n2. Previous Posts \n3. Exit\n Enter your choice : ")
                if ch == '1':
                    tweet = Tweet(input("\nEnter the Post here : \n"))
                    print(tweet.post)
                    i.posts = tweet.post

                elif ch == '2':
                    print(f"\nYour recent Post : i.posts")

                elif ch == '3':
                    exit()
                    break
            break

        else:
            print("Wrong ID")
            break
