#037
#049
#52
#66

from c07_web16_review import *
import unittest 


class TestReview(unittest.TestCase):

    def test_km_to_mile_valid(self):
        valid = [0, 10, 5.0, 3.2]
        for v in valid:
            self.assertAlmostEqual(km_to_mile(v), v * 0.621371192, 5)

    def test_km_to_mile_neg(self):
        invalid = [-4, -10, -5.0, -7.2]
        for v in invalid:
            with self.assertRaises(ValueError):
                km_to_mile(v)

    def test_consecutive_char_ConsecutiveChar(self):
        valid = ['hello','week','mass']
        for value in valid:
            self.assertTrue(consecutive_char(value))

    def test_consecutive_char_NotConsecutive(self):
        invalid = ['new','make']
        for value in invalid:
            self.assertFalse(consecutive_char(value))

    def test_duplicate_Duplicate(self):
        valid = ['need','soo']
        for value in valid:
            self.assertTrue(duplicate(value))
    def test_duplicate_NotDuplicate(self):
        invalid = ['so','do','go']
        for value in invalid:
            self.assertFalse(duplicate(value))
    def test_x_is_MaxValue(self):
        value = [(300,200,100,300),(500,300,200,500)]
        for x,y,z,Maxvalue in value:
            self.assertEqual(max_value(x,y,z),Maxvalue)
    def test_y_is_MaxValue(self):
        value = [(200,300,100,300),(300,500,200,500)]
        for x,y,z,Maxvalue in value:
            self.assertEqual(max_value(x,y,z),Maxvalue)
    def test_z_is_MaxValue(self):
        value = [(200,100,300,300),(300,200,500,500)]
        for x,y,z,Maxvalue in value:
            self.assertEqual(max_value(x,y,z),Maxvalue)
    def test_All_is_equal(self):
        value = [(200,200,200,200),(300,300,300,300)]
        for x,y,z,Maxvalue in value:
            self.assertEqual(max_value(x,y,z),Maxvalue)
    def test_two_is_equal(self):
        value = [(200,200,100,200),(300,300,100,300)]
        for x,y,z,Maxvalue in value:
            self.assertEqual(max_value(x,y,z),Maxvalue)
    
    

if __name__ == '__main__':
    unittest.main()
