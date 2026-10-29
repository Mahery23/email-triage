import pytest

from email_triage import main


# Check that main prints the project greeting
def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert "email-triage" in capsys.readouterr().out
