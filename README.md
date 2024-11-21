# 100daysPython-DAY-9

# Auction Program
This Python script implements a simple auction system where multiple bidders can place their bids, and the program determines the highest bidder. The console-based interface clears the screen between inputs to ensure privacy and smooth operation.

# Features
- Accepts bids from multiple users.
- Clears the console after each user's input for a better user experience.
- Determines and displays the highest bidder along with their bid amount.
# How to Run
1. Ensure you have Python installed on your system.
Install the required dependency by running:
- pip install art
2. Save the script in a file, e.g., auction.py.
3. Execute the script:
python auction.py

# Usage
1.When prompted, enter your name and your bid.
2.Indicate whether there are more bidders by typing 'yes' or 'no'.
3.If you type 'yes', the screen will clear, and the next bidder can enter their details.
4.If you type 'no', the program will announce the winner with the highest bid.

# Example

What is your name? Alice
What is your bid? $250
Are there any other bidders? Type 'yes' or 'no'. yes
What is your name? Bob
What is your bid? $300
Are there any other bidders? Type 'yes' or 'no'. no
the winner is Bob with a bid of $300
# Notes
. The art module is used to display a banner/logo. Ensure you have it installed before running the script.
. The cls() function ensures the console is cleared after each input. It works on both Windows and Unix-based systems.
# License
This project is free to use and modify. No specific license is applied.
