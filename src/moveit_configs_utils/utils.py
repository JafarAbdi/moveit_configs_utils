import yaml
from pathlib import Path


class MoveItConfigFileNotFoundError(KeyError):
    pass


def load_file(file_path: Path):
    if not file_path.exists():
        raise MoveItConfigFileNotFoundError(f"File {file_path} doesn't exists")
    try:
        with open(file_path, "r") as file:
            return file.read()
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return None


def load_yaml(file_path: Path):
    if not file_path.exists():
        raise MoveItConfigFileNotFoundError(f"File {file_path} doesn't exists")

    try:
        with open(file_path, "r") as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        return None
