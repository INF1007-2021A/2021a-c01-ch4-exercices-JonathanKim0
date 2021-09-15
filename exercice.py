#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string)%2 == 0:
        return True
    else:
        return False


def remove_third_char(string: str) -> str:
    modify = list(string)
    modify.pop(2)
    return "".join(modify)


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new = list(string)
    for i in range(len(string)):
        if new[i] == old_char:
            new[i] = new_char
    return "".join(new)


def get_number_of_char(string: str, char: str) -> int:
    count = 0
    new = list(string)
    for i in range(len(string)):
        if new[i] == char:
            count += 1
    return count


def get_number_of_words(sentence: str, word: str) -> int:
    count = 0
    new = sentence.split(" ")
    for i in range(len(new)):
        if new[i] == word:
            count += 1
    return count


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
