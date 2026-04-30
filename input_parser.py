from typing import Any


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
    FLAGS = {
        'WIDTH': int,
        'HEIGHT': int,
        'ENTRY': lambda v: (int(v.split(',')[0]), int(v.split(',')[1])),
        'EXIT': lambda v: (int(v.split(',')[0]), int(v.split(',')[1])),
        'OUTPUT_FILE': str,
        'PERFECT': bool
    }

    with open(config_file_path, 'r') as config_file:
        flags: dict[str, Any] = {}
        for line in config_file:
            if line[0] == '#':
                continue

            for flag, action in FLAGS.items():
                if not line[:len(flag)] == flag:
                    if flag == 'PERFECT':
                        raise SyntaxError('Invalid syntax')
                    continue

                str_value: str = line[len(flag) + 1:]
                value: Any = action(str_value.strip('\n'))
                flags.update({flag.lower(): value})
                break

    return flags


def verify_flags(flags: dict[str, Any]) -> bool:
    if flags['width'] < 1 or flags['height'] < 1:
        return False

    if flags['width'] > 40 or flags['width'] < 9:
        return False
    if flags['height'] > 40 or flags['height'] < 7:
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
