import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Testreport"
    
# Smidig IT-2 © TIP AS 2024