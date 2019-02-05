import os
import unittest

from click.testing import CliRunner

from git_ignore.main import main as cli
from git_ignore.main import Template


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
