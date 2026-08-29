"""Module entry point for ``python -m knowledge_lab``."""

from knowledge_lab.lessons import (
    p1_1_execution,
    p1_2_names_and_types,
    p1_3_functions_and_scope,
    p1_4_control_flow,
    p2_1_sequences,
    p2_2_mappings_and_sets,
    p2_3_strings_and_bytes,
    p2_4_comprehensions,
    p3_1_mutability_aliasing_copy,
    p3_2_classes_and_instances,
)


def main() -> None:
    """Run the completed lessons and the current lesson in order."""
    # p1_1_execution.run()
    # p1_2_names_and_types.run()
    # p1_3_functions_and_scope.run()
    # p1_4_control_flow.run()
    # p2_1_sequences.run()
    # p2_2_mappings_and_sets.run()
    # p2_3_strings_and_bytes.run()
    # p2_4_comprehensions.run()
    # p3_1_mutability_aliasing_copy.run()
    p3_2_classes_and_instances.run()


if __name__ == "__main__":
    main()
