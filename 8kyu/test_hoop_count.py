from hoop_count import hoop_count


def test_keepup():
    assert hoop_count(9) == "Keep at it until you get it"


def test_great():
    assert hoop_count(15) == "Great, now move on to tricks"
