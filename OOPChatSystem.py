class User:
    def __init__(self,username):
        self.username=username
        self.chatroom=None
    
    def join_a_classroom(self,chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom")
        else:
            chatroom.add_user(self)
            self.chatroom=chatroom
            print(f"{self.username} joined {chatroom.name}")
        
    
    def leave_a_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} not in a chatroom")
        else:
            self.chatroom.remove_user(self)
            self.chatroom=None
    
    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message,not in a chatroom")
        else:
            self.chatroom.broadcast(self,content)

class ChatRoom:
    def __init__(self,name):
        self.name=name
        self.users=[]
        self.messages=[]
    
    def add_user(self,user):
        self.users.append(user)

    def remove_user(self,user):
        self.users.remove(user)
    
    def show_history(self):
        for msg in self.messages:
            print(msg)

    def broadcast_msg(self,sender,content):
        message=Message(sender,content)
        print(message)
        self.messages.append(message)

class Message:
    message_counter=1 

    def __init__(self,sender,content):
        self.sender=sender.username
        self.content=content
        self.id=Message.message_counter
        Message.message_counter+=1
    
    def __str__(self):
        return f"{self.id} {self.sender} : {self.content}"


