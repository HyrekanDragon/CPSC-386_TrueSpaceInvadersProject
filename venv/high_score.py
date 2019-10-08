import  operator
import pygame
filepath = 'high_score.txt'

class Highscores:
    """A Cclass to keep track of high scores"""

    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Font settings for scoring information
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 60)
        self.font2 = pygame.font.SysFont(None, 100)

        self.high_scores = dict()

        with open(filepath) as fp:
            line = fp.readline()
            while line:
                name, score = line.strip('\n').split(' ')
                self.high_scores.update({name: int(score)})
                line = fp.readline()

    def check_score(self, score):
        """Checks if endgame score beats the lowest high score"""
        self.sort()
        first = next(iter(self.high_scores.keys()))
        print('\n')

        if (score > self.high_scores[first]):
            name = input("Enter 3 Letters.")
            while len(name) != 3:
                name = input('Enter 3 Lettrs')
            name = name.upper()
            if name not in self.high_scores.keys():
                del self.high_scores[first]
            self.high_scores.update({name: score})
            print("Highscore added")

    def sort(self):
        """Sorts highscores by score"""
        self.high_scores = dict(sorted(self.high_scores.items(), key=operator.itemgetter(1)))

    def save_scores(self):
        """Saves highscores into a file"""
        self.sort()
        fp = open(filepath, 'w+')
        for name in self.high_scores:
            fp.write("{} {}\n".format(name, self.high_scores[name]))

        fp.close()

    def show_scores(self):
        str = "Highscores"
        score_image = self.font2.render(str, True, self.text_color, self.settings.bg_color)
        score_rect = score_image.get_rect()
        score_rect.center = (600, 100)
        self.screen.blit(score_image, score_rect)

        y = 200
        for name in self.high_scores:
            str = "{} {}".format(name, self.high_scores[name])
            score_image = self.font.render(str, True, self.text_color, self.settings.bg_color)
            score_rect = score_image.get_rect()
            score_rect.center = (600, y)
            self.screen.blit(score_image, score_rect)
            y += 50