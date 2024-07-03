# -*- coding: utf-8 -*-

import pytest

from libs.numer0n_number import Numer0nNumber


class TestNumer0nNumber:
    @pytest.fixture
    def valid_numer0n_number_123(self):
        """
        Return a valid Numer0nNumber("123") instance.
        """
        return Numer0nNumber("123")

    @pytest.fixture
    def valid_numer0n_number_123_(self):
        """
        Return another valid Numer0nNumber("123") instance.
        """
        return Numer0nNumber("123")

    @pytest.fixture
    def valid_numer0n_number_456(self):
        """
        Return a valid Numer0nNumber("456") instance.
        """
        return Numer0nNumber("456")

    @pytest.fixture
    def valid_numer0n_number_321(self):
        """
        Return a valid Numer0nNumber("321") instance.
        """
        return Numer0nNumber("321")

    def test_invalid_numer0n_number_too_short(self):
        """
        Confirm that an error is raised if the number is too short.
        """
        with pytest.raises(ValueError):
            Numer0nNumber("12")

    def test_invalid_numer0n_number_too_long(self):
        """
        Confirm that an error is raised if the number is too long.
        """
        with pytest.raises(ValueError):
            Numer0nNumber("1234")

    def test_invalid_numer0n_number_not_number(self):
        """
        Confirm that an error is raised if the number is not a number.
        """
        with pytest.raises(ValueError):
            Numer0nNumber("b2c")

    def test_invalid_numer0n_number_duplicate(self):
        """
        Confirm that an error is raised if the number has duplicate digits.
        """
        with pytest.raises(ValueError):
            Numer0nNumber("112")

    def test_check_no_match(
        self,
        valid_numer0n_number_123: Numer0nNumber,
        valid_numer0n_number_456: Numer0nNumber,
    ):
        """
        Verify that the check method returns the correct number of EAT and BITE.
        """
        eat, bite = valid_numer0n_number_123.check(valid_numer0n_number_456)
        assert eat == 0 and bite == 0

    def test_check_all_match(
        self,
        valid_numer0n_number_123: Numer0nNumber,
        valid_numer0n_number_123_: Numer0nNumber,
    ):
        """
        Verify that the check method returns the correct number of EAT and BITE.
        """
        eat, bite = valid_numer0n_number_123.check(valid_numer0n_number_123_)
        assert eat == 3 and bite == 0

    def test_check_some_match(
        self,
        valid_numer0n_number_123: Numer0nNumber,
        valid_numer0n_number_321: Numer0nNumber,
    ):
        """
        Verify that the check method returns the correct number of EAT and BITE.
        """
        eat, bite = valid_numer0n_number_123.check(valid_numer0n_number_321)
        assert eat == 1 and bite == 2
