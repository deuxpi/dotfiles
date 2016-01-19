import os

import invoke

from . import bash
from . import config


@invoke.task
def setup():
    dotfiles_dir = os.path.join(os.path.dirname(__file__), '..')
    home_dotfiles = os.path.expanduser('~/.dotfiles')
    if not os.path.exists(home_dotfiles):
        os.symlink(os.path.abspath(dotfiles_dir), home_dotfiles)


@invoke.task(setup, config.xdg, config.misc, bash.theme)
def install():
    pass


ns = invoke.Collection(install, bash, config)
