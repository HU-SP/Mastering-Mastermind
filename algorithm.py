import itertools
import random

import game
import globalFunctions

# Alle mogelijke pins
pins = [1, 2, 3, 4, 5, 6]
# Genereerd alle mogelijke antwoorden
answerSet = list(itertools.product([1, 2, 3, 4, 5, 6], repeat=4))


# Maak de answer kleiner doormiddel van de feedback onderdeel van
# paragraaf 2.2 van Yet another Mastermind Strategy
def trim_answer_set(secret, fb):
    # Hier pakken we de global variable set
    global answerSet
    # Maken we een nieuwe set
    newAnswerSet = []
    # Loop door alle codes in de set
    for code in answerSet:
        # Krijg de feedback van de code met de 'secret'
        fbCompare = game.feedback(globalFunctions.tuple_to_int(code), secret)
        # Wanneer feedback gelijk is aan de feedback van de secret
        # Voeg de code toen aan de nieuwe se
        if fbCompare == fb:
            newAnswerSet.append(code)
    # de oude set wordt overschreden door de nieuwe set
    answerSet = newAnswerSet
    return


# Dit is de functie van de stap 2.2 in "Yet another mastermind strategy"
def looking_one_step_ahead():
    table = {}
    # Hier maken we een feedback set van de aantal hoeveelheden feedback we terug kunnen krijgen
    # Met een bepaalde gok.
    # Loop door de set
    for item in answerSet:
        # De basis feedback set, dit zijn alle soorten feedback dat je kan krijgen
        feedbackSet = {'(0, 0)': 0, '(0, 1)': 0, '(0, 2)': 0, '(0, 3)': 0, '(0, 4)': 0, '(1, 0)': 0, '(1, 1)': 0,
                       '(1, 2)': 0,
                       '(1, 3)': 0, '(2, 0)': 0, '(2, 1)': 0, '(2, 2)': 0, '(3, 0)': 0, '(4, 0)': 0}
        # Loop door de set
        for i in answerSet:
            # Krijg feedback van de items in de set
            fb = game.feedback(globalFunctions.tuple_to_int(i), globalFunctions.tuple_to_int(item))
            # Zoek de feedback soort en verhoog die met 1
            feedbackSet[str(fb)] += 1
        # Per item zetten we de feedback in de tabel
        table[item] = feedbackSet
    return table


# Hier bereken en we de worst case strategy
# paragraaf 2.3 van Yet another Mastermind Strategy
def worstcase(table):
    counter = {}
    # Blijkbaar zit hier een issue in waarbij bij sommige getallen
    # de table breekt maar ik heb daar helaas niet genoeg
    # Tijd meer voor om te fixen :(
    # Zorgt ervoor dat we alle feedback mogelijkheden hebben
    tableFBKeys = table[answerSet[0]].keys()
    # Loop door de set
    for item in answerSet:
        # Elk element begint bij 0 omdat je kan met een gok
        # 0 element weg halen uit de lijst
        counter[item] = 0
        # Loop door de keys
        for key in tableFBKeys:
            # Voor elk element voeg daar de hoeveel elementen
            # Er mogelijk over zijn na deze gok
            counter[item] += (table[item][key] ** 2) / len(answerSet)
    return counter


# Hier kiezen we de beste keuze,
# de keuze baseren we op de hoeveelheid elementen
# er over blijven in de lijst na het kiezen.
def best_choice(table):
    # Lege lijst voor de volgende guess
    nextGuess = []
    # Loop door de items van de vorige functie
    # gemaakt dict
    for item in table.items():
        # Pak de item waarbij de waarde het laagste is
        # De laagste waarde omdat er dan de minste aantal combinaties overblijven in de set
        if item[1] == min(table.values()):
            # Voeg de item toe aan de volgende gok lijst
            nextGuess.append(item[0])
    # Laad de oude set
    global answerSet
    # de oude set wordt overschreden door de nieuwe
    answerSet = nextGuess
    # return het eerste element want alle elementen halen evenveel elementen uit de set.
    return nextGuess[0]


# Computer genereerd een random code
def generate_code():
    code = []
    for i in range(0, 4):
        code.append(random.randrange(1, 7))
    return code
