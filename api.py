from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks
from fastapi.responses import FileResponse
import os
import tempfile

from indextts.infer import IndexTTS

app = FastAPI()
tts = IndexTTS(cfg_path="checkpoints/config.yaml", model_dir="checkpoints")


@app.post("/tts")
async def tts_endpoint(
    background_tasks: BackgroundTasks,
    text: str = Form(...),
    audio_prompt: UploadFile = File(...),
):
    """Synthesize speech from text with a reference audio prompt.

    The request should include a form field ``text`` containing the input
    text and an ``audio_prompt`` file providing the speaker reference audio.
    The synthesized waveform is returned as a WAV file.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_prompt.filename)[1]) as tmp_prompt:
        tmp_prompt.write(await audio_prompt.read())
        prompt_path = tmp_prompt.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_out:
        output_path = tmp_out.name

    tts.infer(prompt_path, text, output_path)

    background_tasks.add_task(os.remove, prompt_path)
    background_tasks.add_task(os.remove, output_path)

    return FileResponse(output_path, media_type="audio/wav", filename="output.wav")


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000)
