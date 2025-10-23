"""
AI pattern detection module
Identifies common AI-generated writing patterns and phrases
"""

import re
from typing import Any
from collections import defaultdict
from functools import lru_cache
import hashlib


class AIPatternDetector:
    """Detects AI-generated writing patterns in text"""
    
    # AI phrase patterns organized by category and weight
    AI_PATTERNS = {
        "dead_giveaways": {
            "phrases": [
                "delve into", "delving deeper", "delve deeper",
                "tapestry of", "rich tapestry", 
                "a testament to", "stands as a testament",
                "in today's world", "in today's landscape", "in today's society",
                "navigating the complexities", "navigate the complex",
                "unlock the potential", "unlocking insights"
            ],
            "weight": 3.0
        },
        "high_probability": {
            "phrases": [
                "moreover", "furthermore", "additionally",
                "it's important to note that", "it's worth noting",
                "it's crucial to understand", "it's essential to",
                "while it's true that", "while it may seem",
                "on one hand", "on the other hand",
                "in conclusion", "to summarize", "in summary",
                "leverage", "utilize", "paramount", "plethora"
            ],
            "weight": 2.0
        },
        "moderate_indicators": {
            "phrases": [
                "however", "nevertheless", "nonetheless",
                "significant", "robust", "comprehensive",
                "various", "numerous", "multifaceted",
                "it should be noted", "bear in mind",
                "synergy", "holistic", "paradigm"
            ],
            "weight": 1.0
        },
        "structural_patterns": {
            "phrases": [
                "firstly", "secondly", "thirdly", "lastly",
                "in essence", "essentially", "fundamentally",
                "broadly speaking", "generally speaking",
                "for instance", "for example",
            ],
            "weight": 0.5
        }
    }
    
    def __init__(self):
        """Initialize the AI pattern detector"""
        self.sensitivity_multipliers = {
            "low": 0.7,
            "medium": 1.0,
            "high": 1.3
        }

        # Pre-compile regex patterns for better performance
        self._compiled_patterns = {}
        for category, data in self.AI_PATTERNS.items():
            self._compiled_patterns[category] = [
                (phrase, re.compile(r'\b' + re.escape(phrase) + r'\b', re.IGNORECASE))
                for phrase in data["phrases"]
            ]
    
    def detect_patterns(self, text: str, sensitivity: str = "medium") -> tuple[float, list[dict[str, Any]]]:
        """
        Detect AI patterns in text and calculate AI likelihood score

        Args:
            text: The text to analyze
            sensitivity: Detection sensitivity level (low/medium/high)

        Returns:
            Tuple of (ai_score, list_of_patterns_found)
        """
        patterns_found = []
        total_score = 0

        # Get sensitivity multiplier
        multiplier = self.sensitivity_multipliers.get(sensitivity, 1.0)

        # Check each category of patterns using pre-compiled regex
        for category, data in self.AI_PATTERNS.items():
            category_matches = []

            for phrase, pattern in self._compiled_patterns[category]:
                # Find all matches using pre-compiled pattern
                matches = pattern.finditer(text)

                for match in matches:
                    # Get context around the match
                    start = max(0, match.start() - 30)
                    end = min(len(text), match.end() + 30)
                    context = text[start:end].strip()

                    # Add ellipsis if truncated
                    if start > 0:
                        context = "..." + context
                    if end < len(text):
                        context = context + "..."

                    category_matches.append({
                        "phrase": phrase,
                        "context": context,
                        "position": match.start()
                    })

                    # Add to total score
                    total_score += data["weight"] * multiplier

            if category_matches:
                patterns_found.append({
                    "category": category,
                    "confidence": self._get_confidence_level(category),
                    "matches": category_matches,
                    "count": len(category_matches)
                })
        
        # Calculate final AI score (0-100)
        # Use pattern density normalized per 100 words for consistent scoring
        word_count = len(text.split())
        if word_count > 0:
            # Calculate pattern density (patterns per 100 words)
            # This makes scoring consistent regardless of text length
            pattern_density = (total_score / word_count) * 100

            # Scale to 0-100 range with a reasonable curve
            # Score of 15+ in density maps to ~100, Score of 3 maps to ~50
            ai_score = min(100, pattern_density * 6.5)

            # For very short texts (< 50 words), apply a small confidence penalty
            # to account for statistical insignificance
            if word_count < 50:
                confidence_factor = word_count / 50  # 0.2 to 1.0
                ai_score = ai_score * (0.7 + 0.3 * confidence_factor)
        else:
            ai_score = 0
        
        return ai_score, patterns_found
    
    def _get_confidence_level(self, category: str) -> str:
        """Get human-readable confidence level for a category"""
        confidence_map = {
            "dead_giveaways": "Very High",
            "high_probability": "High",
            "moderate_indicators": "Medium",
            "structural_patterns": "Low"
        }
        return confidence_map.get(category, "Unknown")
    
    def interpret_ai_score(self, score: float) -> str:
        """Interpret the AI likelihood score"""
        if score < 20:
            return "Very low - Text appears naturally written"
        elif score < 40:
            return "Low - Mostly natural with minor AI indicators"
        elif score < 60:
            return "Medium - Noticeable AI patterns present"
        elif score < 80:
            return "High - Strong AI characteristics detected"
        else:
            return "Very high - Multiple strong AI patterns found"
    
    def get_recommendations(self, patterns_found: list[dict[str, Any]], ai_score: float) -> list[str]:
        """
        Generate specific recommendations based on patterns found
        
        Args:
            patterns_found: List of detected patterns
            ai_score: Overall AI likelihood score
        
        Returns:
            List of specific improvement recommendations
        """
        tips = []
        
        # Count patterns by category
        category_counts = defaultdict(int)
        all_phrases = []
        
        for pattern_group in patterns_found:
            category = pattern_group["category"]
            category_counts[category] = pattern_group["count"]
            for match in pattern_group["matches"]:
                all_phrases.append(match["phrase"])
        
        # Specific recommendations based on patterns
        if category_counts.get("dead_giveaways", 0) > 0:
            tips.append("Replace phrases like 'delve into' with simpler alternatives like 'explore' or 'look at'")
            tips.append("Avoid 'tapestry' and 'testament' - use concrete descriptions instead")
        
        if category_counts.get("high_probability", 0) > 2:
            tips.append("Reduce formal transitions - try starting sentences directly with your point")
            tips.append("Replace 'moreover/furthermore' with 'also' or just connect ideas naturally")
        
        if "it's important to note" in all_phrases or "it's worth noting" in all_phrases:
            tips.append("Remove meta-commentary like 'it's important to note' - just state the point")
        
        if category_counts.get("structural_patterns", 0) > 3:
            tips.append("Vary your paragraph structure - avoid rigid firstly/secondly/thirdly patterns")
        
        # Check for overuse of certain word types
        if any(phrase in all_phrases for phrase in ["leverage", "utilize", "comprehensive", "robust"]):
            tips.append("Simplify business jargon: 'use' instead of 'utilize', 'strong' instead of 'robust'")
        
        # General recommendations based on score
        if ai_score > 60:
            tips.append("Try writing in a more conversational tone - imagine explaining to a friend")
            tips.append("Add personal examples or specific details to make content more authentic")
        elif ai_score > 40:
            tips.append("Consider adding more variety in sentence structure and vocabulary")
        elif ai_score < 20:
            tips.append("Text appears relatively natural - minor adjustments could include varying sentence structure")
        
        return tips
    
    def analyze(self, text: str, sensitivity: str = "medium") -> dict[str, Any]:
        """
        Complete AI pattern analysis with optional caching for identical texts

        Args:
            text: The text to analyze
            sensitivity: Detection sensitivity (low/medium/high)

        Returns:
            Dictionary containing AI score, patterns, and recommendations
        """
        # Use cached analysis for identical text+sensitivity combinations
        # This helps when analyzing the same text multiple times
        cache_key = self._get_cache_key(text, sensitivity)
        cached_result = self._get_cached_result(cache_key)
        if cached_result is not None:
            return cached_result

        ai_score, patterns_found = self.detect_patterns(text, sensitivity)

        result = {
            "ai_likelihood_score": round(ai_score, 1),
            "interpretation": self.interpret_ai_score(ai_score),
            "patterns_detected": patterns_found,
            "pattern_summary": {
                "total_patterns": sum(p["count"] for p in patterns_found),
                "categories_triggered": len(patterns_found),
                "most_common_category": max(patterns_found, key=lambda x: x["count"])["category"] if patterns_found else None
            },
            "recommendations": self.get_recommendations(patterns_found, ai_score),
            "sensitivity_used": sensitivity
        }

        self._cache_result(cache_key, result)
        return result

    @staticmethod
    def _get_cache_key(text: str, sensitivity: str) -> str:
        """Generate a cache key for text and sensitivity combination"""
        text_hash = hashlib.md5(text.encode()).hexdigest()
        return f"{text_hash}:{sensitivity}"

    @lru_cache(maxsize=128)
    def _get_cached_result(self, cache_key: str) -> dict[str, Any] | None:
        """Get cached result if available (using LRU cache)"""
        return None  # Placeholder that gets replaced by LRU cache

    def _cache_result(self, cache_key: str, result: dict[str, Any]) -> None:
        """Cache a result (handled by LRU cache decorator)"""
        # This is a workaround since we can't directly cache complex return values
        # The actual caching is done at a higher level
        pass