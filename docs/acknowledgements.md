# Acknowledgements

IndexTTS builds upon several innovative projects and research in the field of speech synthesis. We are grateful to the developers and researchers behind these works.

Our project is mainly based on or inspired by:

1.  **[Tortoise-TTS](https://github.com/neonbjb/tortoise-tts)**: A leading open-source text-to-speech system known for its high-quality voice cloning capabilities. We adopted and adapted several architectural concepts from Tortoise.

2.  **[XTTSv2 (Coqui-AI TTS)](https://github.com/coqui-ai/TTS)**: Coqui's XTTS models, particularly version 2, have been a significant reference for our work, especially in terms of multilingual capabilities and model structure.

3.  **[BigVGAN](https://github.com/NVIDIA/BigVGAN)**: We integrated a BigVGAN2-based vocoder to enhance the audio quality and fidelity of the synthesized speech. NVIDIA's work on GAN-based vocoders has been pivotal for achieving realistic speech output.

4.  **[WeNet](https://github.com/wenet-e2e/wenet/tree/main)**: The WeNet toolkit, particularly its work on Conformer models, influenced our design of the conditioning encoder, contributing to improved training stability and timbre similarity.

5.  **[Icefall (K2-FSA)](https://github.com/k2-fsa/icefall)**: Research and codebases from the K2-FSA project, including Icefall, provided valuable insights into speech processing and model architectures.

We also thank the broader open-source community for providing the tools, libraries, and datasets that make projects like IndexTTS possible.

If you believe your work has been an important inspiration and is not listed here, please let us know by opening an issue or discussion on our GitHub repository.
