from pathlib import Path
import re

class ReaderAgent:
    def read(self, path: Path) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    def clean(self, text: str) -> str:
        s = text.replace('\r\n', '\n')
        s = re.sub(r'\n{2,}', '\n\n', s)
        s = re.sub(r'(^>+\s?.*$\n?)', '', s, flags=re.MULTILINE)
        s = re.split(r'-{2,}Original Message-{2,}', s, flags=re.IGNORECASE)[0]
        return s.strip()
