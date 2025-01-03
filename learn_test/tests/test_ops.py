import unittest

# import os,sys
# sys.path.append(os.path.abspath('..'))
from src.example.ops import add, sub, mul, div, async_add


class TestExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """vipolniaetsia pered vsima testamy odin raz"""

    @classmethod
    def tearDownClass(cls):
        """vipolniaetsia poslie vsih testiv odin raz"""

    def setUp(self):
        """vipolniaetsia pered cagdim testom"""

    def tearDown(self):
        """vipilniaetsia poslie cagdogo testa"""

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)

    # @unittest.skip('byde skipat ietot test')
    def test_div(self):
        self.assertAlmostEqual(div(2, 3), 0.66666666)  # pohti sovapaiet? need 7 simvol
        with self.assertRaises(ZeroDivisionError) as cm:
            div(3, 0)


class TestAsync(unittest.IsolatedAsyncioTestCase):
    async def test_add(self):
        r = await async_add(2, 3)
        self.assertEqual(r, 5)


if __name__ == "__main__":
    unittest.main()
