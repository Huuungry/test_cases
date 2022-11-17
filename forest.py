import turtle
import random

colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "orange", "pink"]


def build_tree(t, branch_length, shorten_by, angle, trunk_size, real_world_coef=False):
    if branch_length > 5:
        tree.color("brown")
        size = int(branch_length / trunk_size)
        t.pensize(size)
        t.forward(branch_length)
        if real_world_coef:
            randomizer = random.randint(int(-branch_length*0.2), int(branch_length*0.2))
            # print(randomizer_left)
        else:
            randomizer = 0
        new_length = branch_length - shorten_by + randomizer
        size = int(branch_length / 10)
        t.pensize(size)
        t.left(angle)
        build_tree(t, new_length, shorten_by, angle, trunk_size, real_world_coef)
        t.right(angle * 2)
        build_tree(t, new_length, shorten_by, angle, trunk_size, real_world_coef)
        t.left(angle)
        t.backward(branch_length)
    else:
        tree.color("green")
        t.stamp()
        tree.color("brown")


tree = turtle.Turtle()
tree.speed("fastest")
tree.hideturtle()
tree.setheading(90)
tree.penup()
tree.goto(-400, 0)

for i in range(10):
    # set the tree position in the forest and
    # draw the trees adding a random value to the branch size
    tree.penup()
    tree.goto(int(tree.xcor()) + random.randint(20, 100), -200)
    tree.pendown()
    build_tree(tree, 70, 15, 20, random.randint(5, 13), True)

turtle.mainloop()
print("done")
