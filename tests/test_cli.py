"""
Unit Tests for SaidLang CLI
"""
import unittest
import sys
import os
import tempfile
from io import StringIO
from unittest.mock import patch
from saidlang.cli import main

class TestSaidLangCLI(unittest.TestCase):
    def test_cli_version(self):
        with patch('sys.argv', ['said', '--version']):
            with patch('sys.stdout', new_callable=StringIO) as fake_out:
                try:
                    main()
                except SystemExit:
                    pass
                output = fake_out.getvalue()
                self.assertIn("SaidLang", output)

    def test_cli_run_script(self):
        with tempfile.NamedTemporaryFile('w', suffix='.said', delete=False) as f:
            f.write('show "CLI Test Pass"\n')
            f_path = f.name

        try:
            with patch('sys.argv', ['said', 'run', f_path]):
                with patch('sys.stdout', new_callable=StringIO) as fake_out:
                    main()
                    self.assertIn("CLI Test Pass", fake_out.getvalue())
        finally:
            if os.path.exists(f_path):
                os.remove(f_path)

if __name__ == '__main__':
    unittest.main()
