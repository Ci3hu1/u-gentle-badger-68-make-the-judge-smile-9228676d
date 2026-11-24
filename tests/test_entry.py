"""Tests for the Make the Judge Smile entry.

Run: python3 -m unittest discover -s tests -v
"""

import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from main import LINE, validate  # noqa: E402


class TestEntry(unittest.TestCase):
    def test_validate_accepts_the_line(self):
        """validate() passes the approved line through unchanged."""
        self.assertEqual(validate(LINE), LINE)

    def test_validate_rejects_bad_lines(self):
        """validate() rejects blank, over-long, multi-line and control-char lines."""
        for bad in ("", "   ", "x" * 201, "one\ntwo", "a\rb", "tab\there"):
            with self.assertRaises(ValueError, msg=repr(bad)):
                validate(bad)

    def test_line_is_valid_gate_input(self):
        """The line itself passes the sealed gate: 1-200 chars, not blank."""
        stripped = LINE.strip()
        self.assertTrue(stripped, "line must not be only whitespace")
        self.assertGreaterEqual(len(LINE), 1)
        self.assertLessEqual(len(LINE), 200)
        self.assertEqual(LINE.count("\n"), 0, "entry must be a single line")

    def test_program_writes_exact_output(self):
        """main.py writes exactly LINE to <out>/entry.txt, readable by all."""
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, ENTRY_OUTPUT_DIR=tmp)
            result = subprocess.run(
                [sys.executable, str(ROOT / "main.py")],
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            out = Path(tmp) / "entry.txt"
            self.assertTrue(out.is_file())
            data = out.read_bytes()
            self.assertEqual(data.decode("utf-8"), LINE + "\n")
            self.assertEqual(len(data.decode("utf-8").strip()), len(LINE))
            mode = stat.S_IMODE(out.stat().st_mode)
            self.assertEqual(mode, 0o644, "output must be world-readable")


if __name__ == "__main__":
    unittest.main()
