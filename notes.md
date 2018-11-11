## Setup

sudo add-apt-repository ppa:jonathonf/ffmpeg-4
sudo apt-get update && sudo apt-get install ffmpeg
ffmpeg -i ./A7R3-001-194.mov -ss 00:00:10 -t 00:00:50 -async 1 -vn -ac 1 audio-194-1.flac
gcloud ml speech recognize --language-code ko-KR ./audio-194-1.aac


## Examples

### Short clip of in-match material, English-speaking

```bash
ffmpeg -i ./A7R3-001-186.mov -ss 00:04:15 -t 00:00:50 -async 1 -vn -ac 1 audio-186-1-en-short.flac
gcloud ml speech recognize --language-code en-US  --include-word-time-offsets --max-alternatives=0 ./audio-186-1-en-short.flac
{
  "results": [
    {
      "alternatives": [
        {
          "confidence": 0.82896113,
          "transcript": "hey let's go inside.",
          "words": [
            {
              "endTime": "6.400s",
              "startTime": "5.900s",
              "word": "hey"
            },
            {
              "endTime": "7.800s",
              "startTime": "6.400s",
              "word": "let's"
            },
            {
              "endTime": "7.800s",
              "startTime": "7.800s",
              "word": "go"
            },
            {
              "endTime": "9.100s",
              "startTime": "7.800s",
              "word": "inside."
            }
          ]
        }
      ]
    },
    {
      "alternatives": [
        {
          "confidence": 0.53151643,
          "transcript": " Sew-in side part closure",
          "words": [
            {
              "endTime": "25.400s",
              "startTime": "24.800s",
              "word": "Sew-in"
            },
            {
              "endTime": "25.600s",
              "startTime": "25.400s",
              "word": "side"
            },
            {
              "endTime": "25.700s",
              "startTime": "25.600s",
              "word": "part"
            },
            {
              "endTime": "26.100s",
              "startTime": "25.700s",
              "word": "closure"
            }
          ]
        }
      ]
    }
  ]
}
```

### Long clip of conversational material, Korean-speaking

```
gcloud ml speech recognize-long-running --language-code ko-KR  --include-word-time-offsets --max-alternatives=0 gs://"transcriber-material/audio-194-2-mono-long-running.flac" --async
gcloud ml speech operations wait <operation id> > audio-194-2-mono-long-running.json
python generate_srt.py audio-194-2-mono-long-running.json
```
