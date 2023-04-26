from unittest import TestCase
from decision_tree import *


class Test(TestCase):
    def test_detects_purity(self):
        d = [Datum(True)]
        self.assertAlmostEqual(0.0, impurity(d))

    def test_detects_even_impurity(self):
        d = [Datum(True)] * 5 + [Datum(False)] * 5
        self.assertAlmostEqual(0.5, impurity(d))

    def test_detects_uneven_impurity(self):
        d = [Datum(True)] * 3 + [Datum(False)]
        self.assertAlmostEqual(6/16, impurity(d))

    def test_computes_split_cost(self):
        result = split_cost(data, 'Raining', False)
        self.assertAlmostEqual(0.4857, result, delta=0.001)

    def test_finds_best_split(self):
        a, v = best_split(data)
        self.assertEqual('Patrons', a)
        self.assertEqual('Some', v)

    def test_predicts_all_training_examples_correctly(self):
        tree = Tree(data)
        for d in data:
            self.assertEqual(d.target, tree.predict(d))
