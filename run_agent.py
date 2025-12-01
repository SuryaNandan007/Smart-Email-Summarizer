#!/usr/bin/env python3
"""Run the Smart Email Summarizer Agent pipeline.

Usage:
    python run_agent.py --email data/sample_email.txt
"""
from pathlib import Path
from agent.reader import ReaderAgent
from agent.summarizer import SummarizerAgent
from agent.extractor import ExtractorAgent
from agent.report_builder import ReportBuilderAgent
import argparse

def run_pipeline(email_path):
    reader = ReaderAgent()
    summarizer = SummarizerAgent()
    extractor = ExtractorAgent()
    builder = ReportBuilderAgent()
    raw = reader.read(email_path)
    cleaned = reader.clean(raw)
    summary = summarizer.summarize(cleaned)
    tasks, dates = extractor.extract_tasks(cleaned)
    report = {'summary': summary, 'tasks': tasks, 'dates': dates, 'source_file': str(email_path)}
    j = builder.save_json(report)
    t = builder.save_text(report)
    print('Done. Outputs:')
    print(' JSON:', j)
    print(' TXT :', t)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', '-e', required=False, default='data/sample_email.txt', help='Path to the email text file')
    args = parser.parse_args()
    p = Path(args.email)
    if not p.exists():
        print('Email file not found:', p)
        raise SystemExit(1)
    run_pipeline(p)
