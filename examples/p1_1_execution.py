"""P1-1: observe when module-level code and guarded code execute."""

language = "Python"

print(f"module level: {__name__=}")
print(f"display: {language}")
print(f"debug: {language!r}")
print(f"type: {type(language)}")

if __name__ == "__main__":
    print("entry point: direct execution")
