from unittest.mock import patch

from app.config import get_required_env


def test_missing_environment_variable():
    with patch.dict("os.environ", {"TEST_SECRET": ""}):
        try:
            get_required_env("TEST_SECRET")
        except RuntimeError as error:
            assert str(error) == (
                "Required configuration is missing: TEST_SECRET"
            )
            print("PASS: Missing configuration is handled safely.")
        else:
            raise AssertionError(
                "Expected RuntimeError for missing configuration"
            )


if __name__ == "__main__":
    test_missing_environment_variable()