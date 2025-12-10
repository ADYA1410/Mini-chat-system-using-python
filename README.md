**🗨️ Python Chatroom System**
A lightweight Object-Oriented Chatroom implementation in Python.
Users can join chatrooms, send messages, and view chat history — showcasing simple interactions between objects.

**✨ Features**
👥 Users can join or leave chatrooms
💬 Message broadcasting with unique message IDs
🧠 Chat history storage per room
🧱 Clean OOP structure using three classes: User, ChatRoom, Message


**📂 Project Structure**
├─ User        → Represents chat participants
├─ ChatRoom    → Manages users & messages
└─ Message     → Stores message data (ID, sender, content)


**🧩 Class Summary**
Class	Responsibilities:
User	Join/leave chatrooms and send messages
ChatRoom	Maintain users & broadcast messages with history
Message	Auto-labeled message data with printable format

**🚀 Usage Example**
room = ChatRoom("Python Room")
u1 = User("Alex")
u2 = User("Sam")

u1.join_a_classroom(room)
u2.join_a_classroom(room)

u1.send_message("Hello!")
u2.send_message("Hi!")

room.show_history()


Output
Alex joined Python Room
Sam joined Python Room
1 Alex : Hello!
2 Sam : Hi!

**📌 Constraints & Notes**
A user can only be in one chatroom at a time
Messages persist only while the program runs

🧑‍💻 Author
ADYA THACHILATH PRATAPCHANDRAN
Project maintained for learning and demonstration purposes.

Console-based simulation — no networking layer yet
