def draw_tree(height):
  for i in range(1, height + 1):
    for j in range(height - i):
      print(" ", end="")
    for j in range(2 * i - 1):
      print("*", end="")
    print()
draw_tree(15)