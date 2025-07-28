from configuration import CONFIGURATION
from logger import LOGGER
import os

AUDIO_FILE_EXTENSIONS = tuple(eval(CONFIGURATION.get('SEARCH', 'ACCEPTED_EXTENSIONS')))

def obtainAudioFiles(fromDir: str, recursiveSearch: bool = False) -> list[str]:
    """
    Obtains a list of audio files from the specified directory. The directory is defined in the configuration file.
    :param fromDir: Directory to search for audio files.
    :param recursiveSearch: If True, searches recursively in subdirectories.
    :return: List of audio file paths.
    """
    if not os.path.isdir(fromDir):
        LOGGER.error(f"Directory does not exist: {fromDir}")
        return []
    else:
        audioFiles = []
        if recursiveSearch:
            LOGGER.debug(f"Searching recursively in directory: {fromDir}")
            for root, _, files in os.walk(fromDir):
                for file in files:
                    filePath = os.path.join(root, file)
                    if os.path.isfile(filePath) and file.upper().endswith(AUDIO_FILE_EXTENSIONS):
                        audioFiles.append(filePath)
                        LOGGER.debug(f"Found audio file: {file}")
        else:
            LOGGER.debug(f"Searching in directory: {fromDir}")
            for file in os.listdir(fromDir):
                filePath = os.path.join(fromDir, file)
                if os.path.isfile(filePath) and file.upper().endswith(AUDIO_FILE_EXTENSIONS):
                    audioFiles.append(filePath)
                    LOGGER.debug(f"Found audio file: {file}")

    LOGGER.info(f"Found {len(audioFiles)} audio files in {fromDir}")

    return audioFiles
