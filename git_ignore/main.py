import os
import textwrap as tw

import click
import pkg_resources

from .__version__ import __version__


def echo_status(status, title, text, use_default_color=False):
    status_color = {
        'Success': 'green',
        'Error': 'red',
        'Hint': 'yellow',
    }
    if status not in status_color.keys():
        raise Exception('Wrong status code')
    color = status_color[status]
    text_color = None if use_default_color else color

    click.echo(click.style(f'[{status}]', fg=color) + f' {title}\n')
    if text:
        click.echo(
            click.style(tw.indent(tw.fill(text), '\t'), fg=text_color) + '\n'
        )


class Template:
    '''Functions related to manipulating template'''

    def __init__(self, to_stdout=False, no_custom=False):
        self.to_stdout = to_stdout
        self.no_custom = no_custom
        self.CUSTOM_DIR = os.path.expanduser('~/.gitignore_templates/')
        self.TEMPLATE_DICT = dict()
        self.CUSTOM_TEMPLATE_DICT = dict()

        if not no_custom and os.path.exists(self.CUSTOM_DIR):
            custom_lst = os.listdir(self.CUSTOM_DIR)
            self.CUSTOM_TEMPLATE_DICT = {
                n[:-10].lower(): n[:-10] for n in custom_lst}

        resource_package = __name__
        resource_path = 'template'
        lst = pkg_resources.resource_listdir(
            resource_package, resource_path)
        # print(lst)
        for n in lst:
            if n[-10:] == '.gitignore':
                self.TEMPLATE_DICT[n[:-10].lower()] = n[:-10]

    def print_available(self):
        if not self.no_custom:
            if self.CUSTOM_TEMPLATE_DICT:
                echo_status(
                    'Hint', 'Your custom templates:',
                    ', '.join(sorted(self.CUSTOM_TEMPLATE_DICT.values())),
                    use_default_color=True)
            else:
                echo_status(
                    'Hint', 'Your custom templates:',
                    ('Not found. You can add custom templates by adding to '
                     '~/.gitignore_templates/some_name.gitignore '
                     'And use it with '
                     '$git-ignore some_name'),
                    use_default_color=True)
        echo_status(
            'Hint', 'Supported templates:',
            ', '.join(sorted(self.TEMPLATE_DICT.values())),
            use_default_color=True)

    def get_template_str(self, arg):
        resource_package = __name__
        resource_path = 'template/{}.gitignore'.format(
            self.TEMPLATE_DICT[arg])
        template = pkg_resources.resource_string(
            resource_package, resource_path)
        return template.decode()

    def get_custom_template_str(self, arg):
        with open(self.CUSTOM_DIR + '{}.gitignore'.format(self.CUSTOM_TEMPLATE_DICT[arg])) as f:
            template = f.read()
        return template

    def write_template(self, file_str):
        if self.to_stdout:
            click.echo(file_str)
        else:
            # TODO: use click.echo
            # NOTE: click.echo may not support a+ addition.
            with open('.gitignore', 'a+') as fout:
                fout.write(file_str)

    def proceed_addition(self, args):
        file_str = '\n'.join(args)
        self.write_template(file_str)

    def proceed_args(self, args):
        nomatch = list()
        matched = list()
        for arg in args:
            arg = arg.lower()
            if arg in self.TEMPLATE_DICT:
                template_file_str = self.get_template_str(arg)
                self.write_template(template_file_str)
                matched.append(arg)
            elif arg in self.CUSTOM_TEMPLATE_DICT:
                template_file_str = self.get_custom_template_str(arg)
                self.write_template(template_file_str)
                matched.append(arg)
            else:
                nomatch.append(arg)

        if self.to_stdout:
            return
        if matched:
            echo_status(
                'Success', 'Added .gitignore from template for:', ', '.join(matched))
        if nomatch:
            echo_status(
                'Error', 'Following templates not found:', ', '.join(nomatch))
            self.print_available()


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--list', '-l', 'list_up', is_flag=True, help='List up supported ARGS and exit.')
@click.option('--add', '-a', 'add', is_flag=True, help='Add args as new lines to .gitignore.')
@click.option('--no-custom', 'no_custom', is_flag=True, help='Do not use custom .gitignore_template/ folder.')
@click.option('--stdout', 'to_stdout', is_flag=True, help='Output to STDOUT.')
@click.argument('args', nargs=-1)
@click.version_option(version=__version__)
def main(list_up, add, no_custom, to_stdout, args):
    '''
    Create .gitignore from template.

    Specify the language etc, whose template you want to use, in ARGS.
    You can specify multiple ARGS at once.

    \b
    Example usage:
        $ git-ignore python sass
        This will create .gitignore from both templates of Python ans Sass.

    \b
    List up supported ARGS:
        $ git-ignore --list
        or
        $ git-ignore

    \b
    Add new lines as you wish:
        $ git-ignore --add .gitignore
        This will add .gitignore to your .gitignore file.
        or
        $ git-ignore -a !.keep !.gitkeep
        This will add !.keep and !.gitkeep as new lines to your .gitignore

    \b
    Output to stdout if you want to:
        $ git-ignore --stdout python >> .gitignore
        You don\'t need to, but you can do this to use more freely.
    '''
    template = Template(to_stdout, no_custom)

    if list_up:
        template.print_available()
        return
    if add:
        if not args:
            echo_status(
                'Error', 'Arguments(ARGS) are required, but not found.', '')
            return
        template.proceed_addition(args)
        return

    if not args:
        echo_status('Error', 'Arguments(ARGS) are required, but not found.', '')
        template.print_available()
        return
    template.proceed_args(args)


if __name__ == '__main__':
    main()
