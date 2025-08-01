from .filtering import checkFileSampleRate
from .configuration import CONFIGURATION
from .utils import copyFileToDirectory
from .files import obtainAudioFiles
from .converter import toAIFF, Path
from datetime import datetime
from .logger import LOGGER
import os

RECURSIVE_SEARCH = CONFIGURATION.getboolean('SEARCH', 'RECURSIVE', fallback=False)
UNPACK_FILES = CONFIGURATION.getboolean('OUTPUT', 'UNPACK_FILES', fallback=False)
APPLY_FILTERING = CONFIGURATION.getboolean('FILTERING', 'ENABLED', fallback=False)

def main(inputPath: str) -> None:
    """
    Main function to convert audio files to AIFF format.
    :param inputPath: Path to the directory containing audio files.
    """
    LOGGER.info(f"Starting conversion of audio files in: {inputPath}")

    audioFiles = obtainAudioFiles(inputPath, RECURSIVE_SEARCH)

    if not audioFiles:
        LOGGER.warning("No audio files found to convert.")
    else:
        LOGGER.info(f"Found {len(audioFiles)} audio files to convert.")

        timestamp = datetime.now().strftime(CONFIGURATION.get('OUTPUT', 'NEW_FOLDER_TIMESTAMP'))
        baseName = os.path.basename(os.path.normpath(inputPath))
        outputDir = os.path.join(os.path.dirname(inputPath), f"{baseName}_{timestamp}")
        n = len(audioFiles)
        for i, filePath in enumerate(audioFiles):
            outputDir = f"{os.path.dirname(filePath)}_{timestamp}" if not UNPACK_FILES else outputDir
            audioFormat = filePath.split('.')[-1].upper()

            sampleThreshold = CONFIGURATION.getint('FILTERING', f'{audioFormat}_THRESHOLD')
            isValidSampleRate = checkFileSampleRate(filePath, sampleThreshold) if APPLY_FILTERING else True

            if isValidSampleRate:
                if APPLY_FILTERING:
                    LOGGER.info(f"File {filePath} meets the sample rate threshold {sampleThreshold} Hz")
                if filePath.lower().endswith('.aiff'):
                    LOGGER.info(f"Not converting already converted file: {filePath}")
                    copyFileToDirectory(filePath, outputDir)
                    LOGGER.info(f"Copied {filePath} to {outputDir}")
                    continue
                if filePath.lower().endswith('.mp3'):
                    LOGGER.info(f"Not converting MP3 file: {filePath}")
                    copyFileToDirectory(filePath, outputDir)
                    LOGGER.info(f"Copied {filePath} to {outputDir}")
                    continue

                try:
                    convertedFile = toAIFF(Path(filePath), Path(outputDir))
                except Exception as e:
                    LOGGER.error(f"Failed to convert {filePath}: {e}")
                else:
                    LOGGER.info(f"Successfully converted: {filePath} -> {convertedFile}")
            else:
                LOGGER.warning(f"File {filePath} does not meet the sample rate threshold {sampleThreshold} Hz.")

            yield i+1, n
