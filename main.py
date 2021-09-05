import random

# race_dict contains horses number as key, and their steps, and counter for the steps as values.
race_dict = {'2': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '3': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '4': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '5': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '6': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '7': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '8': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '9': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '10': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '11': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1],
             '12': [['c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd'], -1]
             }


class Race:
    """Methods for a horse race game... """

    # class Race initiated so as to take racing dictionary as parameter
    def __init__(self, any_race_dict):
        self.race_dict = any_race_dict
        self.cont_game = True

    def play(self):
        # Two dies are thrown and sum of both is stored in die_sum
        die_one = random.randint(1, 6)
        die_two = random.randint(1, 6)
        self.die_sum = die_one + die_two
        print("Rolling two dies ....")
        print(f"die_one = {die_one}, die_two = {die_two}, DIE_SUM = {self.die_sum}")
        return self.die_sum

    def step(self):
        # die_sum is compared to horse number contained in race_dict above. the horse number that equates to die_sum
        # moves ahead(digit case CAPITALIZED). The numbers in race_dict are used as counters for each horse.
        for horse in self.race_dict:
            if self.die_sum == int(horse):
                self.race_dict[horse][1] = self.race_dict[horse][1] + 1
                step = self.race_dict[horse][1]
                self.race_dict[horse][0][step] = self.race_dict[horse][0][step].upper()
        return [print(key, ":", "   ".join(value[0]), "  ", value[1]) for key, value in self.race_dict.items()]


    def game_play(self):
        # Initiates and plays game according to user's response by running play(), and step() methods above.
        while self.cont_game:
            user_play = input("Play?: (y/n) \n")
            if user_play == "n":
                self.cont_game = False
                return "End of game!"
            else:
                self.play()
                self.step()
            for horse in self.race_dict:
                if self.race_dict[horse][1] == ((len(self.race_dict[horse][0])) - 1):
                    self.cont_game = False
                    return f"The winner of the race is horse {horse}, congratulations!"


game = Race(race_dict)
# print(game.play())
# print(game.step())
print(game.game_play())
print(race_dict['4'][1] + 1)
#print(game.race_dict)


# [print(key, ":", " ".join(value)) for key, value in race_dict.items()]
