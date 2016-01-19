import invoke


@invoke.task
def theme():
    invoke.run('cat bash/profile >> ~/.bashrc')
