from typing import Any


def get_flags(file_path: str) -> dict[str, Any]:
    FLAGS = {
        'WIDTH': int,
        'HEIGHT': int,
        'ENTRY': lambda x, y: (int(x), int(y)),
        'EXIT': lambda x, y: (int(x), int(y)),
        'OUTPUT_FILE': str,
        'PERFECT': bool
    }

    with open(file_path) as input_file:
        flags = {}
        while input_file.readline():
            line = input_file.readline()
            if line[0] == '#':
                continue

            for flag in FLAGS:
                if flag not in line:
                    continue

                str_value = line[len(flag) + 1]
                value = FLAGS[flag](str_value)
                flags.update({flag: value})

    return flags
