# -*- coding: utf-8 -*-

import random
import re
import typing as t

type Eat = int
type Bite = int


class Numer0nNumber:
    def __init__(self, number: str, /):
        number = number.strip()

        if re.match(r"^\d{3}$", number) is None or len(set(number)) != 3:
            raise ValueError(f"number must be 3 distinct digits: '{number}'")

        self._number = number

    def __repr__(self) -> str:
        return f"Numer0nNumber({self.number})"

    @property
    def number(self) -> str:
        return self._number

    def check(self, other: t.Self) -> tuple[Eat, Bite]:
        """
        Return how many EAT and BITE between self and other Numer0nNumber.

        >>> Numer0nNumber("123").check(Numer0nNumber("456"))
        (0, 0)
        >>> Numer0nNumber("123").check(Numer0nNumber("123"))
        (3, 0)
        >>> Numer0nNumber("123").check(Numer0nNumber("321"))
        (1, 2)
        """

        eat = bite = 0
        for i in range(3):
            if self.number[i] in other.number:
                if self.number[i] == other.number[i]:
                    eat += 1
                else:
                    bite += 1
        return eat, bite

    @classmethod
    def generate_random_number(cls) -> t.Self:
        """
        Generate random numer0n number.
        """
        return cls("".join(random.sample("0123456789", 3)))
