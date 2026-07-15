import datetime
print("===================")
print("Welcome to Voice Assitant!")
print("===================")
print("Available Commands: ")
print("1. Hello")
print("2. time")
print("3. date")
print("4. exit")

while True:
    command = input("\nYou: ").lower()

    if command == "hello":
        print("Assistant: Hello! How can I help you?")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Assistant: Current Time:", current_time)

    elif command == "date":
        current_datet = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Assistant: Today's Date:", current_date)
    
    elif command == "exit":
        print("Assistant: Goodbye! Have a nice day.")
        break

    else:
        print("Assistant: Sorry! I don't understand that command.")