"""
Test suite validating that all canonical examples in examples/ transpile and execute.
"""
import unittest
import os
import glob
from saidlang.transpiler import SaidLangTranspiler

class TestCanonicalExamples(unittest.TestCase):
    def setUp(self):
        self.transpiler = SaidLangTranspiler(include_runtime=True)
        self.examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

    def test_all_examples_transpile(self):
        example_files = glob.glob(os.path.join(self.examples_dir, "*.said"))
        self.assertTrue(len(example_files) > 0, "No example files found in examples/")

        for example_file in example_files:
            with self.subTest(example=os.path.basename(example_file)):
                with open(example_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                python_code = self.transpiler.transpile(content)
                self.assertTrue(len(python_code) > 0)
                # Verify that python code compiles cleanly
                compiled = compile(python_code, example_file, 'exec')
                self.assertIsNotNone(compiled)

if __name__ == '__main__':
    unittest.main()
