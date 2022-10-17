# Hangman Game

![responsive](assets/responsive.pm3.JPG)

[Link to Heroku](https://project-milestone3.herokuapp.com/
)

[GitHub Repo](https://github.com/Vaidots/Project-milestone3)

# Project description 


This is my third milestone project for Code Institute. Hangman game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
The word to guess is represented by a row of dashes representing each letter of the word. If the suggested letter is in the word, it is written down, If guessed wrong it will progress the hangman picture and mark the used letter. This process is repeated until the hangman is completed or the user guesses the word.


# Flow chart

![flowchart](assets/HangmanDiagram.jpg)

[Back to top](#hangman-game)

# Features and User experience

* Greetings message
  * First time user can easily follow the instruction
  * UX: as a first time or returning user, I want to receive a welcoming message.

![Welcome](assets/Welcome.JPG)

* Game starts
  * Random word is selected.
  * How many lives/tries player has.
  * Shows how many letters the word has counting "_".
  * UX: as a first time or returning user, I want to see what stage I am at in the game.
  * UX: as a first time or returning user, I want to see how many letters in the word I have to guess.

![Username](assets/Username.JPG)

* Incorrect username
  * The player has to use only alphabetic letters to progress in the game.

![incorrect username](assets/incorrectUsername.JPG)

* Correct, incorrect guesses or have already guessed messages.
  * The player gets feedback after guessing.
  * UX: as a first time or returning user, I want to receive feedback on my guesses.

![Correct guess](assets/CorrectGuess.JPG)

* Correct word guess
  * Player receives a congratulations message after guessing the word.
  * Has an option to play again or quit.
  * UX: as a first time or returning user, I want to receive a nice message when won.

![Guessed the word](assets/GuessedTheWord.JPG)

* Failing to guess the word
  * Has an option to play again or quit.
  * UX: as a first time or returning user, I want to receive a comforting message when failling to guess the word.

![fail to guess](assets/FailedToGuess.JPG)

* Play again option
  * User can play again typing letter "y".
  * UX: as a first time or returning user, I want to have a chance to play again.

![Play again](assets/PlayAgain.y.JPG)

* Username quits the game
  * User can quit the game by typing any letter except "y" to quit the game
  *  UX: as a first time or returning user, I want to have an option to quit the game.

![Quit](assets/Quit.JPG)



[Back to top](#hangman-game)


# Future features to implement

* Different difficulity levels
* Create scoring system
* Create categories for users to choose
* Create an option to leave the game at any time


# Technologies Used


* [Python 3.10.8](https://www.python.org/)

* [Git](https://git-scm.com/)

* [GitHub](https://github.com/) 

* [Heroku](https://id.heroku.com/login)

* [LucidChart](https://www.lucidchart.com/pages)


[Back to top](#hangman-game)

# Validation

* Originally meant to validate the code at pep8online.com, however the site was down.

   * Checked in slack community about the issue and found an alternative.
   
1. Run the command pip3 install pycodestyle  Note that this extension may already be installed, in which case this command will do nothing.
2. In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
3. Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results (image 1).
4. Select pycodestyle from the list.
5. PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

[Back to top](#hangman-game)


# Testing

* Checked if chosing numbers or symbols will get an error telling to use alphabetic letters only.
* Checked if entering correct letter will be shown in the random word space.
* Checked if entering incorrect letter will take a live and progress hangman picture.
* Checked after answering the word or running out of lives gets an option to play again.
* Checked when asked if you want to play again after pressing "y" the player can start guessing again.
* Checked that any other letter pressed will end the game.


[Back to top](#hangman-game)


# Deployment 

* The project was deployed using Code Institutes mock terminal for Heroku.
  * Steps to deploy:
1. Fork or clone this repository.
2. Ensure the Procfile is in place.
3. requirements.txt can be left empty as this project does not use any external libraries.
4. Create a new app in Heroku.
5. Select "New" and "Create new app".
6. Name the new app and click "Create new app".
7. In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
8. Whilst still in "Settings", click "Reveal Config Vars" and input the folloing. KEY: PORT, VALUE: 8000.  
9. Nothing else is needed here as this project does not have any sensitive files.
10. Click on "Deploy" and select your deploy method and repository.
11. Click "Connect" on selected repository.
12. Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
13. Heroku will now deploy the site.

[Back to top](#hangman-game)

# Credits

* Thanks to Code Institute for the deployment terminal.
* Stackoverflow
* Fellow students in slack
* [Tech with Tim](https://www.youtube.com/c/TechWithTim)
* Youtube tutorial for hangman game [link](https://www.youtube.com/watch?v=m4nEnsavl6w)

[Back to top](#hangman-game)

# Special thanks

* My mentor at Code Institute Brian Macharia for code review, help and feedback.

[Back to top](#hangman-game)
