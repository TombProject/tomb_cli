import sys

from tomb_cli.__about__ import __version__
from cliff.app import App
from cliff.command import Command
from cliff.commandmanager import CommandManager


class Simple(Command):
    "A simple command that prints a message."

    def take_action(self, parsed_args):
        self.app.echo('hi!')


class TombApp(App):
    def __init__(self):
        super().__init__(
            description='Tomb CLI',
            version=__version__,
            command_manager=CommandManager('tomb'),
            deferred_help=True,
        )
        self.logger = self.LOG
        self.command_manager.add_command('simple', Simple)

    def echo(self, msg):
        self.stdout.write('{0}\n'.format(msg))


def main(argv=sys.argv[1:]):
    myapp = TombApp()
    return myapp.run(argv)
