from textual.app import ComposeResult

# from textual.containers import Vertical
from textual.reactive import reactive
from textual.widgets import Button, Input, Static


class Hourglass(Static):
    """A widget that renders an hourglass visualization."""

    percent = reactive(1.0)  # Start full (1.0 = 100%)

    def _generate_hourglass_text(self, percent: float) -> str:
        """Generates the ASCII art for the hourglass."""
        height = 10
        width = 2 * height - 1
        lines = []

        total_sand_chars = sum(2 * i - 1 for i in range(1, height))
        sand_to_render = int(total_sand_chars * percent)

        # Top of the hourglass
        lines.append(" " + "▄" * (width - 2) + " ")

        rendered_sand = 0
        for i in range(1, height):
            line_width = 2 * i - 1
            padding = " " * (height - i)

            # Bottom part (filled with static sand)
            sand_in_line = 0
            if sand_to_render > rendered_sand:
                sand_in_line = min(line_width, sand_to_render - rendered_sand)

            sand_chars = "█" * sand_in_line + " " * (line_width - sand_in_line)
            lines.append(padding + sand_chars + padding)
            rendered_sand += line_width

        # Invert for the top part (sand draining)
        lines.reverse()

        # Middle part
        lines.insert(height, " " * (height - 1) + "X" + " " * (height - 1))

        # Bottom of the hourglass
        lines.append(" " + "▀" * (width - 2) + " ")

        return "\n".join(lines)

    def watch_percent(self, percent: float) -> None:
        """Called when the percent attribute changes."""
        self.update(self._generate_hourglass_text(percent))


class TimerWidget(Static):
    """A timer widget with an hourglass visualization."""

    remaining_time = reactive(0)

    def __init__(self) -> None:
        super().__init__()
        self.total_time = 0
        self.timer = self.set_interval(1, self.tick, pause=True)

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Seconds (e.g., 60)", type="integer")
        yield Button("Start Timer", id="start-timer", variant="success")
        yield Hourglass()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start-timer":
            try:
                input_widget = self.query_one(Input)
                self.total_time = int(input_widget.value)
                self.remaining_time = self.total_time
                self.timer.resume()
            except (ValueError, IndexError):
                # Handle cases where input is empty or invalid
                pass

    def tick(self) -> None:
        """Called every second by the timer."""
        self.remaining_time -= 1
        if self.remaining_time < 0:
            self.timer.pause()
            self.remaining_time = 0

        hourglass = self.query_one(Hourglass)
        if self.total_time > 0:
            hourglass.percent = self.remaining_time / self.total_time
        else:
            hourglass.percent = 0

    def watch_remaining_time(self, time: int) -> None:
        """Update the input with the remaining time."""
        self.query_one(Input).value = str(time)
