import os

import invoke


@invoke.task
def xdg():
    for root, dirs, files in os.walk('config'):
        for name in files:
            dst = os.path.expanduser(os.path.join('~', '.' + root, name))
            if not os.path.exists(dst):
                src = os.path.expanduser(
                    os.path.join('~', '.dotfiles', root, name))
                os.symlink(src, dst)
        for name in dirs:
            dir_path = os.path.expanduser(os.path.join('~', '.' + root, name))
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)


@invoke.task
def misc():
    for filename in os.listdir('misc'):
        dst = os.path.expanduser(os.path.join('~', '.' + filename))
        if not os.path.exists(dst):
            src = os.path.expanduser(
                os.path.join('~', '.dotfiles', 'misc', filename))
            os.symlink(src, dst)
