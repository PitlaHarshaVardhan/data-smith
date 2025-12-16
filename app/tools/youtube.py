from youtube_transcript_api import YouTubeTranscriptApi
import re

def fetch(text):
    video_id = re.findall(r"(?:v=|\/)([0-9A-Za-z_-]{11})", text)
    if not video_id:
        return "Could not detect YouTube video ID."
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id[0])
        return " ".join([t["text"] for t in transcript])
    except:
        return "Transcript not available."
