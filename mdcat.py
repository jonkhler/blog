#!/usr/bin/env python3

import re
import sys
from pathlib import Path
import glob
import argparse
from datetime import datetime

def process_file(filepath):
    """
    Process a Markdown file, replacing @include directives with the contents of specified files.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        print(f"Error: File {filepath} does not exist.", file=sys.stderr)
        return ""

    output = []
    with filepath.open("r", encoding="utf-8") as file:
        for line in file:
            match = re.match(r"@include\s+(.+)", line.strip())
            if match:
                pattern = match.group(1)
                included_files = sorted(
                    glob.glob(str(filepath.parent / pattern)),
                    key=lambda f: Path(f).stat().st_ctime,  # Sort by creation time
                    reverse=True,
                )
                if not included_files:
                    print(f"Warning: No files match the pattern {pattern}.", file=sys.stderr)
                for included_file in included_files:
                    included_file = Path(included_file)
                    if included_file.is_file():
                        last_modified_time = datetime.fromtimestamp(included_file.stat().st_mtime)
                        formatted_time = last_modified_time.strftime("%Y-%m-%d %H:%M:%S")
                        
                        included_content = []
                        with included_file.open("r", encoding="utf-8") as included:
                            lines = included.readlines()

                            # Remove leading empty lines
                            while lines[0].strip() == "":
                                lines.pop(0)

                            # Check if the first line is a header (starts with "#")
                            if lines and lines[0].startswith("#"):
                                # Insert the modification time below the first header
                                included_content.append(lines[0])  # Header
                                included_content.append(f"<span class=\"last-modified\">Last modified: {formatted_time}</span>\n")  # Time below header
                                included_content.extend(lines[1:])  # Rest of the content
                                print(f"Info: Including {included_file} (last modified: {formatted_time}).", file=sys.stderr)
                            else:
                                # If no header, just append the file as is
                                included_content.extend(lines)

                        result = "".join(included_content)
                        if not result.endswith("\n"):
                            result += "\n"
                        output.append(result)
                    else:
                        print(f"Warning: {included_file} is not a valid file.", file=sys.stderr)
            else:
                output.append(line)
    return "".join(output)

def main():
    """
    Main function to process a file and print the result to stdout.
    """
    parser = argparse.ArgumentParser(
        description="Preprocess a Markdown file by replacing @include directives with file contents."
    )
    parser.add_argument(
        "input_file", type=str, help="Path to the input Markdown file."
    )
    args = parser.parse_args()

    input_file = Path(args.input_file)

    processed_content = process_file(input_file)
    sys.stdout.write(processed_content)

if __name__ == "__main__":
    main()