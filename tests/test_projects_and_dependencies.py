"""Public behavior tests for P4-4 projects and dependencies."""

import io
import tomllib
import unittest
from contextlib import redirect_stdout
from importlib.metadata import distribution

from packaging.requirements import Requirement

from knowledge_lab.lessons import p4_4_projects_and_dependencies


class ProjectsAndDependenciesTest(unittest.TestCase):
    def test_project_metadata_matches_installed_distribution(self) -> None:
        with open("pyproject.toml", "rb") as file:
            config = tomllib.load(file)

        installed = distribution(config["project"]["name"])

        self.assertEqual(config["project"]["name"], installed.metadata["Name"])
        self.assertEqual(config["project"]["version"], installed.version)
        self.assertEqual([], config["project"]["dependencies"])

        requirements = [Requirement(value) for value in installed.requires or []]
        runtime_requirements = [
            requirement
            for requirement in requirements
            if requirement.marker is None or requirement.marker.evaluate({"extra": ""})
        ]
        self.assertEqual([], runtime_requirements)

    def test_run_reports_project_and_entry_point_boundaries(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            p4_4_projects_and_dependencies.run()

        lines = output.getvalue().splitlines()
        self.assertIn("distribution_name: knowledge-lab", lines)
        self.assertIn("import_package_name: knowledge_lab", lines)
        self.assertIn(
            "console script: knowledge_lab.__main__:main",
            lines,
        )
