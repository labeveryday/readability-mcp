"""
Text analysis modules for readability, sentence difficulty, and AI pattern detection
"""

from .readability import ReadabilityAnalyzer
from .sentences import SentenceAnalyzer
from .ai_patterns import AIPatternDetector

__all__ = ['ReadabilityAnalyzer', 'SentenceAnalyzer', 'AIPatternDetector']