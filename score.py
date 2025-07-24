import textstat
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def readability(text):
    score = textstat.flesch_reading_ease(text)
    return round(min(max(score/2, 0), 20), 2)

def grammar(text):
    matches = tool.check(text)
    # for match in matches:
    #     print(f"Grammar issue: {match.ruleId} - {match.message} at position {match.offset}")
    total_words = len(text.split())
    errors = len(matches)
    if total_words == 0:
        return 0
    error_rate = errors / total_words
    score = max(0, 20 - error_rate * 100)
    return round(min(score, 20), 2)

def sections(text):
    sections = ['education', 'experience', 'skills', 'projects', 'certifications']
    found = sum(1 for section in sections if section in text.lower())
    return (found/len(sections))*20

def keywords(text):
    keywords = ['python', 'machine learning', 'sql', 'java', 'data', 'project']
    found = sum(1 for kw in keywords if kw in text.lower())
    return min(found*3, 20)