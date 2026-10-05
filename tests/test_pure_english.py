"""
Unit Tests for Natural English Phrasing in SaidLang
"""
import unittest
from saidlang.transpiler import SaidLangTranspiler

class TestPureEnglishSyntax(unittest.TestCase):
    def setUp(self):
        self.transpiler = SaidLangTranspiler(include_runtime=False)

    def test_save_string(self):
        self.assertEqual(
            self.transpiler.transpile_line('save name as noman as string'),
            'name = "noman"'
        )

    def test_save_integer(self):
        self.assertEqual(
            self.transpiler.transpile_line('save age as 17 as integer'),
            'age = int(17)'
        )

    def test_bidirectional_save_in(self):
        self.assertEqual(
            self.transpiler.transpile_line('save 5 in number as integer'),
            'number = int(5)'
        )
        self.assertEqual(
            self.transpiler.transpile_line("save Red Mustang in rohan's car as string"),
            'rohan_s_car = "Red Mustang"'
        )

    def test_say_variable(self):
        self.assertEqual(
            self.transpiler.transpile_line('say @name'),
            'show(name)'
        )

    def test_say_interpolated_string(self):
        self.assertEqual(
            self.transpiler.transpile_line('say my name is @name and I am @age years old'),
            'show(f"my name is {name} and I am {age} years old")'
        )

    def test_possessive_say_interpolation(self):
        self.assertEqual(
            self.transpiler.transpile_line("say @name drives @name's car"),
            'show(f"{name} drives {name_s_car}")'
        )

    def test_repeat_message_n_times(self):
        self.assertEqual(
            self.transpiler.transpile_line('repeat hello world 3 times'),
            'for _ in range(3):\n    show("hello world")'
        )

    def test_dynamic_repeat_variable(self):
        self.assertEqual(
            self.transpiler.transpile_line('repeat hello @number times'),
            'for _ in range(number):\n    show("hello")'
        )
        self.assertEqual(
            self.transpiler.transpile_line('repeat congratulations @name and @name1 @count times'),
            'for _ in range(count):\n    show(f"congratulations {name} and {name1}")'
        )

    def test_compound_save_and_if_else(self):
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

    def test_multi_prompt_ask(self):
        res1 = self.transpiler.transpile_line('ask what is your name and what is your age and save in name as string and age as integer')
        self.assertEqual(
            res1,
            'name = ask("what is your name: ")\nage = int(ask_number("what is your age: "))'
        )
        res2 = self.transpiler.transpile_line('ask what is second person name and age and save in name1 as string and age1 as integer')
        self.assertEqual(
            res2,
            'name1 = ask("what is second person name: ")\nage1 = int(ask_number("what is second person age: "))'
        )

    def test_elder_older_comparison(self):
        res = self.transpiler.transpile_line('if @age is greater than @age1 then say @name is elder than @name1 else say @name1 is elder than @name')
        self.assertEqual(
            res,
            'if age > age1:\n    show(f"{name} is elder than {name1}")\nelse:\n    show(f"{name1} is elder than {name}")'
        )

if __name__ == '__main__':
    unittest.main()
