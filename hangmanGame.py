import requests
import random

def getWord():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    randomWordNumber = random.randint(0,len(WORDS)-1)
    theOriginalWord = str(WORDS[randomWordNumber])
    theWord = theOriginalWord[2:-1]
    return theWord

def stickman(wrongGuesses):
    stages = [
        """
        """,
        """ 
             _____
            | > < |
            |__O__|
                 
                
                 
               
        """,
        """
            _____
           | 0 0 |
           |__O__|
              |  
              | 
              |  
              |
              
            
        """,
        """
            _____
           | - - |
           |__O__|
              |  
              | 
              |  
              |
             /  
            /    
        """,
        """
            _____
           | v v |
           |__^__|
              |  
              | 
              |  
              |
             / \ 
            /   \ 
        """,
        """
            _____
           | z z |
           |_____|
              |  
             /| 
            / |  
              |
             / \ 
            /   \ 
        """,
        """
            _____
           | x x |
           |__=__|
              |  
             /|\ 
            / | \ 
              |
             / \ 
            /   \ 
        """,
    ]
    index = min(wrongGuesses, len(stages) - 1)
    print(stages[index])
    return 0

def userProgram(theWord):
   
    print("Your word is ", str(len(str(theWord))),"letters long")
    
    wrongGuesses = 0
    maxWrongGuesses = 6
    currentGuess = ["_" for _ in theWord]
    lettersUsed = []

    while wrongGuesses < maxWrongGuesses and "_" in currentGuess:
        guessesLeft = (maxWrongGuesses - wrongGuesses)
        print("You have",guessesLeft,"Guesses left")
        print(f"Used letters: ",{', '.join(lettersUsed) if lettersUsed else 'None'})
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in lettersUsed:
            print("You already guessed that letter!")
            continue

        lettersUsed.append(guess)

        if guess in theWord:
            for i in range(len(theWord)):
                if theWord[i] == guess:
                    currentGuess[i] = guess
            print(f"Correct! Current guess: {' '.join(currentGuess)}")
        else:
            wrongGuesses += 1
            print(f"Incorrect guess. Try again.")
            stickman(wrongGuesses)


    if wrongGuesses == maxWrongGuesses:
        print(f"You lose! The word was: {theWord}")
    else:
        print(f"Congratulations! You guessed the word: {theWord}")
    return 0

def main():
    print("Welcome to Hangman, the game where you have the guess the random word letter by letter. But be careful, if you make 6 mistakes you will Hang the hang man")
    theWord = getWord()
    userProgram(theWord)
    return 0

if __name__ == "__main__":
    main()
