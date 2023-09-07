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

def test_is_latex_command():
    tests_1 = [
        '\\section{Chapter 1}',
        '\\begin{center}',
        '\\includegraphics{image.png}',
        '\\includegraphics[width=1]{image.png}',
        '\\end{center}',
    ]
    tests_2 = [
        'begin{center}',
        '\\textbf{Python}: a programming language',
        'end{center}',
    ]
    for test in tests_1:
        assert justify.is_latex_command(test)
    for test in tests_2:
        assert not justify.is_latex_command(test)

def test_text2blocks():
    tests = [
        '\nA quo autem hic quis id neque. Dolor numquam non iure.\nQuod ipsum officia ad repudiandae est id.\n\nEveniet dolores quis debitis. Deserunt quod tempora rerum ea hic cum.\nEst aperiam velit corrupti.\nLaudantium et laboriosam placeat quia consequatur perspiciatis id molestias.\n\nBlanditiis magnam consequatur aperiam rerum rerum.\nVoluptas cumque rerum et molestias quos at quis.',
        'A quo autem hic quis id neque. Dolor numquam non iure.\n\n\n\nBlanditiis magnam consequatur aperiam rerum rerum.\nVoluptas cumque rerum et molestias quos at quis.\n',
    ]
    expected = [
        [
            '',
            'A quo autem hic quis id neque. Dolor numquam non iure.\nQuod ipsum officia ad repudiandae est id.',
            '',
            'Eveniet dolores quis debitis. Deserunt quod tempora rerum ea hic cum.\nEst aperiam velit corrupti.\nLaudantium et laboriosam placeat quia consequatur perspiciatis id molestias.',
            '',
            'Blanditiis magnam consequatur aperiam rerum rerum.\nVoluptas cumque rerum et molestias quos at quis.',
        ],
        [
            "A quo autem hic quis id neque. Dolor numquam non iure.",
            '', '', '',
            "Blanditiis magnam consequatur aperiam rerum rerum.\nVoluptas cumque rerum et molestias quos at quis.",
        ],
    ]

    for i in range(0, len(tests)):
        blocks = justify.text2blocks(tests[i])
        assert len(blocks) == len(expected[i])
        assert blocks == expected[i]

def test_detect_common_prefix():
    tests = [
        '# Lorem upsum\n# Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis\n# voluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas\n# reiciendis velit itaque voluptatibus. Tempora repellendus iure qui natus rerum',
        '# Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis\n# voluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas\n#\n#\n# reiciendis velit itaque voluptatibus. Tempora repellendus iure qui natus rerum\n# reiciendis',
        '\t\t\tHello\n\t\t\tQuae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis\n\t\t\tvoluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas\n',
        '    Lorem upsum\n    Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis\n    voluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas\n',
        '    // LOREM UPSUM\n    //\n    // Tempora repellendus iure qui natus rerum\n    // voluptatibus id incidunt incidunt doloremque.\n    // Est ut laborum dolorum voluptas\n    //\n    //\n    // Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis',
    ]
    expected = [
        "# ", "#", "\t\t\t", "    ", "    //"
    ]
    for i in range(0, len(tests)):
        assert expected[i] == justify.detect_common_prefix(tests[i])