my_sequence = ("ACAACTATGCATACTATCGGGAACTATCCT")

print(len(my_sequence))


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i : i + len(Pattern)] == Pattern:
            count = count + 1
    return count

pattern = "ACTAT"

print(PatternCount(my_sequence, pattern))