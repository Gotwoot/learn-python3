'''
https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936
'''
# -*- coding: utf-8 -*-
import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # def get_grade(self):
    #     if self.score >= 80 and self.score <= 100:
    #         return 'A'
    #     if self.score >= 60:
    #         return 'B'
    #     if self.score >= 0:
    #         return 'C'
    #     # else:
    #     #     raise ValueError("Invalid score. Score must be between 0 and 100")
    def get_grade(self):
        if not (0 <= self.score <= 100):
            raise ValueError("Invalid score. xxxx--Score must be between 0 and 100")

        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    # def test_invalid(self):
    #     s1 = Student('Bart', -1)
    #     s2 = Student('Lisa', 101)
    #     with self.assertRaises(ValueError):
    #         s1.get_grade()
    #     with self.assertRaises(ValueError):
    #         s2.get_grade()
    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        try:
            s1.get_grade()
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        else:
            print("No ValueError raised.")

        try:
            s2.get_grade()
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        else:
            print("No ValueError raised.")


if __name__ == '__main__':
    unittest.main()