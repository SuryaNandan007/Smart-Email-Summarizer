# Smart Email Summarizer — Kaggle Submission Description

**Project:** Smart Email Summarizer Agent  
**Track:** Concierge Agents

## Summary
A multi-agent pipeline that reads raw email text, summarizes content, extracts actionable tasks and deadlines, and saves a structured report (JSON/TXT). Built to save time and reduce missed follow-ups for professionals.

## How to run
1. Install requirements:
```
pip install -r requirements.txt
```
2. Run the agent:
```
python run_agent.py --email data/sample_email.txt
```

## What's included
- agent/ : Reader, Summarizer, Extractor, Report Builder
- data/ : sample email
- tests/ : pytest tests
- LICENSE : MIT License
- thumbnail.png : diagram thumbnail

## Evaluation
Run `pytest` to validate core functionality. The project includes a small evaluation dataset and `evaluation.json` is generated when running the pipeline.

## Notes
- The summarizer uses OpenAI if `OPENAI_API_KEY` is set; otherwise it falls back to a simple extractive summarizer.
- Replace sample data with real emails to evaluate on your own set.
