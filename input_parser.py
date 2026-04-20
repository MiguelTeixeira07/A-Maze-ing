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
