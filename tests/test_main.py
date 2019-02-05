import unittest

from git_ignore.main import Template


class TemplateTests(unittest.TestCase):
    def setUp(self):
        self.template = Template()

    def test_template_dict_is_not_empty(self):
        print(self.template.TEMPLATE_DICT)
        self.assertTrue(self.template.TEMPLATE_DICT)
