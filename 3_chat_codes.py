messages_number = int(input())

for m_number in range(messages_number):
    specific_number = int(input())
    if specific_number == 88:
        print("Hello")
    elif specific_number == 86:
        print("How are you?")
    elif specific_number > 88 :
        print("Bye.")
    else:
        print("GREAT!")