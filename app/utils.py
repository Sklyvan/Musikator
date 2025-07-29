from mutagen.flac import FLAC
from mutagen.aiff import AIFF
from mutagen.wave import WAVE
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from .logger import LOGGER
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


def copyMetadata(originalFile: str, newFile: str) -> None:
    """
    Copies metadata from the original audio file to the new AIFF file.
    :param originalFile: Path to the original audio file.
    :param newFile: Path to the new AIFF file.
    :return: None
    """
    audioFormat, tags = os.path.splitext(originalFile)[1].upper(), None

    # Read tags from original file
    if audioFormat == ".MP3":
        audio = MP3(originalFile)
        tags = audio.tags
    elif audioFormat == ".FLAC":
        audio = FLAC(originalFile)
        tags = audio.tags
    elif audioFormat == ".M4A":
        audio = MP4(originalFile)
        tags = audio.tags
    elif audioFormat == ".WAV":
        audio = WAVE(originalFile)
        tags = audio.tags
    elif audioFormat == ".AIFF":
        audio = AIFF(originalFile)
        tags = audio.tags
    else:
        LOGGER.warning(f"Unsupported audio format: {audioFormat}. No metadata will be copied.")
        return None

    # Write tags to new AIFF file
    aiff = AIFF(newFile)
    if aiff.tags is None:
        aiff.add_tags()

    # Copy supported tags
    for key, value in tags.items():
        try:
            aiff.tags[key] = value
        except Exception as e:
            LOGGER.warning(f"Failed to copy tag {key} with value {value} to AIFF: {e}")
    else:
        LOGGER.info(f"Copied all metadata from {originalFile} to {newFile}")

    aiff.save()

    return None
