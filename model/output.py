from rich.console import Console

class Rich:
    def time_print(self, minutes):
        Console().print(f"You have worked for [bold green]{minutes} mintes[/bold green] today.", style="bold cyan")