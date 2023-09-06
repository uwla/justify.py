import justify

def test_is_blank():
    tests_1 = [
        '',
        '\n',
        ' ' * 4,
        ' ' * 8,
        '\t',
        '\t' * 2,
        '\t' * 2 + ' ' * 2,
    ]
    tests_2 = [
        'Hello',
        '       World',
        '\t\t\t\t\t\t!',
    ]
    for test in tests_1:
        assert justify.is_blank(test)
    for test in tests_2:
        assert not justify.is_blank(test)

def test_is_start_of_list_item():
    tests_1 = [
        '- test test test test.'
        '* test test test test.'
        '5. test test test test.'
        '5) test test test test.'
        '15. test test test test.'
        '15) test test test test.'
        '\\item Test test test.',
    ]
    tests_2 = [
        '-test test test test.'
        '-- test test test test.'
        '** test test test test.'
        '5 test test test test.'
        '5.test test test test.'
        '5)test test test test.'
        '15 test test test test.'
        '15.test test test test.'
        '15)test test test test.'
    ]
    for test in tests_1:
        assert justify.is_start_of_list_item(test)
    for test in tests_2:
        assert not justify.is_start_of_list_item(test)