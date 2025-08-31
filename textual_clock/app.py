from textual.app import App, ComposeResult

# from textual.containers import Container
from textual.widgets import Header, Footer, TabbedContent, TabPane
from textual.containers import VerticalScroll

# We will create these files in the next steps
from textual_clock.widgets.clock import DigitalClock
from textual_clock.widgets.stopwatch import Stopwatch
# from widgets.timer import TimerWidget


class TerminalClockApp(App):
    """A terminal-based clock application."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("q", "quit", "Quit"),
        ("a", "add_stopwatch", "Add"),
        ("r", "remove_stopwatch", "Remove"),
    ]

    # Link our CSS file
    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with TabbedContent():
            with TabPane("Clock", id="tab-clock"):
                yield DigitalClock()
            with TabPane("Stopwatch"):
                yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch(), id="timers")
        # with TabPane("Timer", id="tab-timer"):
        #     yield TimerWidget()  # Placeholder
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
    app = TerminalClockApp()
    app.run()
