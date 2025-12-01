import os
class SummarizerAgent:
    def __init__(self):
        self.api_key = os.environ.get('OPENAI_API_KEY')
        self._client = None
        if self.api_key:
            try:
                import openai
                openai.api_key = self.api_key
                self._client = openai
            except Exception:
                self._client = None
    def summarize(self, text: str, max_words: int = 100) -> str:
        if self._client:
            try:
                prompt = ("Summarize the following email in a concise paragraph (max {} words).\n\n".format(max_words)) + text
                completion = self._client.Completion.create(model='text-davinci-003', prompt=prompt, max_tokens=200, temperature=0.1)
                out = completion.choices[0].text.strip()
                return ' '.join(out.split())
            except Exception:
                pass
        sentences = self._split_sentences(text)
        if not sentences:
            return ''
        selected = []
        words = 0
        for s in sentences:
            w = len(s.split())
            if words + w > max_words and selected:
                break
            selected.append(s)
            words += w
            if len(selected) >= 3:
                break
        return ' '.join(selected)
    def _split_sentences(self, text: str):
        import re
        pieces = re.split(r'(?<=[.!?])\s+', text.strip())
        return [p.strip() for p in pieces if p.strip()]
