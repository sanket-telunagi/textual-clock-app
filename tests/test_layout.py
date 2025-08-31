from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, TabPane, Static
from textual_clock.widgets.stopwatch import Stopwatch
from textual.containers import VerticalScroll


class LayoutTestApp(App):
    CSS_PATH = "test.css"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("q", "quit", "Quit"),
        ("a", "add_stopwatch", "Add"),
        ("r", "remove_stopwatch", "Remove"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with TabbedContent():
            with TabPane("Tab 1"):
                yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch(), id="timers")
            with TabPane("Tab 2"):
                yield Static("This is the content for Tab 2.")
        yield Footer()

    def action_add_stopwatch(self) -> None:
        """An action to add a timer."""
        new_stopwatch = Stopwatch()
        self.query_one("#timers").mount(new_stopwatch)
        new_stopwatch.scroll_visible()

    def action_remove_stopwatch(self) -> None:
        """Called to remove a timer."""
        timers = self.query("Stopwatch")
        if timers:
            timers.last().remove()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = LayoutTestApp()
    app.run()
