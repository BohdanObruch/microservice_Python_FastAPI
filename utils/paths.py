from pathlib import Path


def path_file(data_file):
    return Path(__file__).parent.parent.joinpath(f'data/{data_file}').absolute().__str__()
