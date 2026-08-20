'''Test integrasjonen mellom app og gui'''
from gui_testing import App
import pytest

@pytest.fixture()
# Opprett en instans av App (med Gui) for testing.
def app():
    app = App()
    yield app
    app.gui.destroy()

class TestAppGuiIntegration:
    
    def test_button_click(self, app):
        # Test at teller oppdaters i app
        # og label i gui
        app.gui.button.invoke()
        assert app.teller == 1
        assert app.gui.label.cget("text") == "Antall klikk: 1"

    def test_combobox_select(self, app):
        # Test at valgt_farg oppdateres i app
        # og label i gui
        app.gui.combo.set("Blå")
        assert app.valgt_farge == "Blå"
        assert app.gui.label.cget("text") == "Valgt farge: Blå"

if __name__ == "__main__":
    pytest.main(["-v", "-s"])

# Smidig IT-2 © TIP AS 2024
