# 📧 Simple Email Addresses Extractor

Lightweight utility to extract unique email addresses from a local text file and optionally from a remote text URL. Designed for Windows development and scripting use. Works as a library function or a simple script.

---

- ✅ Extracts emails using a robust regex
- ✅ Writes deduplicated, sorted results to a file
- ✅ Optional remote text fetch with network error handling
- ✅ Clear errors and return behavior for scripting

---

## Table of contents

- 🔧 Requirements
- 🚀 Quick Start (Windows)
- 🧩 Usage (library + CLI)
- 🛡️ Error handling & behavior
- 🧪 Tests
- 🧾 License
- 🤝 Contributing
- ⚠️ Security & privacy

---

## 🔧 Requirements

- Python 3.8+
- requests (only required if using the remote_text_url option)

Install in a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you don't have a requirements file, install requests:

```powershell
pip install requests
```

---

## 🚀 Quick Start (Windows)

Example: extract emails from `input.txt` and write to `out.txt`:

```powershell
cd 'c:\Users\user\Desktop\Python_Pro_BootCamp\Web_Dev\CodeAlpha\Simple_Email_Addresses_Extractor'
python -c 'from pathlib import Path; from main import extract_emails; extract_emails(Path("input.txt"), Path("out.txt"))'
```

With an additional remote text source:

```powershell
python -c 'from pathlib import Path; from main import extract_emails; extract_emails(Path('input.txt'), Path('out.txt'), remote_text_url="https://example.com/list.txt")'
```

---

## 🧩 Usage (library)

You can import and call the function directly from other Python code:

```python
from pathlib import Path
from main import extract_emails

input_file = Path(r"C:\path\to\emails_input.txt")
output_file = Path(r"C:\path\to\emails_addresses.txt")

extract_emails(input_file, output_file, remote_text_url="https://example.com/emails_data.txt", timeout=8)
```

Function signature:

```python
def extract_emails(
    input_file: Path,
    output_file: Path,
    remote_text_url: Optional[str] = None,
    timeout: float = 10
) -> None:
    ...
```

- `input_file`: Path to local text file (required).
- `output_file`: Path to write unique addresses (required).
- `remote_text_url`: optional URL to fetch extra text from (HTTP GET).
- `timeout`: HTTP request timeout in seconds.

---

## 🛡️ Error handling & behavior

- If the local input file does not exist: logs/prints a FileNotFoundError message.
- Network errors while fetching remote text are caught and reported.
- Output file will be created (overwritten) even if no emails found (empty file).
- Email extraction uses a permissive RFC-like regex; if you need strict RFC parsing, post-process results.

---

## 🧪 Tests

- Add tests under `tests/` to validate regex behavior, remote fetch handling (mock requests), and file writing/permissions.
- Example using pytest and requests-mock:
  - Mock remote URL responses
  - Validate that duplicates are removed and output sorted

---

## 🧾 License

MIT License — see full text below.

```
MIT License

Copyright (c) 2025 Theophilus Asamoah

Permission is hereby granted, free of charge, to any person obtaining a copy

...

```

[`see license`](https://github.com/Suiper34)

---

## 🤝 Contributing

- Fork the repo and open a PR.
- Add tests for new behavior.
- Keep functions small and well-documented.
- If adding features that fetch remote content, include timeout & retry policies.

---

## ⚠️ Security & privacy

- The tool writes all extracted addresses to disk. Ensure you comply with privacy laws (GDPR, etc.) before collecting or storing email lists.
- When fetching remote text, only call trusted URLs. The project does not validate remote content beyond using requests.
