import globalFunctions
import algorithm

def initialize_game():
    gameChoice = input('___  ___          _                      _           _\n'
          '|  \/  |         | |                    (_)         | |\n'
          ' | .  . | __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |\n'
          "| |\/| |/ _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |\n"
          "| |  | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |\n"
          "\_|  |_/\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|\n"
          "Welkom bij mastermind!\n"
          "Als wie wil je beginnen? Mastermind of Speler?\n"
          "\033[93m Type in Mastermind of Speler \033[0m \n")
    print(gameChoice.upper() == 'Mastermind'.upper())
    if (gameChoice.upper()) == 'MASTERMIND':
        mastermind_human()
    elif (gameChoice.upper()) == 'SPELER':
        mastermind_pc()
    else:
        while gameChoice.upper() != 'Mastermind'.upper() or gameChoice.upper() != 'SPELER':
            print('Dat was geen correcte input!')
            gameChoice = input("Als wie wil je beginnen? Mastermind of Speler?\n"
                               "\033[93m Type in Mastermind of Speler \n")



# Hier is de "mens" de mastermind
def mastermind_human():
    # De mens vult een secret code in
    secret = int(input('Wat is de secret code? \n'))
    # Hier zetten we 2 variablen voor het algoritme klaar
    guess = None
    guessCount = 0
    # We blijven doorloopen totdat de gok hetzelfde is als de secret
    while guess != secret or guess is None:
        if guessCount != 0:
            # Krijg de feedback van de eerste gok
            fb = feedback(guess, secret)
            # Maak de combinatie lijst korter
            algorithm.trim_answer_set(guess, fb)
            # Doe een nieuwe guess op basis van de nieuwe lijs
            guess = globalFunctions.tuple_to_int(algorithm.best_choice(algorithm.worstcase(algorithm.looking_one_step_ahead())))
        elif guessCount == 0:
            # Bereken een gok op basis van de set
            guess = globalFunctions.tuple_to_int(algorithm.best_choice(algorithm.worstcase(algorithm.looking_one_step_ahead())))
        # Wanneer het algoritme meer dan 10 gokken heeft gedaan dan heeft de computer
        # Gefaald
        elif guessCount >= 10:
            print('Je hebt gefaald')
            break
        # Verhoog het aantal gokken gedaan
        guessCount += 1

    print('De computer heeft de code gekraakt!')
    print('De computer deed er: ' + str(guessCount) + ' beurten over!')


def mastermind_pc():
    # Maak een secret
    secret = globalFunctions.int_to_list(algorithm.generate_code())
    # Laat de mens een gok doen
    # Ik weet dat ik hier nog een check zou moeten doen voor of de input wel correct is.
    guess = int(input("Gok de 4 cijferige code:"))
    # Geef feedback van de gekozen gok
    fb = feedback(guess, secret)
    # Wanneer de feedback 4 zwarte pins is dan heb je gewonnen zo niet
    # Dan spelen we verder
    if fb == (4,0):
        print('Je hebt gewonnen in 1 gok!')
    else:
        guesses = 1
        # Loopen als er geen correcte gok is gedaan
        while guess != secret:
            # Wanneer de gebruik de 10 gokken heeft bereikt
            # Dan heeft de speler verloren
            if guess == 10:
                print('Je hebt helaas verloren...')
            # Anders gaan we door
            else:
                # Laat de feedback zien aan de speler
                print('Helaas je gok was fout, dit is je feedback: \n'
                      + str(fb))
                # De speler doet nog een gok
                guess = int(input("Gok de 4 cijferige code:"))
                # Nieuwe feedback van nieuwe gok
                fb = feedback(guess, secret)
                guesses += 1
        print('Je hebt de code gekraakt! Je deed er: ' + str(guesses) + ' beurten over!')


def feedback(code, secret):
    # De integers omzetten naar lists om makkelijker te vergelijken
    code = [int(x) for x in str(code)]
    secret = [int(x) for x in str(secret)]
    # Feedback
    fb = [0, 0]
    # Dict om te checken of er geen duplicates zijn
    duplicate = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    if code == secret:
        return (4, 0)
    else:
        # Hier loopen we door elk element heen van de secret en code
        for i in range(4):
            # check of de cijfers hetzelfde zijn
            if code[i] == secret[i]:
                # Voeg een zwarte pin toe aan de feedback
                fb[0] += 1
                # Als er een cijfer al als wit was genoteerd
                # Draai dat terug
                if duplicate[code[i]] >= 1 and fb[1] > 0:
                    fb[1] -= 1
                duplicate[code[i]] += 1
            # Kijken of de cijfer van de code in de secret zit
            # Zo ja, voeg een witte pin toe
            elif duplicate[code[i]] == 0 and code[i] in secret:
                fb[1] += 1
                duplicate[code[i]] += 1
            else:
                continue
    return tuple(fb)
