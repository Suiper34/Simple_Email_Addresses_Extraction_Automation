from pathlib import Path
from main import extract_emails


if __name__ == '__main__':
    extract_emails(
        input_file=Path(r'C:\path\to\emails.txt'),
        output_file=Path(r'D:\path\to\clean_emails.txt'),
        remote_text_url='https://example.com/emails.txt'  # optional
    )
