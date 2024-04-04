import streamlit as st
import random

def guess_number(secret_number, guess):
    if guess < secret_number:
        return "Too low! Try again."
    elif guess > secret_number:
        return "Too high! Try again."
    else:
        return "Congratulations! You guessed the number."

def main():
    st.title("Number Guessing Game")

    secret_number = random.randint(1, 100)
    guess = st.number_input("Enter your guess (between 1 and 100):", min_value=1, max_value=100, step=1)
    result = guess_number(secret_number, guess)

    st.write(result)

if __name__ == "__main__":
    main()
