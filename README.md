# Readability MCP Server

A high-performance Model Context Protocol (MCP) server that provides comprehensive text analysis tools for readability scoring, sentence difficulty analysis, and AI-generated content detection. This server helps writers improve their AI-assisted writing by providing objective, measurable feedback directly within Claude or other MCP-compatible AI assistants.

**Version 2.0** - Now with batch analysis, text comparison, enhanced validation, and performance optimizations!

## Features

### 🎯 Core Analysis Tools

#### 1. **Text Readability Analysis** (`analyze_text`)
- **Flesch-Kincaid Grade Level** - US grade level needed to understand the text
- **Flesch Reading Ease** - Score from 0-100 (higher = easier to read)
- **SMOG Index** - Simple Measure of Gobbledygook
- **Automated Readability Index** - Estimate of US grade level
- **Coleman-Liau Index** - Grade level based on characters
- **Gunning Fog Index** - Years of education needed
- **Dale-Chall Score** - Comprehension difficulty
- **Linsear Write Formula** - Grade level for technical documents
- Provides word, sentence, and syllable statistics
- Human-readable interpretation of scores
- Estimated reading time

#### 2. **Difficult Sentence Detection** (`find_hard_sentences`)
- Identifies the most complex sentences in your text
- Provides specific reasons why sentences are difficult:
  - Sentence length issues
  - Complex vocabulary (syllable analysis)
  - Multiple clauses and subordinate elements
  - Possible passive voice usage
- Shows sentence position in original text
- Calculates individual grade levels per sentence
- Customizable threshold and count

#### 3. **AI Pattern Detection** (`check_ai_phrases`)
- Detects common AI-generated writing patterns with **optimized pre-compiled regex**
- Provides AI likelihood score (0-100) using **improved density-based algorithm**
- Identifies specific phrases and their context
- Four confidence levels:
  - **Dead Giveaways** - Phrases almost exclusively used by AI
  - **High Probability** - Strong indicators of AI writing
  - **Moderate Indicators** - Common in AI and formal writing
  - **Structural Patterns** - Formatting patterns typical of AI
- Offers specific recommendations for more natural writing
- Adjustable sensitivity levels (low/medium/high)
- **Performance**: 10+ analyses in ~2ms

#### 4. **Batch Analysis** (`batch_analyze`) 🆕
- Analyze multiple texts at once for efficient processing
- Supports up to 20 texts per batch
- Flexible analysis types: readability, sentences, ai_patterns, or all
- Returns aggregate statistics across all texts
- Perfect for comparing multiple drafts or sections

#### 5. **Text Comparison** (`compare_texts`) 🆕
- Compare before/after versions of your text
- Automatic improvement detection:
  - Reading level changes
  - AI-likeness reduction
  - Sentence complexity improvements
  - Word count optimization
- Clear visual feedback with ✅ improvements and ⚠️ regressions
- Actionable recommendations for further refinement

### 🚀 Performance & Quality Improvements

- **Input Validation**: Comprehensive validation for all parameters with clear error messages
- **Pre-compiled Regex**: Pattern matching is ~10x faster with pre-compiled patterns
- **Modern Type Hints**: Consistent Python 3.10+ style type annotations throughout
- **Improved AI Scoring**: Density-based algorithm eliminates false positives for short texts
- **Error Handling**: Detailed error responses with error types and helpful messages
- **Extensive Testing**: Comprehensive test suite covering all features and edge cases

## Installation

### Prerequisites
- Python 3.8 or higher
- `uv` package manager (recommended) or `pip`

### Quick Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/readability-mcp.git
cd readability-mcp
```

2. **Set up virtual environment and install dependencies:**

Using `uv` (recommended):
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

Or using traditional pip:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Download required NLTK data:**
```bash
python -c "import nltk; nltk.download('punkt_tab')"
```

## Configuration for Claude Desktop

Add the server to your Claude Desktop configuration file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "readability-analyzer": {
      "command": "python",
      "args": ["/full/path/to/readability-mcp/server.py"],
      "env": {
        "PYTHONPATH": "/full/path/to/readability-mcp"
      }
    }
  }
}
```

Or if using `uv`:
```json
{
  "mcpServers": {
    "readability-analyzer": {
      "command": "uv",
      "args": ["run", "python", "/full/path/to/readability-mcp/server.py"],
      "cwd": "/full/path/to/readability-mcp"
    }
  }
}
```

## How to Use with Claude

Once configured, you can use natural language to request text analysis. See [PROMPTS.md](PROMPTS.md) for detailed examples.

### Quick Examples:

**Basic readability check:**
```
"Analyze the readability of this text: [paste your text]"
```

**Find difficult sentences:**
```
"Show me the 5 hardest sentences in this document"
```

**Check for AI patterns:**
```
"Does this text sound AI-generated? [paste your text]"
```

**Compare before/after (🆕):**
```
"Compare these two versions of my text and show me what improved:
Original: [paste original]
Revised: [paste revised]"
```

**Batch analysis (🆕):**
```
"Analyze these 3 paragraphs and give me a summary:
1. [first paragraph]
2. [second paragraph]
3. [third paragraph]"
```

**Complete analysis:**
```
"Give me a complete readability analysis including difficult sentences
and AI patterns for this text"
```

## Project Structure

```
readability-mcp/
├── server.py           # Main entry point
├── src/
│   ├── server.py      # MCP server with tool endpoints
│   ├── analyzers/     # Analysis logic modules
│   │   ├── readability.py
│   │   ├── sentences.py
│   │   └── ai_patterns.py
│   └── models/        # Data structures
│       └── results.py
├── requirements.txt   # Python dependencies
├── PROMPTS.md        # Example prompts for Claude
├── CHANGELOG.md      # Version history
└── README.md         # This file
```

## Interpreting Scores

### Flesch-Kincaid Grade Levels
- **5 and below:** Elementary school
- **6-8:** Middle school
- **9-12:** High school
- **13-16:** College
- **17+:** Graduate level

### Flesch Reading Ease
- **90-100:** Very easy (5th grade)
- **80-90:** Easy (6th grade)
- **70-80:** Fairly easy (7th grade)
- **60-70:** Standard (8th-9th grade)
- **50-60:** Fairly difficult (high school)
- **30-50:** Difficult (college)
- **0-30:** Very difficult (graduate)

### AI Likelihood Score
- **0-20:** Very low - naturally written
- **20-40:** Low - mostly natural
- **40-60:** Medium - noticeable AI patterns
- **60-80:** High - strong AI characteristics
- **80-100:** Very high - extensive AI patterns

## Development

### Running Tests
```bash
# Quick functionality test
python test_functionality.py

# Comprehensive test suite (recommended)
python test_comprehensive.py
```

### Running the Server Directly
```bash
# With uv
uv run python server.py

# Or with activated venv
source .venv/bin/activate
python server.py
```

## Troubleshooting

### NLTK Data Error
If you see "Resource punkt_tab not found":
```bash
python -c "import nltk; nltk.download('punkt_tab')"
```

### Server Not Appearing in Claude
1. Verify the config file path is correct
2. Ensure Python/uv path in config is absolute
3. Restart Claude Desktop after config changes
4. Check server health: `uv run python -c "from src.server import health_check"`

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

MIT License - See [LICENSE](LICENSE) file for details

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## Related Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)
- [TextStat Library](https://github.com/shivam5992/textstat)