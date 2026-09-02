"""P4-3: module, package, import 실행 경계를 관찰한다."""


print("P4-3 module imported")


def run() -> None:
    """Run the current module and import exercise."""
    print()
    print("P4-3 module, package, import 시작")

    from knowledge_lab.lessons import p4_3_modules_and_imports as first_module
    from . import p4_3_modules_and_imports as second_module

    print(f"same module object: {first_module is second_module}")
    print(f"module name: {first_module.__name__}")
    print(f"module package: {first_module.__package__}")
