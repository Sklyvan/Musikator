from .configuration import FFMPEG_PATH
import subprocess
import re
import os

def checkFileSampleRate(filePath: str, minimumRate: int) -> bool:
    """
    Checks if the sample rate of an audio file is above a specified minimum rate.
    :param filePath: Path to the audio file.
    :param minimumRate: Minimum sample rate to check against.
    :return: True if the sample rate is above the minimum, False otherwise.
    """
    if not os.path.exists(filePath):
        raise FileNotFoundError(f"File not found: {filePath}")

    try:
        result = subprocess.run(
            [FFMPEG_PATH, "-i", filePath],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )

        # Look for something like "44100 Hz"
        match = re.search(r'(\d+)\s*Hz', result.stderr)
        if not match:
            raise RuntimeError("Could not extract sample rate from ffmpeg output.")

        sample_rate = int(match.group(1))
        print(sample_rate)
        return sample_rate >= minimumRate

    except Exception as e:
        raise RuntimeError(f"Failed to check sample rate using ffmpeg: {e}")
