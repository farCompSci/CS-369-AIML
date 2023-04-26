import math

ATTRIBUTES = ('Alternative', 'Bar', 'Friday/Saturday', 'Hungry', 'Patrons', 'Price', 'Raining',
              'Reservation', 'Type', 'Wait')


class Datum:
    def __init__(self, target, *values):
        self.target = target
        self.attributes = dict(zip(ATTRIBUTES, values))


data = (Datum(True, True, False, False, True, 'Some', '$$$', False, True, 'French', '0-10'),
        Datum(False, True, False, False, True, 'Full', '$', False, False, 'Thai', '30-60'),
        Datum(True, False, True, False, False, 'Some', '$', False, False, 'Burger', '0-10'),
        Datum(True, True, False, True, True, 'Full', '$', True, False, 'Thai', '10-30'),
        Datum(False, True, False, True, False, 'Full', '$$$', False, True, 'French', '>60'),
        Datum(True, False, True, False, True, 'Some', '$$', True, True, 'Italian', '0-10'),
        Datum(False, False, True, False, False, 'None', '$', True, False, 'Burger', '0-10'),
        Datum(True, False, False, False, True, 'Some', '$$', True, True, 'Thai', '0-10'),
        Datum(False, False, True, True, False, 'Full', '$', True, False, 'Burger', '>60'),
        Datum(False, True, True, True, True, 'Full', '$$$', False, True, 'Italian', '10-30'),
        Datum(False, False, False, False, False, 'None', '$', False, False, 'Thai', '0-10'),
        Datum(True, True, True, True, True, 'Full', '$', False, False, 'Burger', '30-60'))


def impurity(data):
    '''
    :param data: A sequence of Datum objects.
    :return: The Gini impurity of the data, as per equation 6.1 on p. 197 of Géron.
    '''
    if len(data) == 0:
        return 0  # if there is 0 elements in the data, there is no impurity
    target_true = sum(datum.target for datum in data if datum.target == True) / len(data) # Calculates proportion of data with targets
    gini = (1 - target_true * target_true) - ((1 - target_true) * (1 - target_true)) # Gini Impurity Formula
    return gini


def split_cost(data, attribute, value):
    '''
    :param data: A sequence of Datum objects.
    :param attribute: An attribute on which to split.
    :param value: The value to distinguish from other values at this node.
    :return: The cost of splitting in this way, as per equation 6.2 on p. 200 of Géron.
    '''

    true_data = []
    false_data = []
    for datum in data:
        if datum.attributes[attribute] == value:
            true_data.append(datum)
        else:
            false_data.append(datum)
    p_true = len(true_data) / len(data)
    return p_true * impurity(true_data) + (1 - p_true) * impurity(false_data)


def best_split(data):
    best_attribute, best_value, best_cost = None, None, float('inf')
    for attribute in ATTRIBUTES:
        values = set(datum.attributes[attribute] for datum in data)
        for value in values:
            cost = split_cost(data, attribute, value)
            if cost < best_cost:
                best_attribute, best_value, best_cost = attribute, value, cost
    return best_attribute, best_value


class Tree:
    def __init__(self, data):
        # Base case: if all the data has the same target value, create a leaf node
        if len(set(datum.target for datum in data)) == 1:
            self.attribute = None
            self.value = None
            self.left = None
            self.right = None
            self.is_leaf = True
            self.target = data[0].target
            return

        # Find the best split based on the data
        attribute, value = best_split(data)

        # Split the data based on the best split
        left_data = [datum for datum in data if datum.attributes[attribute] == value]
        right_data = [datum for datum in data if datum.attributes[attribute] != value]

        # Recursively build the subtrees
        self.attribute = attribute
        self.value = value
        self.is_leaf = False
        self.left = Tree(left_data)
        self.right = Tree(right_data)

    def __repr__(self, indent=''):
        if self.is_leaf:
            return f"{indent}Leaf node with target value: {self.target}\n"
        else:
            left_str = self.left.__repr__(indent + '  ')
            right_str = self.right.__repr__(indent + '  ')
            return f"{indent}Attribute: {self.attribute}, Value: {self.value}\n{left_str}{right_str}"

    def predict(self, datum):
        if self.is_leaf:
            return self.target

        if datum.attributes[self.attribute] == self.value:
            return self.left.predict(datum)
        else:
            return self.right.predict(datum)

