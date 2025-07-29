import imageio_ffmpeg as ffmpeg
import configparser

FFMPEG_PATH = ffmpeg.get_ffmpeg_exe()

CONFIGURATION = configparser.ConfigParser(interpolation=None)
CONFIGURATION.read("configuration.ini")
