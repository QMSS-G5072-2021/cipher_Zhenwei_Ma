def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    assert isinstance(shift,str) == False, "Shift cannot be strings"
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

import pytest

def test_cipher():
    result = cipher('math', shift = 1, encrypt = True)
    expected = 'nbui'
    assert result == expected, 'result not equal to expected value'


def test_cipher_negative():
    result = cipher('nbui', shift = -1, encrypt = True)
    expected = 'math'
    assert result == expected, 'result not equal to expected value'
    
def test_cipher_symbol():
    result = cipher('Data-Analusis', shift = 1, encrypt = True)
    expected = 'Ebub-Bobmvtjt'
    assert result == expected, 'result not equal to expected value'
    
def test_cipher_integer():
    with pytest.raises(AssertionError):
        cipher('math', 'one', True)
