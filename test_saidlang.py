"""
Unit Tests for SaidLang Transpiler and Runtime
"""

import unittest
from saidlang.transpiler import SaidLangTranspiler

class TestSaidLangTranspiler(unittest.TestCase):
    def setUp(self):
        self.transpiler = SaidLangTranspiler(include_runtime=False)

    def test_show_and_say(self):
        self.assertEqual(self.transpiler.transpile_line('show "Hello world"'), 'show("Hello world")')
        self.assertEqual(self.transpiler.transpile_line('say 42'), 'show(42)')

    def test_variable_assignment(self):
        self.assertEqual(self.transpiler.transpile_line('set score to 100'), 'score = 100')
        self.assertEqual(self.transpiler.transpile_line('make age = 20'), 'age = 20')
        self.assertEqual(self.transpiler.transpile_line('let name be "Ali"'), 'name = "Ali"')

    def test_increase_decrease(self):
        self.assertEqual(self.transpiler.transpile_line('increase score by 10'), 'score += 10')
        self.assertEqual(self.transpiler.transpile_line('decrease lives by 1'), 'lives -= 1')

    def test_conditionals(self):
        self.assertEqual(self.transpiler.transpile_line('if age is greater than 18:'), 'if age > 18:')
        self.assertEqual(self.transpiler.transpile_line('otherwise if score is equal to 100:'), 'elif score == 100:')
        self.assertEqual(self.transpiler.transpile_line('otherwise:'), 'else:')

    def test_loops(self):
        self.assertEqual(self.transpiler.transpile_line('repeat 5 times:'), 'for _ in range(5):')
        self.assertEqual(self.transpiler.transpile_line('repeat 3 times with i:'), 'for i in range(3):')
        self.assertEqual(self.transpiler.transpile_line('count from 1 to 10 as num:'), 'for num in range(1, (10) + 1):')
        self.assertEqual(self.transpiler.transpile_line('for each item in basket:'), 'for item in basket:')

    def test_functions(self):
        self.assertEqual(self.transpiler.transpile_line('to greet with name:'), 'def greet(name):')
        self.assertEqual(self.transpiler.transpile_line('to add with a and b:'), 'def add(a, b):')
        self.assertEqual(self.transpiler.transpile_line('give back a + b'), 'return a + b')

    def test_file_operations(self):
        self.assertEqual(
            self.transpiler.transpile_line('write "Hello" into file "test.txt"'),
            'write_file("test.txt", "Hello")'
        )
        self.assertEqual(
            self.transpiler.transpile_line('read file "test.txt" into data'),
            'data = read_file("test.txt")'
        )
        self.assertEqual(
            self.transpiler.transpile_line('append "New line" to file "test.txt"'),
            'append_file("test.txt", "New line")'
        )

    def test_random_and_picker(self):
        self.assertEqual(
            self.transpiler.transpile_line('random number between 1 and 100 into num'),
            'num = random_number(1, 100)'
        )
        self.assertEqual(
            self.transpiler.transpile_line('pick random from colors into chosen'),
            'chosen = pick_random(colors)'
        )

    def test_error_handling(self):
        self.assertEqual(self.transpiler.transpile_line('attempt:'), 'try:')
        self.assertEqual(self.transpiler.transpile_line('on error as err:'), 'except Exception as err:')
        self.assertEqual(self.transpiler.transpile_line('on error:'), 'except Exception:')

    def test_string_split(self):
        self.assertEqual(
            self.transpiler.transpile_line('split tags by "," into tag_list'),
            'tag_list = tags.split(",")'
        )

    def test_pure_english_save_and_say(self):
        self.assertEqual(
            self.transpiler.transpile_line('save name as noman as string'),
            'name = "noman"'
        )
        self.assertEqual(
            self.transpiler.transpile_line('save age as 17 as integer'),
            'age = int(17)'
        )
        self.assertEqual(
            self.transpiler.transpile_line('say @name'),
            'show(name)'
        )
        self.assertEqual(
            self.transpiler.transpile_line('say my name is @name and I am @age years old'),
            'show(f"my name is {name} and I am {age} years old")'
        )

    def test_pure_english_repeat(self):
        self.assertEqual(
            self.transpiler.transpile_line('repeat i have a boyfriend 3 times'),
            'for _ in range(3):\n    show("i have a boyfriend")'
        )

    def test_pure_english_multiple_save_and_if_else(self):
        res_save = self.transpiler.transpile_line("save rohan's age as 15 as integer and mohan's age as 16 as integer")
        self.assertEqual(
            res_save,
            'rohan_s_age = int(15)\nmohan_s_age = int(16)'
        )
        res_if = self.transpiler.transpile_line("if rohan's age is bigger than mohan's age then say rohan is bigger else say mohan is bigger")
        self.assertEqual(
            res_if,
            'if rohan_s_age > mohan_s_age:\n    show("rohan is bigger")\nelse:\n    show("mohan is bigger")'
        )

    def test_string_literal_preservation(self):
        # Human operators inside strings must NOT be modified
        line = 'show "This is greater than that"'
        self.assertEqual(self.transpiler.transpile_line(line), 'show("This is greater than that")')

if __name__ == '__main__':
    unittest.main()

