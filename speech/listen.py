from faster_whisper import WhisperModel
import sounddevice as sd
import soundfile as sf
import tempfile

print("Loading Faster Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def listen():

    sample_rate = 16000
    duration = 5

    print("\nSpeak now...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    sf.write(
        temp_file.name,
        recording,
        sample_rate
    )

    segments, info = model.transcribe(
        temp_file.name
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()