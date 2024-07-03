# -*- coding: utf-8 -*-

import itertools
import time
import typing as t

import readchar
from rich.console import Console
from rich.live import Live
from rich.screen import Screen
from rich.table import Table
from rich.text import Text
from rich_menu import Menu  # type: ignore

from libs.numer0n_number import Numer0nNumber


class Game:
    def __init__(self):
        self.history: list[Numer0nNumber] = []
        self.console = Console()
        self.number: Numer0nNumber

    def play(self):
        selected_menu = Menu(
            "vs Computer",
            "vs Player",
            "Exit",
            align="left",
            title="Select a mode",
            rule=False,
            panel=False,
        ).ask(screen=True)

        match selected_menu:
            case "vs Computer":
                self.play_vs_computer()
            case "vs Player":
                self.play_vs_player()
            case "Exit":
                return
            case _:
                raise RuntimeError("Unreachable")

    def play_vs_computer(self) -> None:
        with self.console.status(
            Screen("Preparing the game..."),
            spinner="line",
        ):
            time.sleep(2)
            self.number = Numer0nNumber.generate_random_number()

        with Live(
            self.generate_table(),
            auto_refresh=False,
            console=self.console,
            screen=True,
        ) as live:
            for round in itertools.count(1):
                live.update(self.generate_table(""), refresh=True)

                input_generator = ValuedGenerator(self.input_number())
                for intermediate_input in input_generator:
                    live.update(self.generate_table(intermediate_input), refresh=True)

                self.history.append(input_generator.value)
                if self.number.check(input_generator.value)[0] == 3:
                    live.stop()
                    live.console.print(self.generate_table())
                    live.console.print(
                        f"> Hit! The answer is {self.number.number} in {round} rounds."
                    )
                    live.console.print("> Press any key to return to the main menu.")
                    readchar.readchar()
                    live.console.clear()
                    break

        self.play()

    def play_vs_player(self):
        self.console.print("> Not implemented yet!")
        self.console.print("> Press any key to return to the main menu.")
        readchar.readchar()

        self.play()

    def input_number(self) -> t.Generator[str, None, Numer0nNumber]:
        """
        Let the player enter numbers one at a time
        and return intermediate results sequentially.
        """
        intermediate_input = ""

        while True:
            input_char = readchar.readchar()
            if len(intermediate_input) == 3 and input_char == readchar.key.ENTER:
                break

            if input_char == readchar.key.BACKSPACE:
                intermediate_input = intermediate_input[:-1]
            if input_char.isdigit() and input_char not in intermediate_input:
                intermediate_input += input_char

            yield intermediate_input

        return Numer0nNumber(intermediate_input)

    def generate_table(
        self,
        intermediate_input: str | None = None,
        caption: str | None = None,
    ) -> Table:
        table = Table(show_header=True, header_style="bold magenta")

        table.add_column("Round", style="dim", width=5, justify="center")
        table.add_column("?", justify="center")
        table.add_column("?", justify="center")
        table.add_column("?", justify="center")
        table.add_column("EAT", style="bold", justify="center")
        table.add_column("BITE", style="bold", justify="center")

        for round, player_number in enumerate(self.history, 1):
            eat, bite = self.number.check(player_number)
            table.add_row(str(round), *player_number.number, str(eat), str(bite))

        if intermediate_input is not None:
            table.add_row(
                str(len(self.history) + 1),
                *[Text(char, style="bold") for char in intermediate_input],
                *(
                    ["_"] * (len(intermediate_input) < 3)
                    + [
                        Text(" ", style="bold")
                        for _ in range(3 - len(intermediate_input) - 1)
                    ]
                ),
                " ",
                " ",
            )

        if caption is not None:
            table.caption = caption

        return table


class ValuedGenerator[T, U, V]:
    def __init__(self, gen: t.Generator[T, U, V]):
        self.gen = gen

    def __iter__(self) -> t.Generator[T, U, V]:
        self.value = yield from self.gen
        return self.value
