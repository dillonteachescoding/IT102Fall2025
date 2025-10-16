#!/usr/bin/env python3
# Sample script that writes to a file
# By Dillon Kierce

#Hardcoded variables

questions = [
    "What is your name? ",
    "What is your favorite color",
    "What is your city you grew up in?",
    "What is the current season?"
]

answer = []


# Create a loop that will take question and save it to a file that we can read
for q in questions:
    ans = input(f"Question {q}: ")
    answer.append(f"{ans}")


with open ("hackme.txt", "w") as file:
    for line in answer:
        file.write(line + "\n")


with open ("hackme.txt", "r") as file:
    line = file.read()
    print(line)
