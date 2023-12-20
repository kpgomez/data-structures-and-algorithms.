# Fizz Buzz Tree
Traverse a k_ary_tree and create a new tree. For each node, check for fizzbuzz. The new tree will have the same structure
as the original tree with the exception that its node values will be "FizzBuzz" if original node value is divisible by 5 and 3,
"Buzz" if divisible by 5, "Fizz" if divisible by 3, or a string of the original node value if it doesn't meet any of the
fizzbuzz criteria.

## Whiteboard Process
![whiteboard](/docs/tree_fizz_buzz/fizz_buzz_tree_whiteboard.png)
[link to Figma](https://www.figma.com/file/U6JMMqjUw6tcCZDb2Z3u97/tree_fizz_buzz?type=whiteboard&node-id=25-1258&t=K6otTD1wDvKYLfVF-0)

## Approach & Efficiency

**Approach:** Used BFS, a queue data structure, as the intermediary to traverse the original tree.

**Time complexity: O(n^2)**

In our test example, the size of input tree is 7 Nodes.

There are 4 steps in check_fizz_buzz for each node so this is already 28 steps total. During the while loop, each node is dequeued, another 7 steps, and its children enqueued. Total steps now with dequeueing is 35 steps. Each node is checked for children so now 42 steps, and there are two children left so now total of 44 steps. Those children are then dequeued so we are at around 46 steps. As we are check fizz buzz on each node, a new tree is also being built. We are roughly around 7^2 number of steps.

**Space complexity: O(n)**

The number of new variables created is about 8. The size of the queue expands to size of input,  and size of new tree is equal to original tree size. 3n simplified is still O(n).


## Solution
<!-- Show how to run your code, and examples of it in action -->
```zsh
pytest -k tests_tree_fizz_buzz.py
```

## Attribution
- [Class Demo # 19](https://replit.com/@kiengchay/Warm-Up-Class-19-401n8#main.py)

- [Trees documentation](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
