import imageio_ffmpeg as ffmpeg
import configparser
import os

FFMPEG_PATH = ffmpeg.get_ffmpeg_exe()

CONFIGURATION_FILE_NAME = "configuration.ini"
CONFIGURATION_FILE_PATH = os.path.join(os.path.dirname(__file__), CONFIGURATION_FILE_NAME)

CONFIGURATION = configparser.ConfigParser(interpolation=None)
CONFIGURATION.read(CONFIGURATION_FILE_PATH)
