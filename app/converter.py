from configuration import FFMPEG_PATH
from logger import LOGGER
from pathlib import Path
import subprocess

CODEC = "pcm_s16be"

def toAIFF(inputPath: Path, outputDir: Path) -> Path:
    """
    Converts an audio file to AIFF format using ffmpeg. The input file can be in any format supported by ffmpeg.
    :param inputPath: Path to the input audio file.
    :param outputDir: Directory where the converted AIFF file will be saved.
    :return: Path to the converted AIFF file.
    :raises FileNotFoundError: If the input file does not exist.
    :raises RuntimeError: If ffmpeg fails to convert the file.
    :raises Exception: For any other exceptions that may occur during the conversion.
    """
    if not inputPath.exists():
        raise FileNotFoundError(f"Input file not found: {inputPath}")

    if not outputDir.exists():
        outputDir.mkdir(parents=True, exist_ok=True)

    outputFile = outputDir / (inputPath.stem + ".aiff")

    ffmpegInstruction = [
        FFMPEG_PATH,
        "-y",                      # Overwrite without asking
        "-i", str(inputPath),      # Input file
        "-map_metadata", "0",      # Copy metadata from input
        "-acodec", CODEC,          # Use AIFF codec: uncompressed 16-bit PCM
        str(outputFile)            # Output file path
    ]

    try:
        LOGGER.debug(f"Running ffmpeg command: {' '.join(ffmpegInstruction)}")

        runResult = subprocess.run(ffmpegInstruction, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if runResult.returncode != 0:
            LOGGER.error(f"FFmpeg error converting {inputPath.name}: {runResult.stderr}")
            raise RuntimeError(f"FFmpeg failed for {inputPath.name}")
        else:
            LOGGER.info(f"Converted: {inputPath.name} -> {outputFile.name}")
            return outputFile

    except Exception as e:
        LOGGER.error(f"Exception during conversion of {inputPath.name}: {e}")
        raise Exception(f"Error converting {inputPath.name} to AIFF: {e}")
