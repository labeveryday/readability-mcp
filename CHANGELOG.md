# Changelog

All notable changes to the Readability MCP Server project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-02

### Added
- Initial release of Readability MCP Server
- Three core analysis tools:
  - `analyze_text` - Comprehensive readability scoring with multiple metrics
  - `find_hard_sentences` - Identifies and analyzes difficult sentences
  - `check_ai_phrases` - Detects AI-generated writing patterns
- Support for 8+ readability metrics:
  - Flesch-Kincaid Grade Level
  - Flesch Reading Ease
  - SMOG Index
  - Automated Readability Index
  - Coleman-Liau Index
  - Gunning Fog Index
  - Dale-Chall Readability Score
  - Linsear Write Formula
- AI pattern detection with 4 confidence levels
- Sentence-level difficulty analysis with specific issue identification
- Health check endpoint for server status verification

### Changed
- Refactored from monolithic architecture to modular structure
- Separated business logic into dedicated analyzer modules:
  - `src/analyzers/readability.py` - Readability analysis logic
  - `src/analyzers/sentences.py` - Sentence difficulty logic
  - `src/analyzers/ai_patterns.py` - AI pattern detection logic
- Created data models module for structured results
- Improved code organization and maintainability

### Technical Details
- Built with FastMCP framework for Model Context Protocol support
- Uses textstat library for readability calculations
- NLTK integration for sentence tokenization
- Python 3.8+ compatible
- Virtual environment support with `uv` package manager

### Documentation
- Comprehensive README with installation and usage instructions
- High-Level Design document outlining architecture
- Implementation plan with development phases
- Test suite for module verification

## [0.1.0] - 2025-01-02 (Pre-release)

### Added
- Initial MVP implementation
- Basic MCP server setup
- Core functionality in single file structure