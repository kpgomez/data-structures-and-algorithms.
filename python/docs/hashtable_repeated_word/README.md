# Find the First Repeated Word in a Book
<!-- Description of the challenge -->
Write a function called first_repeated_word that reads in a string called book and return first word that repeats. Ignore punctuation and casing. Return None if no word in the book repeats.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Whiteboard](/docs/hashtable_repeated_word/whiteboard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used a dictionary to hold new words as they were encountered which gave me O(1) lookup time when
checking if a word already exists. I also used the built-in string methods; split(), maketrans(), translate(),
and string.punctuation which has a time complexity of O(n) for each method. Removing punctuation and splitting
the words resulted in a time complexity of O(n^2) + O(n). I believe maketrans() and translate() created a time
complexity of O(n^2) while split() added O(n). The split() occurred after removal of punctuation.
While iterating through each word, I applied lower() to each word as well which makes this a nested loop with a
time complexity of O(n^2). Final complexity was O(2n^2) + O(n) + O(1) which simplifies to **O(n^2)**. The space
complexity was O(n) because the size of the dictionary was dependent on the size of the input, and if no words
were repeated then they would be equal in size.
## Solution
<!-- Show how to run your code, and examples of it in action -->
`pytest -k test_hashtable_repeated_word.py -vv` to run tests verbose

## Attribution
- [Remove punctuation](https://datagy.io/python-remove-punctuation-from-string/)
- [Iterate over words instead of individual characters](https://www.geeksforgeeks.org/iterate-over-words-of-a-string-in-python/)
- [Time complexity for maketrans](https://chat.openai.com/c/a07aa2c4-7971-4ee9-b698-1ef5b31aceba)
