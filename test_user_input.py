# -*- coding: utf-8 -*-
# test_user_input.py
from unittest.mock import patch
from proportionalrelationship import main

@patch('builtins.input', side_effect=['10'])
@patch('builtins.print')
def test_user_input(mock_print, mock_input):
    main()
    mock_print.assert_called_with("When Lionel completes 10 drills, he plays video games for 0.50 hours.")
