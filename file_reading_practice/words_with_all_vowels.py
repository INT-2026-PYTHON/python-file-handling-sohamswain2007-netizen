"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
def main():
    # Step 1: Read the file and store words
    with open('sowpods.txt', 'r') as file:
        words = [line.strip() for line in file]

    # Step 2: Define the set of vowels
    vowels = set('aeiou')

    # Step 3: Find words that contain all vowels
    words_with_all_vowels = []
    for word in words:
        word_lower = word.lower()
        if all(vowel in word_lower for vowel in vowels):
            words_with_all_vowels.append(word)

    # Step 4: Print the results
    for word in words_with_all_vowels:
        print(word)
    print(f'Total words with all vowels: {len(words_with_all_vowels)}')
if __name__ == "__main__":
    main()
