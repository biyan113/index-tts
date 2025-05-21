# Getting Started

This guide will walk you through the process of setting up IndexTTS on your local machine.

## Prerequisites

- Python 3.10 or higher
- Conda (recommended)
- Git

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/index-tts/index-tts.git
    cd index-tts
    ```

2.  **Create and activate a Conda environment:**

    ```bash
    conda create -n index-tts python=3.10
    conda activate index-tts
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install FFmpeg:**

    FFmpeg is required for audio processing.
    -   On Debian/Ubuntu: `sudo apt-get update && sudo apt-get install ffmpeg`
    -   On MacOS: `brew install ffmpeg`
    -   On Windows: Download the FFmpeg binaries and add them to your system's PATH.

5.  **Download Models:**

    The models are required for running IndexTTS. You can download them from HuggingFace or ModelScope.

    Create a `checkpoints` directory if it doesn't exist:
    ```bash
    mkdir -p checkpoints
    ```

    Download the following files into the `checkpoints` directory:
    -   `bigvgan_discriminator.pth`
    -   `bigvgan_generator.pth`
    -   `bpe.model`
    -   `config.yaml` (This should already be in the `checkpoints` directory in the repository)
    -   `dvae.pth`
    -   `gpt.pth`
    -   `unigram_12000.vocab`

    You can use `wget` to download them. For example:
    ```bash
    wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bigvgan_discriminator.pth -P checkpoints
    wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bigvgan_generator.pth -P checkpoints
    wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/bpe.model -P checkpoints
    # Ensure config.yaml is present in checkpoints/
    # wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/config.yaml -P checkpoints
    wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/dvae.pth -P checkpoints
    wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/gpt.pth -P checkpoints
    wget https://huggingface.co/IndexTeam/Index-TTS/resolve/main/unigram_12000.vocab -P checkpoints
    ```
    *Note: The `config.yaml` is usually included in the repository's `checkpoints` directory. If not, download it as well.*


## Quick Test

To ensure everything is set up correctly, you can run a quick test.

1.  **Prepare a prompt audio:**
    Place a `.wav` audio file of a voice you want to clone in a directory, for example, `test_data/input.wav`.

2.  **Run the inference script:**

    ```bash
    PYTHONPATH=. python indextts/infer.py
    ```
    This script will use the `test_data/input.wav` (you'll need to modify the script or place your audio accordingly if it expects a specific path by default) and a predefined text to generate an output audio file. Check the `indextts/infer.py` script for default input/output paths and text.

## Basic Usage (Python)

Here's a simple example of how to use IndexTTS in your Python code:

```python
from indextts.infer import IndexTTS

# Initialize the TTS model
# Ensure the model_dir points to your 'checkpoints' directory
# and cfg_path points to the 'config.yaml' within that directory.
tts = IndexTTS(model_dir="checkpoints", cfg_path="checkpoints/config.yaml")

# Path to the reference voice audio file (e.g., a .wav file)
reference_voice_path = "path/to/your/reference_voice.wav" 

# Text to synthesize
text_to_synthesize = "大家好，我现在正在体验 IndexTTS。AI技术已经发展到这样匪夷所思的地步了！"

# Output path for the generated audio
output_audio_path = "generated_speech.wav"

# Perform inference
tts.infer(reference_voice_path, text_to_synthesize, output_audio_path)

print(f"Generated speech saved to {output_audio_path}")
```

Make sure to replace `"path/to/your/reference_voice.wav"` with the actual path to your reference audio file.

You are now ready to explore more features of IndexTTS!
