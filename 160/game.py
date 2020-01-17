import csv
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    with open(BATTLE_DATA) as csv_file:
        defeat_map = {}
        data_dict = csv.DictReader(csv_file)
        for row in data_dict:
            defeat_map[row['Attacker']] = [x[0] for x in row.items() if x[1] == 'win']
        return defeat_map


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    try:
        p1_defeats = defeat_mapping[player1]
        p2_defeats = defeat_mapping[player2]
    except KeyError:
        raise ValueError
    else:
        if player1 == player2:
            return 'Tie'
        elif player2 in p1_defeats:
            return player1
        else:
            return player2
