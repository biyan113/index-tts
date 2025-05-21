# Usage Guide

This guide provides detailed information on how to use IndexTTS, including the Web UI and advanced features.

## Web UI

IndexTTS comes with a user-friendly web interface built with Gradio.

1.  **Start the Web UI:**

    ```bash
    python webui.py
    ```

2.  **Access the Web UI:**
    Open your web browser and navigate to `http://127.0.0.1:7860` (or the URL shown in your terminal).

### Web UI Features:

-   **Text Input:** Enter the text you want to synthesize.
-   **Reference Audio Upload:** Upload a `.wav` or `.mp3` file of the voice you want to clone.
-   **Pinyin Input (for Chinese):** Optionally provide pinyin for Chinese characters to ensure correct pronunciation.
-   **Pause Control:** Use punctuation marks (e.g., commas, periods) in your text to control pauses in the synthesized speech. More punctuation generally leads to longer pauses.
-   **Language Selection:** Choose the language of the input text.
-   **Output Audio:** Download the generated speech as a `.wav` file.

Experiment with different reference audios and text inputs to explore the capabilities of IndexTTS.

## Command-Line Interface (CLI)

The primary way to use IndexTTS via the command line is through the `indextts/infer.py` script.

### Basic CLI Usage:

```bash
PYTHONPATH=. python indextts/infer.py \
    --voice_path path/to/your/reference_voice.wav \
    --text "Hello, this is a test of IndexTTS." \
    --output_path generated_speech.wav \
    --language "en" 
    # Add other parameters as needed
```

### CLI Parameters in `indextts/infer.py`:

The `indextts/infer.py` script can be customized with various arguments. You might need to modify the script to accept these arguments from the command line or change default values. Here are common parameters you might interact with (based on typical TTS systems and the provided `sample_code`):

-   `model_dir`: Path to the directory containing the model checkpoints (e.g., `"checkpoints"`).
-   `cfg_path`: Path to the configuration file (e.g., `"checkpoints/config.yaml"`).
-   `voice_path` (or similar): Path to the reference audio file for voice cloning.
-   `text`: The text to be synthesized.
-   `output_path`: File path to save the generated audio.
-   `language`: Language of the text (e.g., "en", "zh").
-   **Pinyin Control (for Chinese):**
    IndexTTS allows fine-grained pronunciation control for Chinese text using pinyin. While direct CLI arguments for this might vary, the underlying `tts.infer()` method might accept pinyin-annotated text or separate pinyin inputs.
    Example of pinyin-annotated text: `"你好[ni3 hao3]，世界[shi4 jie4]。"`
    Refer to the `IndexTTS` class implementation or examples for specific pinyin input formats.

-   **Pause Control:**
    Pauses are primarily controlled by punctuation in the input text.
    -   Commas (`,`) typically insert shorter pauses.
    -   Periods (`.`), question marks (`?`), exclamation marks (`!`) typically insert longer pauses.
    -   You can experiment with multiple punctuation marks for longer pauses (e.g., `"Hello... world"`).

### Modifying `indextts/infer.py` for Flexibility:

The default `indextts/infer.py` script in the repository might have hardcoded values for text, reference audio, and output paths. To make it more flexible for CLI use:

1.  **Open `indextts/infer.py`**.
2.  **Import `argparse`:**
    ```python
    import argparse
    ```
3.  **Set up an argument parser at the beginning of the script:**
    ```python
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="IndexTTS Command-Line Inference")
        parser.add_argument("--model_dir", type=str, default="checkpoints", help="Directory containing model checkpoints.")
        parser.add_argument("--cfg_path", type=str, default="checkpoints/config.yaml", help="Path to the configuration file.")
        parser.add_argument("--voice_path", type=str, required=True, help="Path to the reference voice audio file.")
        parser.add_argument("--text", type=str, required=True, help="Text to synthesize.")
        parser.add_argument("--output_path", type=str, default="generated_speech.wav", help="Path to save the output audio file.")
        parser.add_argument("--language", type=str, default="en", help="Language of the text (e.g., 'en', 'zh').")
        # Add other arguments as needed

        args = parser.parse_args()

        tts = IndexTTS(model_dir=args.model_dir, cfg_path=args.cfg_path)
        tts.infer(args.voice_path, args.text, args.output_path, language=args.language) # Ensure your infer method accepts language
        print(f"Generated speech saved to {args.output_path}")
    ```
    *Note: You'll need to ensure the `tts.infer` method in `indextts/infer.py` is updated to accept a `language` parameter if it doesn't already, or handle language selection appropriately within the method.*

## Advanced Usage

### Controlling Pronunciation (Chinese)

For Chinese text, you can improve pronunciation accuracy by providing pinyin.
-   **Web UI:** Use the dedicated pinyin input field if available, or intersperse pinyin in the main text field using a format like `汉字[han4 zi4]`.
-   **Python/CLI:** Prepare your text string with pinyin annotations. The exact format (e.g., `你好[ni3 hao3]`) depends on how the `IndexTTS.infer` method or the underlying text processing pipeline handles it. Refer to specific examples or the source code for the accepted format.

### Controlling Pauses

-   Use standard punctuation marks in your input text:
    -   `,`: short pause
    -   `.`, `?`, `!`: medium/longer pause
    -   `...` (ellipsis): longer pause
    -   Multiple punctuations (e.g. `!!`, `??`): can sometimes extend pauses, depending on the model's training.
-   Experiment with these to achieve the desired rhythm and pacing in the generated speech.

This guide should help you make the most of IndexTTS. For more specific questions, consider looking at the example code, the `indextts` module implementations, or asking the community.
