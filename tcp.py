import socket
import chatbot

def Main():
    host = "localhost"
    port = 8000
    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if "init" in str(data):
            conn.send("init/안녕하세요 저는 **라는 작품이에요".encode())
            continue

        print("from connected  user: " + str(data))
        Words = bot.Conversation(str(data))
        Translated_Words = bot.Translating_Word(Words)
        Output = bot.Answering(Translated_Words)
        #Output ="안녕"
        data = "response/"+str(Output)
        print("respon: " + str(Output))
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    bot = chatbot.bot()
    Main()