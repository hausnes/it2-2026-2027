'''Test App-klassen isolert ved å mocke Gui-klassen'''
from gui_testing import App
import pytest

@pytest.fixture()
def app(mocker):
    # gui_mock = mocker.Mock()
    gui_mock = mocker.MagicMock()
    app = App()
    app.gui = gui_mock
    return app

class TestAppUnit:
    
    def test_on_click(self, app):
        app.on_click()
        assert app.teller == 1
        app.gui.update.assert_called_once_with(verdi=1, type="teller")

    def test_on_select(self, app):
        app.on_select("Blå")
        assert app.valgt_farge == "Blå"
        app.gui.update.assert_called_once_with(verdi="Blå", type="farge")

# Smidig IT-2 © TIP AS 2024
