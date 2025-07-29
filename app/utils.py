import shutil
import os

def copyFileToDirectory(filePath: str, targetDir: str) -> None:
    """
    Copies a file to the specified directory.
    :param filePath: Path of the file to copy.
    :param targetDir: Directory where the file should be copied.
    """
    if not os.path.isfile(filePath):
        raise FileNotFoundError(f"File does not exist: {filePath}")
    else:
        os.makedirs(targetDir, exist_ok=True)
        shutil.copy(filePath, targetDir)
