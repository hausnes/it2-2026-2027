from vaerapp import App
import pytest


@pytest.fixture()
def app(mocker):
    gui = mocker.MagicMock()
    app = App(gui)
    yield app
    gui.reset_mock()

class TestApp:

    def test_init(self, app):
        assert app is not None
        assert isinstance(app, App)
        assert app.byer == {"Oslo": 20, "Bergen": 15, "Trondheim": 10}
        assert app.valgt_by is None

    def test_on_select(self, app):
        app.on_select("Oslo")
        assert app.valgt_by == "Oslo"
        app.gui.update.assert_called_once_with(by="Oslo", temperatur=20)

    def test_on_select_ukjent_by(self, app):
        app.on_select("London")
        assert app.valgt_by == "London"
        app.gui.update.assert_called_once_with(by="London", temperatur="Ukjent")


if __name__ == "__main__":
    pytest.main(["-v", "-s"])

# Smidig IT-2 © TIP AS 2024
