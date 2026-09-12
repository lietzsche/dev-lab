"""P4-4: project와 dependency 경계를 관찰한다."""

import sys
import tomllib
from importlib.metadata import distribution

import knowledge_lab


def run() -> None:
    """Run the current project and dependency exercise."""
    print()
    print("P4-4 project와 dependency 시작")

    distribution_name = "knowledge-lab"
    import_package_name = "knowledge_lab"
    print(f"distribution_name: {distribution_name}")
    print(f"import_package_name: {import_package_name}")
    print(
        "distribution_name == import_package_name: "
        f"{distribution_name == import_package_name}"
    )
    print(f"knowledge_lab.__name: {knowledge_lab.__name__}")
    print(f"sys.executable: {sys.executable}")
    print(f"sys.prefix: {sys.prefix}")
    print(f"sys.base_prefix: {sys.base_prefix}")
    print(f"sys.prefix != sys.base_prefix: {sys.prefix != sys.base_prefix}")
    installed_distribution = distribution(distribution_name)
    print(f"installed_distribution's Name: {installed_distribution.metadata['Name']}")
    print(f"installed_distribution.version: {installed_distribution.version}")
    with open("pyproject.toml", "rb") as file:
        config = tomllib.load(file)
        print(f"in block, pyproject file closed: {file.closed}")
    print(f"after block, pyproject file closed: {file.closed}")
    print(f"build-system/build-backend: {config['build-system']['build-backend']}")
    print(f"project/name: {config['project']['name']}")
    print(f"project/dependencies: {config['project']['dependencies']}")
    build_dependencies = config["build-system"]["requires"]
    runtime_dependencies = config["project"]["dependencies"]
    print(f"build_dependencies: {build_dependencies}")
    print(f"runtime_dependencies: {runtime_dependencies}")
    installed_runtime_dependencies = installed_distribution.requires or []
    print(f"installed_runtime_dependencies: {installed_runtime_dependencies}")
    print(
        "runtime_dependencies == installed_runtime_dependencies: "
        f"{runtime_dependencies == installed_runtime_dependencies}"
    )
    console_script = config["project"]["scripts"]["knowledge-lab"]
    print(f"console script: {console_script}")
