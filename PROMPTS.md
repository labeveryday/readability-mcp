# Example Prompts for Readability MCP Server

This guide provides example prompts you can use with Claude when the Readability MCP Server is installed. These prompts demonstrate various ways to analyze and improve your writing.

## Table of Contents
- [Basic Analysis](#basic-analysis)
- [Targeted Improvements](#targeted-improvements)
- [Content Type Specific](#content-type-specific)
- [Workflow Examples](#workflow-examples)
- [Advanced Usage](#advanced-usage)

---

## Basic Analysis

### Simple Readability Check
```
Analyze the readability of this text:

[paste your text here]
```

### Quick Grade Level Assessment
```
What grade level is this written at?

[paste your text here]
```

### Get All Metrics
```
Give me all readability metrics for this text:

[paste your text here]
```

---

## Targeted Improvements

### Make Text Easier to Read
```
This text needs to be at an 8th grade reading level. Analyze it and tell me 
what needs to be simplified:

[paste your text here]
```

### Find Problem Sentences
```
Find the 5 most difficult sentences in this text and explain why they're hard to read:

[paste your text here]
```

### Identify Complex Vocabulary
```
Which sentences in this text have vocabulary that's too complex for a general audience?

[paste your text here]
```

---

## Content Type Specific

### Blog Post Analysis
```
I'm writing a blog post for a general audience. Check if this is easy enough to read 
and doesn't sound too AI-generated:

[paste your blog post here]
```

### Technical Documentation
```
This is technical documentation for developers. Check the readability and identify 
any sentences that are unnecessarily complex:

[paste your documentation here]
```

### Academic Writing
```
This is for an academic paper. Analyze the readability and tell me if any sentences 
are too convoluted even for academic standards:

[paste your academic text here]
```

### Email Communication
```
Check if this email is clear and easy to understand for business communication:

[paste your email here]
```

---

## Workflow Examples

### Complete Writing Review
```
Please perform a complete analysis of this text:
1. Overall readability scores
2. The 5 hardest sentences to read
3. Check if it sounds AI-generated
4. Give me specific recommendations for improvement

[paste your text here]
```

### Before/After Comparison
```
Compare the readability of these two versions of my text:

Version 1:
[paste original text]

Version 2:
[paste revised text]

Which is better and why?
```

### Progressive Improvement
```
Help me improve this text step by step:
1. First, analyze its current readability
2. Find the most problematic sentences
3. After I revise it, check it again

[paste your text here]
```

---

## Advanced Usage

### AI Pattern Detection

#### Check for AI Writing
```
Does this text sound like it was written by AI? Give me specific examples:

[paste your text here]
```

#### Remove AI Patterns
```
This text sounds too much like AI wrote it. Show me which phrases are the biggest 
giveaways and suggest alternatives:

[paste your text here]
```

#### High Sensitivity Check
```
Check this text for AI patterns using high sensitivity. I want to catch even 
subtle indicators:

[paste your text here]
```

### Custom Analysis

#### Focus on Specific Metrics
```
Analyze this text but only show me:
- Flesch-Kincaid Grade Level
- SMOG Index
- Estimated reading time

[paste your text here]
```

#### Sentence Difficulty with Custom Threshold
```
Find all sentences that are above a 12th grade reading level:

[paste your text here]
```

#### Section-by-Section Analysis
```
Analyze each section of this document separately:

Section 1: Introduction
[paste section 1]

Section 2: Main Content
[paste section 2]

Section 3: Conclusion
[paste section 3]
```

---

## Prompt Templates

### For Content Creators
```
I'm creating content for [target audience]. My goal is to maintain a 
[grade level] reading level. Please:
1. Analyze the current readability
2. Identify sentences that don't meet this target
3. Check for AI-sounding phrases
4. Suggest specific improvements

[paste your content here]
```

### For Editors
```
I'm editing this piece for publication. Please:
1. Provide comprehensive readability metrics
2. Flag the top 10 most difficult sentences
3. Identify any AI-generated patterns
4. Assess if it's appropriate for our target demographic (age/education level)

[paste content here]
```

### For Students
```
I need to ensure my essay is at an appropriate academic level but still readable. 
Please check:
1. Is it at a college reading level (grades 13-16)?
2. Are there any sentences that are unnecessarily complex?
3. Does it sound too much like AI helped write it?

[paste essay here]
```

### For Business Communications
```
This is a [type of document: report/proposal/email] for [audience: executives/clients/team]. 
Please ensure it's:
1. Professional but accessible (8th-10th grade level)
2. Free of overly complex sentences
3. Natural sounding (not AI-generated)

[paste business document here]
```

---

## Tips for Best Results

1. **Be Specific**: Tell Claude exactly what reading level or audience you're targeting
2. **Iterate**: Use the analysis to revise, then check again
3. **Context Matters**: Mention if it's technical, academic, or general content
4. **Combine Tools**: Use all three tools together for comprehensive analysis
5. **Set Thresholds**: Specify how many difficult sentences you want to see
6. **Adjust Sensitivity**: Use different AI detection sensitivities based on your needs

---

## Common Patterns to Watch For

When Claude identifies these issues, consider revising:

### Readability Red Flags
- Sentences over 25 words
- Average syllables per word over 2
- Passive voice constructions
- Multiple subordinate clauses
- Technical jargon without explanation

### AI Pattern Indicators
- "Delve into" or "tapestry of"
- Excessive use of "moreover," "furthermore"
- "It's important to note that..."
- Rigid structure (firstly, secondly, thirdly)
- Overuse of "leverage," "utilize," "robust"

---

## Quick Reference Commands

- **Basic check**: "Analyze readability"
- **Find problems**: "Show difficult sentences"
- **AI check**: "Check for AI patterns"
- **Complete analysis**: "Full readability analysis"
- **Simplify**: "Make this easier to read"
- **Compare**: "Which version is clearer?"

Remember: The more specific your request, the more helpful the analysis will be!