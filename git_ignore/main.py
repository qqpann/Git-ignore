import os
import textwrap as tw

import click
import pkg_resources

from .__version__ import __version__


class Template:
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
        click.echo(click.style('[Hint]', fg='yellow') +
                   ' Supported templates:\n')
        supported = ', '.join(sorted(self.TEMPLATE_DICT.values()))
        click.echo(tw.indent(tw.fill(supported), '\t'))

    def write_template(self, arg):
        resource_package = __name__
        resource_path = 'template/{}.gitignore'.format(
            self.TEMPLATE_DICT[arg])
        template = pkg_resources.resource_string(
            resource_package, resource_path)

        with open('.gitignore', 'a+') as fout:
            fout.write(template.decode())


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--show', '-s', is_flag=True, help='Show supported ARGS and exit.')
@click.argument('args', nargs=-1)
@click.version_option(version=__version__)
def main(show, args):
    '''
    Create .gitignore from template.

    Specify the language etc, whose template you want to use, in ARGS.
    You can specify multiple ARGS at once.

    \b
    Example usage:
        $ git-ignore python sass
        This will create .gitignore from both templates of Python ans Sass.

    \b
    Show supported ARGS:
        $ git-ignore --show
        or
        $ git-ignore
    '''
    tem = Template()

    if show:
        tem.print_available()
        return
    elif not args:
        click.echo(click.style(
            'Arguments(ARGS) are required, but not found.\n', fg='red', bold=True))
        tem.print_available()
        return

    nomatch = list()
    matched = list()
    for arg in args:
        arg = arg.lower()
        if arg in tem.TEMPLATE_DICT:
            tem.write_template(arg)
            matched.append(arg)
        else:
            nomatch.append(arg)

    if matched:
        click.echo(click.style('[Success]', fg='green') +
                   ' Added .gitignore from template for:\n')
        added = ', '.join(matched)
        click.echo(click.style(tw.indent(tw.fill(added), '\t'), fg='green'))
        click.echo()
    if nomatch:
        click.echo(click.style('[Error]', fg='red') +
                   ' Following templates not found:\n')
        notfound = ', '.join(nomatch)
        click.echo(click.style(tw.indent(tw.fill(notfound), '\t'), fg='red'))
        click.echo()

        tem.print_available()


if __name__ == '__main__':
    main()
