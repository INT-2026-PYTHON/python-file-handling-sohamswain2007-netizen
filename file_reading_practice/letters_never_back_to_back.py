"""
## 2. Alphabets That Never Appear Back-to-Back  *(Medium)*

=================================================
ALPHABETS NEVER IN SEQUENCE
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every alphabet letter that:
   - APPEARS at least once in the words of
     the file, AND
   - NEVER appears TWICE IN A ROW (back-to-back)
     in ANY word of the file.

Letters that never appear in the file at all
should NOT be in the answer. Letters that
appear back-to-back at least once (like the
'u' in "vacuum") should also be excluded.

-------------------------------------------------
Input Example (sowpods.txt sample):
aardvark
hello
buzz
moon
puppy

Output Example:
Letters that never appear back-to-back:
['b', 'd', 'e', 'h', 'k', 'm', 'n', 'r', 'u', 'v', 'y']

-------------------------------------------------
Explanation:
Letters seen anywhere in the sample:
   aardvark -> a, r, d, v, k
   hello    -> h, e, l, o
   buzz     -> b, u, z
   moon     -> m, o, n
   puppy    -> p, u, y
   seen    = {a, b, d, e, h, k, l, m, n, o,
              p, r, u, v, y, z}

Letters that ever appear back-to-back:
   aa (aardvark), ll (hello), zz (buzz),
   oo (moon),     pp (puppy)
   doubled = {a, l, z, o, p}

Answer = seen - doubled
       = {b, d, e, h, k, m, n, r, u, v, y}
Sorted -> ['b', 'd', 'e', 'h', 'k', 'm', 'n',
           'r', 'u', 'v', 'y']
=================================================

"""
def main():
    # Step 1: Read the file and store words
    with open('sowpods.txt', 'r') as file:
        words = [line.strip() for line in file]

    # Step 2: Create sets to track seen letters and doubled letters
    seen = set()
    doubled = set()

    # Step 3: Process each word to populate the sets
    for word in words:
        for i in range(len(word)):
            letter = word[i]
            seen.add(letter)
            if i > 0 and word[i] == word[i - 1]:
                doubled.add(letter)

    # Step 4: Calculate letters that never appear back-to-back
    result = sorted(seen - doubled)

    # Step 5: Print the result
    print("Letters that never appear back-to-back:")
    print(result)
if __name__ == "__main__": 
      main()

               
