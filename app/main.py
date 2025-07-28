from configuration import CONFIGURATION
from files import obtainAudioFiles
from converter import toAIFF, Path
from datetime import datetime
from logger import LOGGER
import os

def main(inputPath: str) -> None:
    """
    Main function to convert audio files to AIFF format.
    :param inputPath: Path to the directory containing audio files.
    """
    recursiveSearch = CONFIGURATION.getboolean('SEARCH', 'RECURSIVE', fallback=False)

    LOGGER.info(f"Starting conversion of audio files in: {inputPath}")

    audioFiles = obtainAudioFiles(inputPath, recursiveSearch)

    if not audioFiles:
        LOGGER.warning("No audio files found to convert.")
    else:
        LOGGER.info(f"Found {len(audioFiles)} audio files to convert.")

        timestamp = datetime.now().strftime(CONFIGURATION.get('OUTPUT', 'NEW_FOLDER_TIMESTAMP'))
        baseName = os.path.basename(os.path.normpath(inputPath))
        outputDir = os.path.join(os.path.dirname(inputPath), f"{baseName}_{timestamp}")

        for filePath in audioFiles:
            if filePath.lower().endswith('.aiff'):
                LOGGER.info(f"Skipping already converted file: {filePath}")
                continue
            if filePath.lower().endswith('.mp3'):
                LOGGER.info(f"Skipping MP3 file: {filePath}")
                continue
            try:
                convertedFile = toAIFF(Path(filePath), Path(outputDir))
            except Exception as e:
                LOGGER.error(f"Failed to convert {filePath}: {e}")
            else:
                LOGGER.info(f"Successfully converted: {filePath} → {convertedFile}")


if __name__ == "__main__":
    main(r"C:\Users\jgracia4\Documents\Musikator\music")
