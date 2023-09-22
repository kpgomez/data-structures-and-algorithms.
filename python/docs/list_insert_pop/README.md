# Challenge Title
list insert pop (I may have misunderstood the problem domain.
I would rename this branch/directory to list insert middle if I could)

## Whiteboard Process

![img.png](img.png)

## Approach & Efficiency
?? What does this mean ??

## Solution

def insert_middle_list(list=[], value):
  if len(list) % 2 == 0:
    list = list.insert((len(list)/2), value)
  if len(list) % 2 != 0:
    list = list.insert(((len(list)/2)+1), value)
  return list


## Attribution

[ChatGPT Big O of built-in functions](https://chat.openai.com/share/b04b5657-ccb0-475f-a311-8f6032719ed3)


