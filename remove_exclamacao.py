"""Write function RemoveExclamationMarks which removes all exclamation marks from a given string."""

def remove_exclamation_marks(s):
    palavra_sem_exclamacao = ""
    for i in s:
        if "!" not in i:
            palavra_sem_exclamacao = palavra_sem_exclamacao + i
    return palavra_sem_exclamacao

print(remove_exclamation_marks("!jo!rge!!"))