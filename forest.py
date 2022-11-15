import turtle
import random

colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "orange", "pink"]


def build_tree(t, branch_length, shorten_by, angle, real_world_coef=False):
    if branch_length > 5:
        t.forward(branch_length)
        if real_world_coef:
            randomizer = random.randint(int(-branch_length*0.1), int(branch_length*0.1))
            # print(randomizer_left)
        else:
            randomizer = 0
        new_length = branch_length - shorten_by + randomizer
        t.left(angle)
        build_tree(t, new_length, shorten_by, angle, real_world_coef)
        t.right(angle * 2)
        build_tree(t, new_length, shorten_by, angle, real_world_coef)
        t.left(angle)
        t.backward(branch_length)


tree = turtle.Turtle()
tree.speed("fastest")
tree.hideturtle()
tree.setheading(90)
tree.penup()
tree.goto(-400,0)

for i in range(30):
    # select color
    tree.color(random.choice(colors))
    # set the tree position in the forest and
    # draw the trees adding a random value to the branch size
    tree.penup()
    tree.goto(int(tree.xcor()) + random.randint(20, 100), -200)
    tree.pendown()
    build_tree(tree, 70, 10, 20, True)

turtle.mainloop()
