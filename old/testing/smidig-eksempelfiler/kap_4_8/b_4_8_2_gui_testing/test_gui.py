from gui_testing import Gui
import tkinter as tk
from tkinter import ttk
import pytest


@pytest.fixture()
def gui(mocker):
    app = mocker.MagicMock()
    gui = Gui(app)
    yield gui
    app.reset_mock()
    gui.update_idletasks()
    gui.destroy()
    gui.quit()

class TestGuiUnit:

    def test_create_widgets(self, gui):
        # Test at widgetene er opprettet som forventet
        assert gui.winfo_exists()
        assert gui.frame.winfo_exists()
        assert isinstance(gui.frame, tk.Frame)
        assert gui.button.winfo_exists()
        assert isinstance(gui.button, tk.Button)
        assert gui.button.cget("text") == "Klikk meg!"
        assert gui.combo.winfo_exists()
        assert isinstance(gui.combo, ttk.Combobox)
        assert gui.combo.cget("values") == ("Rød", "Grønn", "Blå")
        assert gui.combo.get() == "Velg farge"
        assert gui.label.winfo_exists()
        assert isinstance(gui.label, tk.Label)
        assert gui.label.cget("text") == "Antall klikk: 0"

    def test_update(self, gui):
        # Test at update-metoden oppdaterer labelen som forventet
        gui.update(verdi=42, type="teller")
        assert gui.label["text"] == "Antall klikk: 42"
        gui.update(verdi="Grønn", type="farge")
        assert gui.label["text"] == "Valgt farge: Grønn"

    def test_endret_farge(self, gui):
        # Test at endret_farge-metoden oppfører seg som forventet
        gui.farge_valg.set("Grønn")
        gui.app.on_select.assert_called_once_with("Grønn")

    def test_button(self, gui):
        # Test at knappen oppfører seg som forventet
        gui.button.invoke()
        gui.app.on_click.assert_called_once()

    def test_combobox(self, mocker):
        # Test at komboboksen oppfører seg som forventet.
        # Mock endret_farge før denne bindes til farge_valg
        # med trace_add når Gui-instansen opprettes.
        mock_endret_farge =  mocker.patch.object(
            Gui, "endret_farge", autospec=True)
        app = mocker.MagicMock()
        gui = Gui(app)
        gui.combo.set("Grønn")
        assert gui.farge_valg.get() == "Grønn"
        mock_endret_farge.assert_called_once()
        args = mock_endret_farge.call_args[0]
        assert "write" in args


# Smidig IT-2 © TIP AS 2024
