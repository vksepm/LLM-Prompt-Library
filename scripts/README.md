# LLM Prompt Library Scripts



<div align="center">
  <a href="#prompt-validator">Validator</a> •
  <a href="#prompt-mixer">Mixer</a> •
  <a href="#token-counter">Counter</a> •
  <a href="#prompt-analyzer">Analyzer</a> •
  <a href="#prompt-evolution">Evolution</a> •
  <a href="#financial-metacognition">Metacognition</a>
</div>

<br>

This directory contains powerful utility scripts to help maintain and enhance the LLM Prompt Library. These tools enable you to validate, optimize, mix, analyze, and evolve prompts for maximum effectiveness.

---

## Available Scripts


### 1. Prompt Validator

<details>
<summary>Click to expand validator details</summary>

This script validates the format and contents of prompt files to ensure they meet the repository's standards.

#### Features

- ✅ Title format validation
- ✅ Markdown code block verification
- ✅ Configuration option checks
- ✅ Instruction clarity analysis
- ✅ Content length verification

#### Usage

```bash
# Basic usage (checks all prompts in the prompts/ directory)
python scripts/validate_prompts.py

# Validate prompts in a specific directory
python scripts/validate_prompts.py --dir prompts/programming

# Get detailed output about each file
python scripts/validate_prompts.py -v

# Use strict validation mode (more rigorous checks)
python scripts/validate_prompts.py -s
```

The validator operates in two modes:
- **Standard Mode**: Focuses on critical issues while providing warnings for minor issues
- **Strict Mode** (`-s` flag): Applies more rigorous criteria for production-ready prompts

If issues are found, the script provides a detailed report and exits with a non-zero status code, making it suitable for CI/CD pipelines.

</details>

<div align="right">
  <a href="#llm-prompt-library-scripts">
    <img src="https://img.shields.io/badge/⬆️-Back_to_Top-orange" alt="Back to Top">
  </a>
</div>

### 2. Prompt Mixer

<details>
<summary>Click to expand mixer details</summary>

This script allows you to create new prompts by mixing and matching elements from existing prompts in the library.

#### Features

- 🔄 Component extraction from source prompts
- 🔄 Selective component mixing
- 🔄 Coherent prompt assembly
- 🔄 Source attribution tracking
- 🔄 Default element addition

#### Usage

```bash
# Basic usage (creates a random mix using elements from the prompts/ directory)
python scripts/prompt_mixer.py

# Specify a custom title for the mixed prompt
python scripts/prompt_mixer.py --title "My Custom Mixed Prompt"

# Mix specific elements from different prompts
python scripts/prompt_mixer.py \
  --config-from "10-KAnalyzer.md" \
  --instructions-from "programming/Python.md" \
  --examples-from "writing_editing/Proofread.md" \
  --output-from "programming/Code_Explainer.md"

# Specify an output file name
python scripts/prompt_mixer.py --output-file "my_special_mix.md"

# Get detailed output about the mixing process
python scripts/prompt_mixer.py -v
```

The mixer scans prompt files, extracts components, allows selection from different sources, combines them coherently, and saves the result to the `scripts/mixed_prompts/` directory with source attribution.

</details>

<div align="right">
  <a href="#llm-prompt-library-scripts">
    <img src="https://img.shields.io/badge/⬆️-Back_to_Top-orange" alt="Back to Top">
  </a>
</div>

### 3. Token Counter

<details>
<summary>Click to expand token counter details</summary>

This script analyzes prompt files and counts tokens using various tokenization methods, helping you understand token usage and estimate API costs.

#### Features

- 🔢 Multi-model token counting
- 🔢 Category-based token analysis
- 🔢 High-token prompt identification
- 🔢 API cost estimation
- 🔢 Detailed per-file reporting

#### Usage

```bash
# Basic usage (analyzes all prompts in the prompts/ directory)
python scripts/token_counter.py

# Analyze prompts in a specific directory
python scripts/token_counter.py --dir prompts/programming

# Analyze a specific file
python scripts/token_counter.py --file prompts/programming/Python.md

# Use a specific tokenizer model
python scripts/token_counter.py --tokenizer gpt-4

# Skip counting tokens in code blocks
python scripts/token_counter.py --skip-code-blocks

# Include markdown formatting in token counts
python scripts/token_counter.py --include-markdown

# Export results to a JSON file
python scripts/token_counter.py --export token_stats.json

# Get detailed output about each file
python scripts/token_counter.py -v
```

For accurate tokenization with OpenAI models, the script uses the `tiktoken` library. If not available, it falls back to a simple word-based approximation.

</details>

<div align="right">
  <a href="#llm-prompt-library-scripts">
    <img src="https://img.shields.io/badge/⬆️-Back_to_Top-orange" alt="Back to Top">
  </a>
</div>

### 4. Prompt Analyzer

<details>
<summary>Click to expand analyzer details</summary>

