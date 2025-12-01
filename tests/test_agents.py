from pathlib import Path
from agent.reader import ReaderAgent
from agent.summarizer import SummarizerAgent
from agent.extractor import ExtractorAgent
from agent.report_builder import ReportBuilderAgent

def test_reader_and_clean(tmp_path):
    p = tmp_path / 'sample.txt'
    p.write_text('Hello\n\n> Quoted\n-----Original Message-----\nold')
    r = ReaderAgent()
    raw = r.read(p)
    cleaned = r.clean(raw)
    assert 'Original Message' not in cleaned

def test_summarizer_fallback():
    text = 'This is sentence one. This is sentence two. This is sentence three. This is sentence four.'
    s = SummarizerAgent()
    summary = s.summarize(text, max_words=20)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_extractor():
    text = 'Please send the report by Friday. Also schedule a call on Monday.'
    e = ExtractorAgent()
    tasks, dates = e.extract_tasks(text)
    assert any('send' in t.lower() or 'schedule' in t.lower() for t in tasks)
    assert any('Friday' in d or 'Monday' in d for d in dates)

def test_report_builder(tmp_path):
    rb = ReportBuilderAgent(output_dir=tmp_path)
    report = {'summary':'ok','tasks':['do it'],'dates':['Friday']}
    j = rb.save_json(report)
    t = rb.save_text(report)
    assert Path(j).exists()
    assert Path(t).exists()
