# KLIB - difference
# wykys 2021

from difflib import Differ
from klib_print import con_stdout, info


def diff_change_log_add(content: str) -> None:
    con_stdout.print(f'[bold green]+[/][green]{content}[/]')


def diff_change_log_del(content: str) -> None:
    con_stdout.print(f'[bold red]-[/][red]{content}[/]')


def diff(old_str_list: list, new_str_list: list) -> None:

    lines_add = 0
    lines_del = 0

    for line in Differ().compare(old_str_list, new_str_list):

        op = line[0]
        line = line[1:].strip()

        if op == '+':
            lines_add += 1
            diff_change_log_add(line)

        elif op == '-':
            diff_change_log_del(line)
            lines_del += 1

    if lines_add > 0 or lines_del > 0:
        info('Change statistics')
        con_stdout.print(f'[bold green]+++[/][green] {lines_add}[/]')
        con_stdout.print(f'[bold red]---[/][red] {lines_del}[/]')
