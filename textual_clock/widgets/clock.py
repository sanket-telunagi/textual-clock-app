from time import strftime
from textual.widgets import Static
from pyfiglet import Figlet


class DigitalClock(Static):
    """A digital clock widget that updates every second."""

    DEFAULT_CSS = """
    DigitalClock {
            /* Make the widget fill its container (the TabPane) */
        


            /* Center the time text vertically and horizontally */
            content-align: center middle;

            /* Make the font size responsive to the terminal width (8% of viewport width) */
            text-align: center; 

            /* Use a color from the app's theme */
            color: #8be9fd; /* Dracula Cyan */
        }
    """

    def on_mount(self) -> None:
        """Event handler called when the widget is mounted."""
        # Set an interval to update the time every second

        self.figlet = Figlet(font="smslant")
        self.set_interval(1, self.update_time)
        self.update_time()  # Update once immediately
        # self.set_interval(1, self.update_time)

    def update_time(self) -> None:
        """Update the time display."""
        time_str = strftime("%H:%M:%S")

        # 2. Render the string into large ASCII art text
        ascii_time = self.figlet.renderText(time_str)

        # 3. Update the widget's content with the ASCII art
        self.update(ascii_time)
