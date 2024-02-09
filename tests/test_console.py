#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def test_show_missing_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_show("")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_show_missing_id(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_show("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_show_instance_not_found(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_show("BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** no instance found **", output)

    def test_precmd_empty_line(self):
        line = ''
        result = self.hbnb_command.precmd(line)
        self.assertEqual(result, line)

    def test_precmd_valid_command(self):
        line = 'BaseModel.show(123)'
        result = self.hbnb_command.precmd(line)
        self.assertEqual(result, "show BaseModel 123")

    def test_precmd_invalid_command(self):
        line = 'InvalidClass.invalid_method(123)'
        result = self.hbnb_command.precmd(line)
        self.assertEqual(result, line)

    def test_do_destroy_missing_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_destroy("")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_do_destroy_missing_id(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_destroy("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_do_destroy_class_not_exist(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.do_destroy("InvalidClass 123")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.emptyline()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_quit(self):
        result = self.hbnb_command.do_quit("")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
