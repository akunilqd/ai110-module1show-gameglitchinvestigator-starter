from logic_utils import check_guess, parse_guess


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- parse_guess: valid inputs ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_float_rounds_to_int():
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None


# --- parse_guess: invalid inputs ---

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_letters():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_mixed_string():
    ok, value, err = parse_guess("12abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_whitespace_only():
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert value is None
    assert err is not None
