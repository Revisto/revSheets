from rich.console import Console

class Rich:
    def time_print(self, time):
        Console().print(f"You have worked for [bold green]{time}[/bold green] today.", style="bold cyan")