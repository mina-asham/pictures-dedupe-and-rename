from mock import call


def calls_from(list_args):
    return [call(*args) for args in list_args]
