import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "My testreport"

def pytest_html_results_summary(
        prefix, summary, postfix):
    prefix.extend(["<p>My summary</p>"])

# Smidig IT-2 © TIP AS 2024