"""
Data models for analysis results
"""

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ReadabilityResult:
    """Structure for readability analysis results"""
    flesch_kincaid_grade: float
    flesch_reading_ease: float
    interpretation: str
    word_count: int
    sentence_count: int
    syllable_count: int
    avg_words_per_sentence: float


@dataclass
class DifficultSentence:
    """Structure for difficult sentence analysis"""
    text: str
    grade_level: float
    position: int
    issues: List[str]
    word_count: int
    syllable_count: int


@dataclass
class AIDetectionResult:
    """Structure for AI pattern detection results"""
    ai_score: float
    confidence: str
    patterns_found: List[Dict[str, Any]]
    recommendations: List[str]