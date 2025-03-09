# 🪨📄✂️ Rock-Paper-Scissors (Python3)

## **📌 Learning Objectives**
By the end of this lesson, you will be able to:
- Understand how Python handles **user input** and **randomization**.
- Use **functions** to organize your code.
- Implement **conditional statements** (`if`, `elif`, `else`) to determine a winner.
- Work with **lists** and **loops** to create an interactive game.

---

## **📖 Glossary of Concepts**
| Concept        | Definition |
|---------------|------------|
| `import random` | A built-in Python module that generates random values. |
| `list` | A collection of values, similar to an array in JavaScript. |
| `function` | A block of reusable code that performs a specific task. |
| `input()` | A function that allows the user to enter data. |
| `while True` | A loop that continues running until explicitly stopped. |
| `if-elif-else` | A structure that makes decisions based on conditions. |

---

## **📝 Main Activity: Writing Rock-Paper-Scissors in Python**
Below is the **pseudocode** version of the game. Copy the comments into your Python file, then write the actual code underneath each comment.

```python
# Step 1: Import the random module to generate a random choice for the computer.
# (Hint: Use "import random")

# Step 2: Create a list containing the three possible choices: "rock", "paper", "scissors"
# (Hint: Use a list like this: ["rock", "paper", "scissors"])

# Step 3: Define a function to determine the winner.
# - It should take two parameters: the player's choice and the computer's choice.
# - If both choices are the same, return "It's a tie!"
# - If the player wins based on the rules, return "You win!"
# - Otherwise, return "Computer wins!"
# (Hint: Use an if-elif-else statement to compare choices)

# Step 4: Create a function to run the game.
# - Start an infinite loop using "while True"
# - Ask the player to input their choice (rock, paper, or scissors)
# - Convert the input to lowercase to ensure case insensitivity
# - If the player types "quit", print a goodbye message and break the loop
# - If the input is not valid, prompt the user again
# - The computer should randomly select a choice from the list
# - Print both the player's and computer's choices
# - Call the function that determines the winner and print the result

# Step 5: Call the function to start the game.
```
# 🎯 Conclusion
Congratulations! You have built a fully functional Rock-Paper-Scissors game in Python. 🎉

This exercise shows how similar Python is to JavaScript while reinforcing:

Handling user input (input() vs. prompt() in JavaScript).
Using functions for better code organization.
Making random selections (random.choice() vs. Math.random() in JavaScript).
Using loops and conditionals to control the game flow.

 # ✅ Check for Understanding

1.  How does Python handle user input compared to JavaScript's prompt()?
2. What would happen if we removed the .lower() method when getting user input?
3. How does Python’s random.choice() compare to JavaScript’s Math.random()?
4. What is the purpose of using while True in this game?
5. How would you modify the game to allow the user to keep track of their score?
