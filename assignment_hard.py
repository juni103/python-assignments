import random

words = ['apple', 'grape', 'peach', 'mango', 'berry']

guess_word = random.choice(words)
guessed_underscore = ['_'] * len(guess_word)
attempts = 6
guessed_letters = []
incorrect_guesses = []

print('Welcome to Hangman!')
print('You have {} attempts to guess the word.'.format(attempts))
print('Guess the word')

while attempts > 0 and '_' in guessed_underscore:
  print(' '.join(guessed_underscore))
  guess = input('Guess a letter: ').lower()

  if len(guess) != 1 or not guess.isalpha():
    print('Please enter a single letter.')
    continue

  if guess in guessed_letters:
    print('You have already guessed that letter.')
    continue

  guessed_letters.append(guess)

  if guess in guess_word:
    for i in range(len(guess_word)):
      if guess_word[i] == guess:
        guessed_underscore[i] = guess
  
  else:
    attempts -= 1
    incorrect_guesses.append(guess)
    print('Incorrect! You have {} attempts left.'.format(attempts))
    print('Incorrect Guessed letters: {}'.format(' '.join(incorrect_guesses)))
    print()

if '_' not in guessed_underscore:
  print('Congratulations! You guessed the word: {}'.format(guess_word))
else:
  print('Game Over! The word was: {}'.format(guess_word))