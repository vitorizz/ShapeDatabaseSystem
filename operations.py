from shapes import *
import sys


def load(fileName):
    print("Processing << path-to-file >> ...")
    file = open(fileName, "r")
    shapes = list()
    line_cnt = 0
    errors = 0
    for line in file:
        line_cnt += 1
        l = line.rstrip()
        words = l.split(" ")
        shape = words[0]
        if shape == "shape":
            shapes.append(Shape())
        elif shape == "circle":
            if not (words[1].isdigit() and int(words[1]) >= 0):
                errors += 1
                print("Error: Invalid {} on line {}: {} {}".format(
                    words[0].capitalize(), line_cnt, words[0], words[1]))
                continue
            shapes.append(Circle(words[1]))
        elif shape == "ellipse":
            if not (words[1].isdigit() and int(words[1]) >= 0 and words[2].isdigit() and int(words[2]) >= 0):
                errors += 1
                print("Error: Invalid {} on line {}: {} {}".format(
                    words[0].capitalize(), line_cnt, words[0], words[1], words[2]))
                continue
            shapes.append(Ellipse(words[1], words[2]))
        elif shape == "rhombus":
            if not (words[1].isdigit() and int(words[1]) >= 0 and words[2].isdigit() and int(words[2]) >= 0):
                errors += 1
                print("Error: Invalid {} on line {}: {} {}".format(
                    words[0].capitalize(), line_cnt, words[0], words[1], words[2]))
                continue
            shapes.append(Rhombus(words[1], words[2]))
    file.close()
    print("Processed {} row(s), {} shape(s) added, {} error(s).".format(
        line_cnt, len(shapes), errors))
    return shapes


def toSet(list):
    print("Multi-set is converted to a Set\n")
    shape_set = set()
    for shape in list:
        unique = True
        for element in shape_set:
            if shape.name == element.name:
                if shape.name == "Shape":
                    unique = False
                elif shape.name == "Circle":
                    if shape.radius == element.radius:
                        unique = False
                elif shape.name == "Ellipse":
                    if (shape.semiMajor == element.semiMajor) and (shape.semiMinor == element.semiMinor):
                        unique = False
                elif shape.name == "Rhombus":
                    if (shape.diagonal_1 == element.diagonal_1) and (shape.diagonal_2 == element.diagonal_2):
                        unique = False
        if unique:
            shape_set.add(shape)
    return shape_set


def print_(list):
    for shape in list:
        shape.pr()

def summary(shape_list):
    circles = sum(isinstance(shape, Circle) for shape in shape_list)
    ellipses = sum(isinstance(shape, Ellipse) for shape in shape_list)
    rhombi = sum(isinstance(shape, Rhombus) for shape in shape_list)
    shapes = sum(isinstance(shape, Shape) for shape in shape_list)
    print(f"\nCircle(s): {circles}\nEllipse(s): {ellipses}\nRhombus(es): {rhombi}\nShape(s): {shapes}\n")

def details(shape_list):
    result = ""
    for shape in shape_list:
        if isinstance(shape, Circle):
            result += shape.name + " " + str(shape.radius) + "\n"
        elif isinstance(shape, Ellipse):
            result += shape.name + " " + \
                str(shape.semiMajor) + " " + str(shape.semiMinor) + "\n"
        elif isinstance(shape, Rhombus):
            result += shape.name + " " + \
                str(shape.diagonal_1) + " " + str(shape.diagonal_2) + "\n"
        else:
            result += shape.name + "\n"
    return result


def save(fileName, list):
    f = open(fileName, "w")
    f.write(details(list))
    print("Processed database into new file called " + fileName)


def quit():
    print("Quitting program")
    sys.exit(0)
