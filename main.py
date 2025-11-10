from pathlib import Path
from re import compile
from typing import Optional

from requests import RequestException, get

EMAIL_PATTERN = compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')


def extract_emails(
    input_file: Path,
    output_file: Path,
    remote_text_url: Optional[str] = None,
    timeout: float = 10
) -> None:
    """
    Collect email addresses from a local text file (and optional remote text)
    and save unique addresses to output_file.

    Parameters
    ----------
    input_file : Path
        Path to the local .txt file containing emails.
    output_file : Path
        Destination file for the extracted email list.
    remote_text_url : Optional[str]
        If provided, fetch additional text content from this URL.
    timeout : float
        Timeout (seconds) for the HTTP request.
    """

    try:
        if not input_file.is_file():
            raise FileNotFoundError(f'Input file not found: {input_file}')

        text_sources = [input_file.read_text(encoding='utf-8',
                                             errors='ignore')]

        if remote_text_url:
            response = get(remote_text_url, timeout=timeout)
            response.raise_for_status()
            text_sources.append(response.text)

        found_emails = set()
        for text in text_sources:
            found_emails.update(EMAIL_PATTERN.findall(text))

        if not found_emails:
            print('No email addresses detected.')
            output_file.write_text('', encoding='utf-8')
            return

        sorted_emails = sorted(found_emails, key=str.lower)
        output_file.write_text(
            '\n'.join(sorted_emails),
            encoding='utf-8'
        )
        print(f'Extracted {len(sorted_emails)} unique email(s) to \
            {output_file}')

    except (FileNotFoundError, PermissionError) as fnfe_pe:
        print(f'File error: {fnfe_pe}')

    except RequestException as rexc:
        print(f'Network error while fetching remote text: {rexc}')

    except OSError as ose:
        print(f'I/O error: {ose}')
