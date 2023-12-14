# Challenge Title
Create a class called AnimalShelter which holds only dogs
and cats. The shelter operates using a FIFO approach so it is a queue-like structure.

## Whiteboard Process


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Time: for enqueue, the time complexity is 4 steps when queue is empty and still 4 steps when queue is not empty. Since this appears constant, the time complexity is O(1)

Space: for enqueue, the space complexity for worst case also appears constant therefore it is O(1)

Time: for dequeue, the time complexity is O(n * m) because it has to traverse the queue and it could possibly traverse the entire length of the queue, and for each traversal it has to perform so many steps along the way. n is the number of traversals and m is the number of steps for each traversal.

Space: for dequeue, the space complexity is constant therefore O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->

## Attribution
[ChatGPT](https://chat.openai.com/c/bb30f64c-9ca8-40dc-b8c6-aee601cc3b73)

I did not utilize ChatGPT this time around.
