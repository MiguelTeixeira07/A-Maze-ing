from typing import Any
from collections.abc import Callable


def get_flags(config_file_path: str) -> dict[str, Any]:
    """Parses the configuration file.

    Scans the file line by line ignoring comments (lines started with #).
    If a line doesnt start with a keyword or a '#' it's interpreted as a
    syntax error.

    Args:
        config_file_path (str): Path of configuration file.

    Returns:
        dict[str, Any]: Dict with the flag as key and its corresponding value.

    Raises:
        SyntaxError: Is raised when a line that is not a comment doesn't
        contain a flag on the beginning.
    """
    OPERATE: dict[str, Callable[[str], tuple[int, int] | int | str | bool]] = {
        'WIDTH': int,
        'HEIGHT': int,
        'ENTRY': lambda v: (int(v.split(',')[0]), int(v.split(',')[1])),
        'EXIT': lambda v: (int(v.split(',')[0]), int(v.split(',')[1])),
        'OUTPUT_FILE': str,
        'PERFECT': lambda v: v == 'True'
    }

    with open(config_file_path, 'r') as config_file:
        flags: dict[str, Any] = {}
        seen: list[str] = []
        for line in config_file:
            if line[0] == '#':
                continue

            flag, str_value = line.split('=')
            if ' ' in str_value:
                raise SyntaxError
            if (
                flag in ('ENTRY', 'EXIT') and
                (
                    len(str_value.split(',')) != 2 or
                    not str_value.split(',')[0].isdigit() or
                    not str_value.split(',')[1].strip('\n').isdigit()
                )
            ):
                raise SyntaxError
            if (
                flag == 'OUTPUT_FILE' and
                (
                    len(str_value.split('.')) != 2 or
                    str_value.split('.')[1].strip('\n') != 'txt'
                )
            ):
                raise SyntaxError
            if (
                flag == 'PERFECT' and
                str_value.strip('\n') not in ('True', 'False')
            ):
                raise SyntaxError

            if flag in seen:
                raise SyntaxError

            seen.append(flag)
            value: Any = OPERATE[flag](str_value.strip('\n'))
            flags.update({flag.lower(): value})

    return flags


def verify_flags(flags: dict[str, Any]) -> bool:
    """Checks if every value is valid for every flag.

    Does a bunch of checks for each flag to see if every single on of them is
    valid and will let the rest of the progeam run without crashes related to
    flags.

    Args:
        flags (dict[str, Any]): Dictionary containing all of the flags.

    Returns:
        bool: False if there are errors with any flag, otherwise returns True.
    """
    if len(flags) != 6:
        return False

    if flags['width'] < 1 or flags['height'] < 1:
        return False

    if flags['width'] > 40 or flags['width'] < 9:
        return False
    if flags['height'] > 20 or flags['height'] < 7:
        return False
    if flags['entry'] == flags['exit']:
        return False

    if flags['entry'][0] < 0 or flags['entry'][1] < 0:
        return False
    if flags['exit'][0] < 0 or flags['exit'][1] < 0:
        return False

    if flags['entry'][0] >= flags['width']:
        return False
    if flags['entry'][1] >= flags['height']:
        return False

    if flags['exit'][0] >= flags['width']:
        return False
    if flags['exit'][1] >= flags['height']:
        return False

    if flags['output_file'][len(flags['output_file']) - 4:] != '.txt':
        return False

    return True
