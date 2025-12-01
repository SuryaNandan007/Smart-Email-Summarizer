import json
from pathlib import Path
from datetime import datetime

class ReportBuilderAgent:
    def __init__(self, output_dir: Path = Path('output')):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    def save_json(self, report: dict) -> str:
        filename = self._timestamped_name('email_summary', 'json')
        path = self.output_dir / filename
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        return str(path)
    def save_text(self, report: dict) -> str:
        filename = self._timestamped_name('email_summary', 'txt')
        path = self.output_dir / filename
        with open(path, 'w', encoding='utf-8') as f:
            f.write('SUMMARY:\n')
            f.write(report.get('summary','') + '\n\n')
            f.write('TASKS:\n')
            for t in report.get('tasks', []):
                f.write('- ' + t + '\n')
            f.write('\nDATES:\n')
            for d in report.get('dates', []):
                f.write('- ' + d + '\n')
        return str(path)
    def _timestamped_name(self, base: str, ext: str) -> str:
        ts = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
        return f"{base}_{ts}.{ext}"
