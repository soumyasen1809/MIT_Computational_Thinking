# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec1.pdf


class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def getDensity(self):
        return self.getValue()/(1.0*self.getCost())

    def __str__(self):
        return self.name


def menu(name, value, calories):
    menu = []

    for index in range(len(value)):
        menu.append(Food(name[index], value[index], calories[index]))

    return menu


def greedy(item, maxcost, keyFunction):
    itemcopy = sorted(item, key=keyFunction, reverse=True)
    result = []
    totalcost, totalvalue = 0.0, 0.0

    for index in range(len(itemcopy)):
        if (totalcost + itemcopy[index].getCost()) <= maxcost:
            result.append(itemcopy[index])
            totalcost = totalcost + itemcopy[index].getCost()
            totalvalue = totalvalue + itemcopy[index].getValue()

    print("Total value is: {}".format(totalvalue))
    for index in result:
        print (index)
    return 0


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

food = menu(names, values, calories)

print('By value')
greedy(food, 800, Food.getValue)

print('By cost')
greedy(food, 800, lambda x: 1.0/(1.0*Food.getCost(x)))  # Use lambda x when operations are involved

print('By density')
greedy(food, 800, Food.getDensity)
