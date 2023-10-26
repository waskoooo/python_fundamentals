def memory_game(sequence):
    moves = 0

    while True:
        command = input()

        if command == "end":
            print("Sorry you lose :(")
            print(" ".join(sequence))
            break

        moves += 1

        indexes = command.split()
        index1 = int(indexes[0])
        index2 = int(indexes[1])

        if index1 == index2 or index1 < 0 or index1 >= len(sequence) or index2 < 0 or index2 >= len(sequence):
            print("Invalid input! Adding additional elements to the board")
            middle = len(sequence) // 2
            sequence.insert(middle, f"-{moves}a")
            sequence.insert(middle, f"-{moves}a")
            continue

        if sequence[index1] == sequence[index2]:
            print(f"Congrats! You have found matching elements - {sequence[index1]}!")
            sequence.pop(max(index1, index2))
            sequence.pop(min(index1, index2))

            if len(sequence) == 0:
                print(f"You have won in {moves} turns!")
                break
        else:
            print("Try again!")


if __name__ == "__main__":
    sequence = input().split()
    memory_game(sequence)
