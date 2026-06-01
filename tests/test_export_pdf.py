import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.export_pdf import sanitize_config


class ExportPdfTests(unittest.TestCase):
    def make_temp_config(self, content: str) -> Path:
        root = Path(".build_logs")
        root.mkdir(exist_ok=True)
        directory = TemporaryDirectory(dir=root)
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "_config_test.yml"
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def test_sanitize_config_preserves_custom_excludes(self):
        config = """
        title: Example book
        exclude_patterns:
          - _build
          - hidden_chapter/
          - extra_files/**
        """
        path = self.make_temp_config(config)
        sanitize_config(path)
        modified = path.read_text(encoding="utf-8")

        self.assertIn("hidden_chapter/", modified)
        self.assertIn("extra_files/**", modified)
        self.assertIn("_build", modified)
        self.assertIn("**.ipynb_checkpoints", modified)
        self.assertIn(".git", modified)
        self.assertIn(".github", modified)

    def test_sanitize_config_adds_minimal_excludes_when_missing(self):
        config = """
        title: Example book
        author: Testing
        """
        path = self.make_temp_config(config)
        sanitize_config(path)
        modified = path.read_text(encoding="utf-8")

        self.assertIn("exclude_patterns", modified)
        self.assertIn("_build", modified)
        self.assertIn("**.ipynb_checkpoints", modified)
        self.assertIn(".git", modified)
        self.assertIn(".github", modified)


if __name__ == "__main__":
    unittest.main()
