"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""
def main():
    # Step 1: Read sowpods.txt and store words in a set
    with open('sowpods.txt', 'r') as file:
        sowpods_words = set(line.strip() for line in file)

    # Step 2: Read sonnet_words.txt and store words in a set
    with open('sonnet_words.txt', 'r') as file:
        sonnet_words = set(line.strip() for line in file)

    # Step 3: Find words that are in sonnet but not in sowpods
    unique_sonnet_words = sonnet_words - sowpods_words

    # Step 4: Print the results
    print("Words in sonnet but not in sowpods:")
    print(sorted(unique_sonnet_words))
    print(f"Total: {len(unique_sonnet_words)}")
if __name__ == "__main__":
    main()
