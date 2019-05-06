import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""

        number = input(f"Guess a number between {START} and {END}: ")
        if not number:
            print("Please enter a number")
            raise ValueError

        try:
            number = int(number)
        except ValueError:
            print("Should be a number")
            raise ValueError

        if number < START or number > END:
            print("Number not in range")
            raise ValueError

        if number in self._guesses:
            print("Already guessed")
            raise ValueError

        self._guesses.add(number)
        return number

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f"{guess} is correct!")
            return True
        elif guess < self._answer:
            print(f"{guess} is too low")
        elif guess > self._answer:
            print(f"{guess} is too high")
        return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while True:

            try:
                guess = self.guess()
            except ValueError:
                continue

            no_of_guesses = len(self._guesses)
            self._win = self._validate_guess(guess)

            if self._win:
                print(f"It took you {no_of_guesses} guesses")
                break
            elif no_of_guesses >= MAX_GUESSES:
                print(f"Guessed {no_of_guesses} times, answer was {self._answer}")
                break


if __name__ == "__main__":
    game = Game()
    game()
