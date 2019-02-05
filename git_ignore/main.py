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

    def __init__(self):
        self.TEMPLATE_DICT = dict()

        # lst = os.listdir('./ignore_template/')
        resource_package = __name__
        resource_path = 'template'
        lst = pkg_resources.resource_listdir(
            resource_package, resource_path)
        # print(lst)
        for n in lst:
            if n[-10:] == '.gitignore':
                self.TEMPLATE_DICT[n[:-10].lower()] = n[:-10]

    def print_available(self):
        echo_status(
            'Hint', 'Supported templates:',
            ', '.join(sorted(self.TEMPLATE_DICT.values())),
            use_default_color=True)

    def write_template(self, arg):
        resource_package = __name__
        resource_path = 'template/{}.gitignore'.format(
            self.TEMPLATE_DICT[arg])
        template = pkg_resources.resource_string(
            resource_package, resource_path)

        with open('.gitignore', 'a+') as fout:
            fout.write(template.decode())

    def proceed_args(self, args):
        nomatch = list()
        matched = list()
        for arg in args:
            arg = arg.lower()
            if arg in self.TEMPLATE_DICT:
                self.write_template(arg)
                matched.append(arg)
            else:
                nomatch.append(arg)

        if matched:
            echo_status(
                'Success', 'Added .gitignore from template for:', ', '.join(matched))
        if nomatch:
            echo_status(
                'Error', 'Following templates not found:', ', '.join(nomatch))
            self.print_available()


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--list', '-l', '_list', is_flag=True, help='List supported ARGS and exit.')
@click.argument('args', nargs=-1)
@click.version_option(version=__version__)
def main(_list, args):
    '''
    Create .gitignore from template.

    Specify the language etc, whose template you want to use, in ARGS.
    You can specify multiple ARGS at once.

    \b
    Example usage:
        $ git-ignore python sass
        This will create .gitignore from both templates of Python ans Sass.

    \b
    List supported ARGS:
        $ git-ignore --list
        or
        $ git-ignore
    '''
    tem = Template()

    if _list:
        tem.print_available()
        return
    elif not args:
        echo_status('Error', 'Arguments(ARGS) are required, but not found.', '')
        tem.print_available()
        return

    tem.proceed_args(args)


if __name__ == '__main__':
    main()
