from pathlib import Path

from decouple import config
from termcolor import colored


def generate_rc_files():
    # Load token from environment variables using python-decouple
    testpypi_token = config("TESTPYPI_TOKEN")

    # Define the content of the .pypirc file
    pypirc_content = (
        "[distutils]\n"
        "  index-servers =\n"
        "    testpypi\n\n"
        "[testpypi]\n"
        f"  username = __token__\n"
        f"  password = {testpypi_token}\n\n"
    )

    # Get the project folder using pathlib
    project_folder = Path(__file__).parent.parent.resolve()

    # Write the .pypirc file in the project folder
    pypirc_path = project_folder / ".pypirc"
    pypirc_path.write_text(pypirc_content)
    print(colored(f".pypirc has been generated at {pypirc_path}", "green"))


if __name__ == "__main__":
    generate_rc_files()
