from time import strftime
from textual.widgets import Static


class DigitalClock(Static):
    """A digital clock widget that updates every second."""

    def on_mount(self) -> None:
        """Event handler called when the widget is mounted."""
        # Set an interval to update the time every second
        self.set_interval(1, self.update_time)

    def update_time(self) -> None:
        """Update the time display."""
        self.update(strftime("%I:%M:%S %p"))  # Format: 10:30:59 PM
