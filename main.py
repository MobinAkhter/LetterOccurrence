from collections import Counter

print("Welcome to the Frequency Analysis of Letters App")

non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', '?', ',', '!', '"', "'", ":", ';', '(', ')',
               '%', '$', '&', '#', '\n', '\t']

key_phrase_1 = input("Enter a word or phase to count the occurrence of each letter: ").lower().strip()

# Removing all non letters from key phrase

for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)

letter_count = Counter(key_phrase_1)

print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\t  Letter\t\tOccurrence\t\tPercentage")

for key, value in sorted(letter_count.items()):
    percentage = 100 * value / total_occurrences
    percentage = round(percentage, 2)
    print("\t\t" + key + "\t\t\t\t" + str(value) + "\t\t\t  " + str(percentage) + "%")

ordered_letter_count = letter_count.most_common()

key_phrase_1_ordered_letters = []

for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_1_ordered_letters:
    print(letter, end='')

key_phrase_2 = input("\nEnter a word or phase to count the occurrence of each letter: ").lower().strip()

# Removing all non letters from key phrase

for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurrences = len(key_phrase_2)
123
letter_count = Counter(key_phrase_2)

print("\nHere is the frequency analysis from phrase 2: ")
print("\n\t  Letter\t\tOccurrence\t\tPercentage")

for key, value in sorted(letter_count.items()):
    percentage = 100 * value / total_occurrences
    percentage = round(percentage, 2)
    print("\t\t" + key + "\t\t\t\t" + str(value) + "\t\t\t  " + str(percentage) + "%")

ordered_letter_count = letter_count.most_common()

key_phrase_2_ordered_letters = []

for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])

print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_2_ordered_letters:
    print(letter, end='')