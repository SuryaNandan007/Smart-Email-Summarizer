import re
from typing import List, Tuple

class ExtractorAgent:
    ACTION_VERBS = ['call','email','send','review','approve','schedule','submit','deliver','prepare','meet','confirm']
    DATE_PATTERNS = [r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{1,2}\b',
                     r'\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b',
                     r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',
                     r'\bbefore\s+\w+\b']
    def extract_tasks(self, text: str) -> Tuple[List[str], List[str]]:
        sentences = self._split_sentences(text)
        tasks = []
        for s in sentences:
            lower = s.lower()
            if any(v in lower for v in self.ACTION_VERBS) or 'please' in lower:
                tasks.append(s.strip())
        dates = self._find_dates(text)
        return tasks, dates
    def _split_sentences(self, text: str):
        import re
        pieces = re.split(r'(?<=[.!?])\s+', text.strip())
        return [p.strip() for p in pieces if p.strip()]
    def _find_dates(self, text: str):
        found = set()
        for pat in self.DATE_PATTERNS:
            for m in re.findall(pat, text, flags=re.IGNORECASE):
                found.add(m)
        return sorted(found)
