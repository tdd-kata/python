from src.map.dict import basic_dictionary

def test_basic_dictionary():
    expect = {
        "hi": "hello",
        "id": 1,
    }

    assert basic_dictionary() == expect
