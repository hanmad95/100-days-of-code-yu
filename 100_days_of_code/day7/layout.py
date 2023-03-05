
from typing import List, Tuple


def layout() -> Tuple[List[str], str]:

    stages = ['''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''']

    logo = '''
            _
            | |
            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  |
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |
                                |___/
            '''

    return stages, logo