import ast
import unittest

from curve_analyzer.tests.a02.a02 import a02_curve_function
from curve_analyzer.tests.example_curves import curve_names

results = {'secp112r2': {"{'deg': 1}": {'cm_disc': -3147981784734289480448435252561803,
                                        'factorization': [[2, 2], [23, 1], [136868773249316933932540663154861, 1]],
                                        'max_conductor': 2}}, 'bn158': {
    "{'deg': 1}": {'cm_disc': -3, 'factorization': [[3, 1], [51329, 2], [8849442974123583107, 2]],
                   'max_conductor': 454233058418789397299203}}, 'brainpoolP160r1': {
    "{'deg': 1}": {'cm_disc': -4645380339943745084523443872838008326722778443,
                   'factorization': [[3, 2], [11, 2], [17, 1], [29, 1], [89, 1], [22067, 1], [577011261754261, 1],
                                     [8314894957527277176257, 1]], 'max_conductor': 33}}}


class TestA02(unittest.TestCase):

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_secp112r2(self):
        params = ast.literal_eval(list(results["secp112r2"].keys())[0]).values()
        computed_result = a02_curve_function(curve_names["secp112r2"], *params)
        self.assertEqual(computed_result, list(results["secp112r2"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_bn158(self):
        params = ast.literal_eval(list(results["bn158"].keys())[0]).values()
        computed_result = a02_curve_function(curve_names["bn158"], *params)
        self.assertEqual(computed_result, list(results["bn158"].values())[0])

    # This test has been auto-generated by gen_unittest
    def test_auto_generated_brainpoolP160r1(self):
        params = ast.literal_eval(list(results["brainpoolP160r1"].keys())[0]).values()
        computed_result = a02_curve_function(curve_names["brainpoolP160r1"], *params)
        self.assertEqual(computed_result, list(results["brainpoolP160r1"].values())[0])


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
