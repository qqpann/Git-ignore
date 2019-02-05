import os
import shutil
import unittest
from test.support import captured_stdout

from click.testing import CliRunner

from git_ignore.main import main as cli
from git_ignore.main import Template


class EvacuateCustomTemplatesDir:
    def __init__(self):
        self.CUSTOM_DIR = os.path.expanduser('~/.gitignore_templates/')
        self.CUSTOM_DIR_BAK = os.path.expanduser('~/.gitignore_templates.bak/')
        self.evacuated = False

    def __enter__(self):
        if os.path.exists(self.CUSTOM_DIR):
            self.evacuated = True
            os.rename(self.CUSTOM_DIR, self.CUSTOM_DIR_BAK)

    def __exit__(self, exc_type, exc_value, traceback):
        if os.path.exists(self.CUSTOM_DIR):
            shutil.rmtree(self.CUSTOM_DIR)
        if self.evacuated:
            os.rename(self.CUSTOM_DIR_BAK, self.CUSTOM_DIR)


class TemplateTests(unittest.TestCase):
    def setUp(self):
        self.template = Template()
        self.runner = CliRunner()

    def test_template_dict_is_not_empty(self):
        self.assertTrue(self.template.TEMPLATE_DICT)

    def test_simplest_usage(self):
        with self.runner.isolated_filesystem():
            self.assertFalse('.gitignore' in os.listdir())

            self.runner.invoke(cli, ['python'])

            self.assertTrue('.gitignore' in os.listdir())

    def test_custom_template_dir(self):
        some_name = 'some_name_that_dont_exist'
        with EvacuateCustomTemplatesDir(), \
                self.runner.isolated_filesystem():
            # Test if there is no custom template defined
            self.assertFalse('.gitignore' in os.listdir())

            self.runner.invoke(cli, [some_name])

            self.assertFalse('.gitignore' in os.listdir())

            # Define custom template
            CUSTOM_DIR = os.path.expanduser('~/.gitignore_templates/')
            os.makedirs(CUSTOM_DIR)
            with open(CUSTOM_DIR + some_name + '.gitignore', 'w') as f:
                f.write('foobar')

            self.runner.invoke(cli, [some_name])

            self.assertTrue('.gitignore' in os.listdir())
            with open('.gitignore', 'r') as f:
                self.assertEqual('foobar', f.read())

    def test_stdout_add__contains_no_garbage(self):
        some_name = 'some_name_that_dont_exist'
        with EvacuateCustomTemplatesDir(), \
                self.runner.isolated_filesystem():
            # Define custom template
            CUSTOM_DIR = os.path.expanduser('~/.gitignore_templates/')
            os.makedirs(CUSTOM_DIR)
            with open(CUSTOM_DIR + some_name + '.gitignore', 'w') as f:
                f.write('foobar')

            result = self.runner.invoke(cli, ['--stdout', '-a', 'foobar'])
            stdout_str = result.output

            self.assertEqual(stdout_str, 'foobar\n')

    def test_stdout__contains_no_garbage(self):
        some_name = 'some_name_that_dont_exist'
        with EvacuateCustomTemplatesDir(), \
                self.runner.isolated_filesystem():
            # Define custom template
            CUSTOM_DIR = os.path.expanduser('~/.gitignore_templates/')
            os.makedirs(CUSTOM_DIR)
            with open(CUSTOM_DIR + some_name + '.gitignore', 'w') as f:
                f.write('foobar')

            result = self.runner.invoke(cli, ['--stdout', some_name])
            stdout_str = result.output

            self.assertEqual(stdout_str, 'foobar\n')
