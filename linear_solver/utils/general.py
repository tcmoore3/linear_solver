import os
from pkg_resources import resource_filename


def get_fn(name):
    """Get the full path to one of the reference files shipped for testing.

    This function is taken straight from MDTraj (see https://github.com/mdtraj/mdtraj).
    In the source distribution, these files are in ``linear_solver/testing/reference``,
    but on istallation, they're moved to somewhere in the user's python
    site-packages directory.

    Parameters
    ----------
    name : str
        Name of the file to load (with respecto to the ``reference/`` directory).

    Examples
    ________
    >>> import linear_solver as ls
    >>> x = ls.solve_linear_system(get_fn('coeffs.txt'), get_fn('consts.txt'))
    """

    fn = resource_filename('linear_solver', os.path.join('testing', 'reference', name))

    if not os.path.exists(fn):
        raise ValueError('Sorry! %s does not exist. If you just '
                         'added it, you\'ll have to re install' % fn)

    return fn
