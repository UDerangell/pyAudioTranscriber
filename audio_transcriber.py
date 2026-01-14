#!/usr/bin/env python3
"""
Offline MP4 to Transcript Processor
Extracts audio from MP4 files and generates text transcripts
Requires: ffmpeg, pydub, whisper (all working offline)
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from pydub import AudioSegment
import whisper
import logging

class VideoTranscriber:
    def __init__(self, mp4_dir="mp4_files", mp3_dir="mp3_files", 
                 wav_dir="wav_output", transcript_dir="transcripts", log_dir="logs"):
        """Initialize transcriber with directory paths"""
        self.mp4_dir = Path(mp4_dir)
        self.mp3_dir = Path(mp3_dir)
        self.wav_dir = Path(wav_dir)
        self.transcript_dir = Path(transcript_dir)
        self.log_dir = Path(log_dir)
        
        # Create directories if they don't exist
        for directory in [self.mp4_dir, self.mp3_dir, self.wav_dir, 
                         self.transcript_dir, self.log_dir]:
            directory.mkdir(exist_ok=True)
        
        # Setup logging
        self._setup_logging()
        
        # Load Whisper model (offline)
        self.logger.info("Loading Whisper model...")
        try:
            self.model = whisper.load_model("base")
            self.logger.info("Whisper model loaded successfully")
        except Exception as e:
            self.logger.error(f"Failed to load Whisper model: {e}")
            sys.exit(1)
    
    def _setup_logging(self):
        """Configure logging to file and console"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = self.log_dir / f"transcription_{timestamp}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def extract_audio(self, mp4_path):
        """Extract audio from MP4 and save as WAV"""
        try:
            self.logger.info(f"Extracting audio from: {mp4_path.name}")
            
            # Load video file and extract audio
            audio = AudioSegment.from_file(str(mp4_path), format="mp3")
            
            # Convert to mono, 16kHz (optimal for speech recognition)
            audio = audio.set_channels(1)
            audio = audio.set_frame_rate(16000)
            
            # Generate output filename
            wav_filename = mp4_path.stem + ".wav"
            wav_path = self.wav_dir / wav_filename
            
            # Export as WAV
            audio.export(str(wav_path), format="wav")
            
            self.logger.info(f"Audio extracted to: {wav_filename}")
            return wav_path
            
        except Exception as e:
            self.logger.error(f"Failed to extract audio from {mp4_path.name}: {e}")
            return None
    
    def transcribe_audio(self, wav_path):
        """Transcribe WAV file using Whisper"""
        try:
            self.logger.info(f"Transcribing: {wav_path.name}")
            
            # Transcribe using Whisper
            result = self.model.transcribe(str(wav_path))
            
            # Generate output filename
            txt_filename = wav_path.stem + ".txt"
            txt_path = self.transcript_dir / txt_filename
            
            # Save transcript
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(result["text"])
            
            self.logger.info(f"Transcript saved to: {txt_filename}")
            return txt_path, result["text"]
            
        except Exception as e:
            self.logger.error(f"Failed to transcribe {wav_path.name}: {e}")
            return None, None
    
    def process_single_file(self, mp4_path):
        """Process a single MP4 file: extract audio and transcribe"""
        self.logger.info(f"\n{'='*60}")
        self.logger.info(f"Processing: {mp4_path.name}")
        self.logger.info(f"{'='*60}")
        
        # Step 1: Extract audio
        wav_path = self.extract_audio(mp4_path)
        if wav_path is None:
            return False
        
        # Step 2: Transcribe
        txt_path, transcript = self.transcribe_audio(wav_path)
        if txt_path is None:
            return False
        
        # Print preview of transcript
        preview = transcript[:200] + "..." if len(transcript) > 200 else transcript
        self.logger.info(f"Transcript preview: {preview}")
        
        return True
    
    def process_all_files(self):
        """Process all MP4 files in the input directory"""
        # Find all MP4 files
        mp4_files = list(self.mp3_dir.glob("*.mp3")) + list(self.mp3_dir.glob("*.MP3"))
        
        if not mp4_files:
            self.logger.warning(f"No MP3 files found in {self.input_dir}")
            return
        
        self.logger.info(f"Found {len(mp4_files)} MP3 file(s) to process")
        
        # Process each file
        successful = 0
        failed = 0
        
        for i, mp4_path in enumerate(mp4_files, 1):
            self.logger.info(f"\nFile {i}/{len(mp4_files)}")
            
            if self.process_single_file(mp4_path):
                successful += 1
            else:
                failed += 1
        
        # Summary
        self.logger.info(f"\n{'='*60}")
        self.logger.info(f"PROCESSING COMPLETE")
        self.logger.info(f"{'='*60}")
        self.logger.info(f"Successful: {successful}")
        self.logger.info(f"Failed: {failed}")
        self.logger.info(f"WAV files saved to: {self.wav_dir}")
        self.logger.info(f"Transcripts saved to: {self.transcript_dir}")
        self.logger.info(f"Log saved to: {self.log_dir}")

def main():
    """Main entry point"""
    print("Offline MP4 to Transcript Processor")
    print("=" * 60)
    
    # Initialize transcriber
    transcriber = VideoTranscriber()
    
    # Process all files
    transcriber.process_all_files()

if __name__ == "__main__":
    main()