This script analyzes the quality, readability, and structure of prompts, providing actionable suggestions for improvements.

#### Features

- 📊 Readability assessment
- 📊 Structure evaluation
- 📊 Clarity analysis
- 📊 Quality scoring
- 📊 Improvement recommendations

#### Usage

```bash
# Basic usage (analyzes all prompts in the prompts/ directory)
python scripts/prompt_analyzer.py

# Analyze a specific file
python scripts/prompt_analyzer.py --file prompts/programming/Python.md

# Get detailed output for each file
python scripts/prompt_analyzer.py -v

# Set minimum recommended examples in prompts
python scripts/prompt_analyzer.py --min-examples 2

# Perform more thorough analysis (slower but more detailed)
python scripts/prompt_analyzer.py --thorough

# Export results to a JSON file
python scripts/prompt_analyzer.py --export analysis_results.json
```

The analyzer evaluates prompts on readability, structure, clarity, and overall quality, providing detailed scores and specific recommendations for improvements.

</details>

<div align="right">
  <a href="#llm-prompt-library-scripts">
    <img src="https://img.shields.io/badge/⬆️-Back_to_Top-orange" alt="Back to Top">
  </a>
</div>

### 5. Prompt Evolution

<details>
<summary>Click to expand evolution details</summary>

This script implements an autonomous prompt optimization system that iteratively refines prompts through self-evolution, critique, and feedback-driven improvement.

#### Features

- 🧬 Evolutionary algorithms
- 🧬 Self-critique mechanisms
- 🧬 Multiple mutation strategies
- 🧬 Quality evaluation metrics
- 🧬 Detailed evolution reporting

#### Usage

```bash
# Basic usage (requires a task description)
python scripts/prompt_evolution.py --task "Summarize scientific papers concisely"

# Start with an initial prompt file
python scripts/prompt_evolution.py --task "Explain complex code" --initial-prompt prompts/programming/Code_Explainer.md

# Run in simulation mode (no API key needed)
python scripts/prompt_evolution.py --task "Write poetry in the style of Emily Dickinson" --simulate

# Customize evolution parameters
python scripts/prompt_evolution.py --task "Generate creative stories" --population 10 --iterations 8

# Use a specific LLM model with your API key
python scripts/prompt_evolution.py --task "Create SQL queries" --model gpt-4 --api-key YOUR_API_KEY

# Get detailed progress information
python scripts/prompt_evolution.py --task "Design marketing copy" --verbose
```

The evolution system maintains a population of prompts that evolve across generations, generates constructive feedback, applies various transformations, and assesses prompt effectiveness using heuristics or LLM feedback.

</details>

<div align="right">
  <a href="#llm-prompt-library-scripts">
    <img src="https://img.shields.io/badge/⬆️-Back_to_Top-orange" alt="Back to Top">
  </a>
</div>

### 6. Financial Metacognition

<details>
<summary>Click to expand financial metacognition details</summary>

The Financial Metacognition module is a specialized tool for analyzing and evaluating AI-generated responses to financial prompts. This tool helps identify potential biases, reasoning limitations, and confidence issues in AI interpretations of financial topics.

#### Features

- 💹 Regional financial terminology analysis
- 💹 Cognitive bias detection
- 💹 Financial reasoning evaluation
- 💹 Confidence assessment
- 💹 Recommendation generation

#### Directory Structure

```
financial_metacognition/
├── financial_metacognition.py - Main analysis script
├── config/ - Configuration files for analysis patterns
│   ├── financial_concepts.json - Financial terminology by region
│   ├── bias_patterns.json - Patterns to detect cognitive biases
│   ├── limitation_patterns.json - Patterns for reasoning limitations
│   └── confidence_patterns.json - Confidence assessment patterns
└── examples/ - Example files for testing
    ├── test_financial_metacognition.py - Test script
    ├── financial_prompt.txt - Example prompt
    └── financial_response.txt - Example response
```

#### Usage

```bash
# Basic Analysis
python financial_metacognition/financial_metacognition.py --prompt-file input/prompt.txt --response-file input/response.txt --output analysis.json

# Region-Specific Analysis
python financial_metacognition/financial_metacognition.py --prompt-file input/prompt.txt --response-file input/response.txt --region EU --output eu_analysis.json

# Running the Test Script
python financial_metacognition/examples/test_financial_metacognition.py --region US --accounting-standard GAAP
```

#### Configuration

The behavior of the financial metacognition module can be customized by modifying the JSON configuration files in the `config/` directory.

#### Dependencies

```bash
pip install spacy
python -m spacy download en_core_web_lg
```

</details>

<div align="right">
  <a href="#llm-prompt-library-scripts">
    <img src="https://img.shields.io/badge/⬆️-Back_to_Top-orange" alt="Back to Top">
  </a>
</div>

## Directories

### mixed_prompts/

This directory contains the output of the prompt mixer tool. All mixed prompts are stored here by default.