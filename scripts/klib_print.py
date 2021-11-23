# KLIB - print
# wykys 2021

from rich.console import Console

con_stdout = Console()
con_stderr = Console(stderr=True)


def error(text: str) -> None:
    con_stderr.print(f'[bold red]ERROR:[/] [red]{text}[/]')


def warning(text: str) -> None:
    con_stderr.print(f'[bold yellow]WARNING:[/] [yellow]{text}[/]')


def info(text: str) -> None:
    con_stdout.print(f'[bold white]INFO:[/] [white]{text}[/]')
