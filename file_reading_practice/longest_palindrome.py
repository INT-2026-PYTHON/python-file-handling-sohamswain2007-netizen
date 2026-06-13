"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
def is_palindrome(word):
    return word == word[::-1]
def main():
      # Step 1: Read the file and store words
      with open('sowpods.txt', 'r') as file:
         words = [line.strip() for line in file]
   
      # Step 2: Find the longest palindrome(s)
      longest_length = 0
      longest_palindromes = []
   
      for word in words:
         if is_palindrome(word):
               length = len(word)
               if length > longest_length:
                  longest_length = length
                  longest_palindromes = [word]
               elif length == longest_length:
                  longest_palindromes.append(word)
   
      # Step 3: Print the result
      print(f"Longest palindrome length: {longest_length}")
      for palindrome in longest_palindromes:
         print(palindrome)
if __name__ == "__main__":
    main()

