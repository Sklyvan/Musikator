# 🎵 Musikator

Welcome to **Musikator**! A Python tool to **search, filter, convert, and organize your audio files** with ease. It leverages `ffmpeg` and `mutagen` to process your music library, supporting formats like MP3, WAV, M4A, AIFF, and FLAC.

---

## 🚀 Features

- 🔍 **Search** for audio files in a directory (recursively or not)
- 🧹 **Filter** files by sample rate (optional)
- 🔄 **Convert** audio files to AIFF format using ffmpeg
- 🏷️ **Copy metadata** from original files to converted ones
- 📁 **Organize** output files into timestamped folders
- 📝 **Log** all actions to a file and the console

---

## 🛠️ How to Use

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Configure your settings**  
   Edit `app/configuration.ini` to match your preferences (see below for details).

3. **Run Musikator**  
   ```
   python app/main.py
   ```
   By default, it processes the folder set in `main.py` (`INPUT_FOLDER`).  
   You can modify this path as needed.

---

## ⚙️ Configuration (`configuration.ini`)

Customize Musikator’s behavior via the INI file:

### LOGGING 📝

| Key         | Description                                      | Example Value                |
|-------------|--------------------------------------------------|------------------------------|
| ENABLED     | Enable/disable logging                           | True                         |
| FILE_NAME   | Log file name                                    | LogFile.log                  |
| LEVEL       | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)| DEBUG                        |
| FORMAT      | Log message format                               | "%(asctime)s - %(name)s ..." |

### SEARCH 🔍

| Key                | Description                                 | Example Value                |
|--------------------|---------------------------------------------|------------------------------|
| RECURSIVE          | Search subfolders too?                      | True                         |
| ACCEPTED_EXTENSIONS| List of file extensions to process          | ["MP3", "WAV", "M4A", ...]   |

### FILTERING 🧹

| Key           | Description                                      | Example Value                |
|---------------|--------------------------------------------------|------------------------------|
| ENABLED       | Enable sample rate filtering                     | False                        |
| MP3_THRESHOLD | Min sample rate for MP3 files (Hz)               | 20000                        |
| WAV_THRESHOLD | Min sample rate for WAV files (Hz)               | 22000                        |
| M4A_THRESHOLD | Min sample rate for M4A files (Hz)               | 22000                        |
| AIFF_THRESHOLD| Min sample rate for AIFF files (Hz)              | 22000                        |
| FLAC_THRESHOLD| Min sample rate for FLAC files (Hz)              | 22000                        |

### OUTPUT 📁

| Key                | Description                                 | Example Value                |
|--------------------|---------------------------------------------|------------------------------|
| NEW_FOLDER_TIMESTAMP| Timestamp format for output folders         | %H_%M_%S_%d_%m_%Y            |
| HASH_VERIFICATION  | Hash algorithm for file verification        | SHA256                       |
| UNPACK_FILES       | Place all output files in a single folder?  | True                         |

## 📦 Example Workflow

1. Musikator scans your folder for audio files.
2. (Optional) Filters out files below the sample rate threshold.
3. Converts eligible files to AIFF, copying metadata.
4. Organizes results into a timestamped folder.
5. Logs all actions for review.

---

## 💡 Tips

- Adjust `UNPACK_FILES` to control output folder structure.
- Set `FILTERING.ENABLED` to `True` to only process high-quality files.
- Check the log file for details on any errors or skipped files.

---

## 🧑‍💻 Requirements

- Python 3.8+
- ffMPEG
- Mutagen
