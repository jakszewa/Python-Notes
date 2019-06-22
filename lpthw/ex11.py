# TAGS: input(), end=' '

print("How old are you?", end= " ")         # end=" " <- not to go on new line
age = input()

print("How tall are you?", end= " ")
height = input()                            # Here we are asking for string input
                                            # to get number do: int(input())

print("How much do you weight?", end= " ")  
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")