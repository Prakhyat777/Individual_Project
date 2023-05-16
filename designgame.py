class GameContext:
    def showQuestion(self, question):
        print(question['text'])

    def end(self):
        print("End The Game")


class Game:
    def __init__(self, game_context):
        self.game_context = game_context
        self.questions = [
            {
                'text': "Does it ensure you have at most one instance of a class in your application?",
                'yes': 11,
                'no': 6
            },

            {
                'text': "Does it provide the object creation mechanism that enhances the flexibilities of the existing code?",
                'yes': 0,
                'no': 2

            },

            {
                'text': "Is it responsible for how one class communicates with others?",
                'yes': 3,
                'no': 8
            },
            {
                'text': "Does it provide a mechanism to the context to change its behavior?",
                'yes': 9,
                'no': 5
            },
            {
                'text': "Welcome to the game! Think of a design pattern and answer these following yes/no questions. Ready?",
                'yes': 1,
                'no': 'finish'
            },

            {
                'text': "Does it allow a group of objects to be notified when some state changes?",
                'yes': 15,
                'no': 16
            },
            {
                'text': "Is it Builder Pattern?",
                'yes': 7,
                'no': 19
            },

            {
                'text': "Woohoo!guessed it! Try again?",
                'yes': 4,
                'no': 'finish'
            },

            {
                'text': "Does it explain how to assemble objects and classes into larger structure and simplifies the structure by identifying the relationships?",
                'yes': 10,
                'no': 19
            },
            {
                'text': "Is Changing behavior built into its scheme?",
                'yes': 13,
                'no': 14
            },
            {
                'text': "Does it attach additional behavior to an object dynamically at run-time?",
                'yes': 17,
                'no': 18
            },
            {
                'text': "Is it Singleton Pattern?",
                'yes': 7,
                'no': 19
            },
            {
                'text': "Is it Builder Pattern?",
                'yes': 7,
                'no': 19
            },

            {
                'text': "Is it State pattern?",
                'yes': 7,
                'no': 19
            },
            {
                'text': "Is it Strategy Pattern?",
                'yes': 7,
                'no': 19
            },

            {
                'text': "Is it Observer Pattern?",
                'yes': 7,
                'no': 19
            },

            {
                'text': "Is it Command Pattern?",
                'yes': 7,
                'no': 19
            },

            {
                'text': "Is it Decorator pattern?",
                'yes': 7,
                'no': 19
            },
            {
                'text': "Is it Adapter Pattern?",
                'yes': 7,
                'no': 19
            },

            {
                'text': "Oops!Something went wrong!Try again?",
                'yes': 4,
                'no': 'finish'
            }
        ]
        self.current_question = 4

    def start(self):
        self.game_context.showQuestion(self.questions[self.current_question])

    def answer(self, answer):
        next_question = self.questions[self.current_question][answer]
        self.current_question = next_question
        if next_question == 'finish':
            self.game_context.end()
        else:
            self.game_context.showQuestion(self.questions[next_question])


def main():
    """
    The main function that runs the game.
    Creates a game context and a game object, starts the game, and handles player input until the game ends.
    """
    game_context = GameContext()
    game = Game(game_context)
    game.start()

    while True:
        answer = input("").lower()

        if answer == "yes":
            game.answer("yes")
        elif answer == "no":
            game.answer("no")
        else:
            print("Please enter either 'yes' or 'no'.")


if __name__ == '__main__':
    main()
