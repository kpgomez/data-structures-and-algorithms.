# Implement a simplified LEFT JOIN for 2 Hashmaps
<!-- Description of the challenge -->
Write a function called left_join that takes two dictionaries as parameters and returns a data structure that imitates a left join.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](/docs/hashtable_left_join/left_join%20whiteboard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used two empty lists; one to hold individual records, and one to hold all records as a result of the left join. This approach
made the most sense after completing the visualization. The Big O space complexity is O(n) and the time complexity is O(n+m)

## Solution
<!-- Show how to run your code, and examples of it in action -->
`pytest -k test_hashtable_left_join.py -vv`

```python

synonyms = {
  "A": "B",
  "B": "C",
  "C": "D",
  "D": "E"
}

antonyms = {
  "A": "C",
  "B": "D",
  "C": "E",
  "E": "F"
}

print(left_join(synonyms, antonyms))

""" example output
[
  ["A", "B", "C"],
  ["B", "C", "D"],
  ["C", "D", "E"],
  ["D", "E", "NONE"]
]
"""
```
