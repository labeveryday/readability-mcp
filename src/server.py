#!/usr/bin/env python3
"""
Readability MCP Server
Main server module that exposes MCP tools for text analysis
"""

import logging
from typing import Dict, Any, Optional, List
from fastmcp import FastMCP

from src.analyzers import ReadabilityAnalyzer, SentenceAnalyzer, AIPatternDetector

# Initialize FastMCP server
mcp = FastMCP("readability-analyzer")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize analyzers
readability_analyzer = ReadabilityAnalyzer()
sentence_analyzer = SentenceAnalyzer()
ai_detector = AIPatternDetector()


@mcp.tool()
async def analyze_text(text: str, metrics: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Analyze text readability using multiple metrics
    
    Args:
        text: The text to analyze
        metrics: Optional list of specific metrics to calculate. 
                Options: flesch_kincaid, flesch_ease, smog, ari, coleman_liau, 
                        linsear, gunning_fog, dale_chall
    
    Returns:
        Dictionary containing:
        - flesch_kincaid_grade: Grade level (0-18+)
        - flesch_reading_ease: Ease score (0-100, higher is easier)
        - interpretation: Human-readable interpretation
        - Additional metrics based on request
        - Text statistics (word count, sentences, etc.)
    
    Example:
        {
            "flesch_kincaid_grade": 8.2,
            "flesch_reading_ease": 65.3,
            "interpretation": "Standard - 8th & 9th grade level",
            "statistics": {...}
        }
    """
    if not text or len(text.strip()) == 0:
        return {"error": "Text cannot be empty"}
    
    try:
        result = readability_analyzer.analyze(text, metrics)
        logger.info(f"Analyzed text with {result['statistics']['word_count']} words")
        return result
    except Exception as e:
        logger.error(f"Error analyzing text: {str(e)}")
        return {"error": f"Analysis failed: {str(e)}"}


@mcp.tool()
async def find_hard_sentences(
    text: str, 
    count: int = 5, 
    threshold: float = 10.0
) -> Dict[str, Any]:
    """
    Find the most difficult sentences in the text
    
    Args:
        text: The text to analyze
        count: Number of difficult sentences to return (default: 5)
        threshold: Minimum grade level to be considered difficult (default: 10.0)
    
    Returns:
        Dictionary containing:
        - difficult_sentences: List of sentences with analysis
        - total_sentences: Total number of sentences analyzed
        - average_grade_level: Average grade level of all sentences
    
    Each sentence includes:
        - sentence: The actual text
        - grade_level: Readability grade level
        - position: Sentence number in original text
        - issues: Specific problems identified
        - word_count: Number of words
    
    Example:
        {
            "difficult_sentences": [
                {
                    "sentence": "The complex...",
                    "grade_level": 16.3,
                    "position": 3,
                    "issues": ["Very long sentence (35 words)", "Multiple clauses"],
                    "word_count": 35
                }
            ],
            "total_sentences": 10,
            "average_grade_level": 9.5
        }
    """
    if not text or len(text.strip()) == 0:
        return {"error": "Text cannot be empty"}
    
    try:
        difficult_sentences = sentence_analyzer.find_difficult_sentences(text, count, threshold)
        
        # Calculate average grade level for context
        import nltk
        import textstat
        sentences = nltk.sent_tokenize(text)
        total_grade = sum(textstat.flesch_kincaid_grade(s) for s in sentences if len(s.strip()) > 10)
        avg_grade = total_grade / len(sentences) if sentences else 0
        
        result = {
            "difficult_sentences": difficult_sentences,
            "total_sentences": len(sentences),
            "average_grade_level": round(avg_grade, 1),
            "threshold_used": threshold
        }
        
        logger.info(f"Found {len(difficult_sentences)} difficult sentences out of {len(sentences)}")
        return result
        
    except Exception as e:
        logger.error(f"Error finding difficult sentences: {str(e)}")
        return {"error": f"Analysis failed: {str(e)}"}


@mcp.tool()
async def check_ai_phrases(
    text: str,
    sensitivity: str = "medium"
) -> Dict[str, Any]:
    """
    Check text for common AI-generated writing patterns
    
    Args:
        text: The text to analyze
        sensitivity: Detection sensitivity - "low", "medium", or "high" (default: "medium")
                    Higher sensitivity catches more patterns but may have false positives
    
    Returns:
        Dictionary containing:
        - ai_likelihood_score: Score from 0-100 (higher = more AI-like)
        - interpretation: Human-readable interpretation
        - patterns_detected: Detailed list of patterns found
        - recommendations: Specific suggestions for more natural writing
    
    Pattern Categories:
        - dead_giveaways: Phrases almost exclusively used by AI
        - high_probability: Strong indicators of AI writing
        - moderate_indicators: Common in AI but also in formal writing
        - structural_patterns: Formatting patterns typical of AI
    
    Example:
        {
            "ai_likelihood_score": 45.2,
            "interpretation": "Medium - Noticeable AI patterns present",
            "patterns_detected": [...],
            "recommendations": ["Replace 'delve into' with 'explore'", ...]
        }
    """
    if not text or len(text.strip()) == 0:
        return {"error": "Text cannot be empty"}
    
    if sensitivity not in ["low", "medium", "high"]:
        return {"error": "Sensitivity must be 'low', 'medium', or 'high'"}
    
    try:
        result = ai_detector.analyze(text, sensitivity)
        
        logger.info(
            f"AI detection complete: score={result['ai_likelihood_score']}, "
            f"patterns={result['pattern_summary']['total_patterns']}"
        )
        
        return result
        
    except Exception as e:
        logger.error(f"Error checking AI patterns: {str(e)}")
        return {"error": f"Analysis failed: {str(e)}"}


@mcp.tool()
async def health_check() -> Dict[str, str]:
    """
    Check if the server is running and all dependencies are loaded
    
    Returns:
        Dictionary with server status and version information
    """
    import textstat
    
    return {
        "status": "healthy",
        "version": "1.0.0",
        "textstat_version": textstat.__version__,
        "tools_available": [
            "analyze_text",
            "find_hard_sentences", 
            "check_ai_phrases",
            "health_check"
        ]
    }


# Run the server
if __name__ == "__main__":
    mcp.run()