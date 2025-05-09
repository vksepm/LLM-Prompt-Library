# LLM Prompt Library

---
## ⚡ Quick peek

* **Live demo** → <https://vksepm.github.io/LLM-Prompt-Library/>  
  Zero-JS until you open the page; the prompt list is rendered client-side from `prompts/INDEX.md`.
  
---

## ✨ Prompt catalogue (live)

> 📖 Full list lives in [`prompts/INDEX.md`](prompts/INDEX.md) — rebuilt on every commit.

---

## 🚀 Quick start

```bash
git clone https://github.com/vksepm/LLM-Prompt-Library.git
cd LLM-Prompt-Library

# helper scripts
pip install -r scripts/requirements.txt

# rebuild catalogue & README counts (CI & pre‑commit do this automatically)
python scripts/build_index.py
```
⸻

The library includes several tools to help you work with prompts:

- **🔍 Prompt Validator** - Validates the format and contents of prompt files to ensure they meet our standards.
- **🔄 Prompt Mixer** - Create new prompts by mixing and matching elements from existing prompts.
- **🔢 Token Counter** - Analyze prompt files to count tokens and estimate API costs.
- **📊 Prompt Analyzer** - Evaluate the quality of prompts and get suggestions for improvements.
- **🔄 Prompt Evolution** - Automatically optimize prompts through iterative self-improvement cycles.