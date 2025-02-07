from util import two_letter

def main():
    num_correct = 0
    while num_correct < len(two_letter):
        answer = input()
        if answer.lower() in two_letter:
            num_correct += 1
            print("Correct!")
            print(f"Words Remaining: {len(two_letter) - num_correct}")
        else:
            print("Incorrect, try again.")
    print("Congratulations! You've named every two letter combination!")


if __name__ == "__main__":
    main()