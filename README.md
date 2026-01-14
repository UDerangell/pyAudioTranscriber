# pyAudioTranscriber

- Transcribes MP3 files to text using Python Whisper model.
- Worked on Python 3.12.1
- TODO: Refactor generated code, test newer versions of Whisper and dependencies

* Subdirectories:
- mp3_files = where you store the MP3 files to be transcribed.  (Use a program like SmartConverter to convert files from other formats)
- wav_output = WAV versions of each MP3 file
- logs = log files for each MP3 file being converted
- transcripts = output TXT files containing transcript for each MP3 file
- transcript_env = virtual environment.  Use PIP to install Whisper and its dependencies.

Sample Output:
```
ericrangell@Erics-MacBook-Air-2 pytrans % ./doaud.sh       
Offline MP4 to Transcript Processor
============================================================
2026-01-14 15:46:24,407 - INFO - Loading Whisper model...
2026-01-14 15:46:25,020 - INFO - Whisper model loaded successfully
2026-01-14 15:46:25,020 - INFO - Found 2 MP3 file(s) to process
2026-01-14 15:46:25,020 - INFO - 
File 1/2
2026-01-14 15:46:25,020 - INFO - 
============================================================
2026-01-14 15:46:25,020 - INFO - Processing: Sovereignty_Non-Interventionism_Versus_Alliance_Friction-mp3.mp3
2026-01-14 15:46:25,020 - INFO - ============================================================
2026-01-14 15:46:25,020 - INFO - Extracting audio from: Sovereignty_Non-Interventionism_Versus_Alliance_Friction-mp3.mp3
2026-01-14 15:46:27,129 - INFO - Audio extracted to: Sovereignty_Non-Interventionism_Versus_Alliance_Friction-mp3.wav
2026-01-14 15:46:27,130 - INFO - Transcribing: Sovereignty_Non-Interventionism_Versus_Alliance_Friction-mp3.wav
/Users/ericrangell/Downloads/git/pytrans/transcript_env/lib/python3.12/site-packages/whisper/transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
2026-01-14 15:47:20,333 - INFO - Transcript saved to: Sovereignty_Non-Interventionism_Versus_Alliance_Friction-mp3.txt
2026-01-14 15:47:20,334 - INFO - Transcript preview:  Welcome to the debate. Our focus today is the November 2025 national security strategy or NSS. It's a document that really signals a dramatic and very intentional pivot in American foreign policy. We...
2026-01-14 15:47:20,334 - INFO - 
File 2/2
2026-01-14 15:47:20,334 - INFO - 
============================================================
2026-01-14 15:47:20,334 - INFO - Processing: The_2025_Strategy_Rejects_Globalism-mp3.mp3
2026-01-14 15:47:20,334 - INFO - ============================================================
2026-01-14 15:47:20,334 - INFO - Extracting audio from: The_2025_Strategy_Rejects_Globalism-mp3.mp3
2026-01-14 15:47:23,551 - INFO - Audio extracted to: The_2025_Strategy_Rejects_Globalism-mp3.wav
2026-01-14 15:47:23,552 - INFO - Transcribing: The_2025_Strategy_Rejects_Globalism-mp3.wav
/Users/ericrangell/Downloads/git/pytrans/transcript_env/lib/python3.12/site-packages/whisper/transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
2026-01-14 15:49:01,900 - INFO - Transcript saved to: The_2025_Strategy_Rejects_Globalism-mp3.txt
2026-01-14 15:49:01,900 - INFO - Transcript preview:  Okay, let's dive in. We have a massive stack of source material in front of us today. And it all centers on one document that really is set to define America's past for the next four years. That's ri...
2026-01-14 15:49:01,900 - INFO - 
============================================================
2026-01-14 15:49:01,900 - INFO - PROCESSING COMPLETE
2026-01-14 15:49:01,900 - INFO - ============================================================
2026-01-14 15:49:01,900 - INFO - Successful: 2
2026-01-14 15:49:01,900 - INFO - Failed: 0
2026-01-14 15:49:01,900 - INFO - WAV files saved to: wav_output
2026-01-14 15:49:01,900 - INFO - Transcripts saved to: transcripts
2026-01-14 15:49:01,900 - INFO - Log saved to: logs
```
