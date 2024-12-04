# Whisper Transcription Project

This project uses OpenAI's Whisper model to transcribe audio files into text. The transcription result is saved to a text file.

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- ffmpeg (Install using `brew install ffmpeg` on macOS or `sudo apt-get install ffmpeg` on Ubuntu)

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

1. Place your audio file named `voice.mp3` in the project directory.

2. Run the script:
    ```sh
    python index.py
    ```

3. The transcription will be saved to [transcription.txt](http://_vscodecontentref_/3).

## Logging

The script uses Python's `logging` module to log the progress of the transcription process. Logs are printed to the console.

## File Details

### [.gitignore](http://_vscodecontentref_/4)
