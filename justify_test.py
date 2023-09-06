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
        # test 1
        """
A quo autem hic quis id neque. Dolor numquam non iure.
Quod ipsum officia ad repudiandae est id.

Eveniet dolores quis debitis. Deserunt quod tempora rerum ea hic cum.
Est aperiam velit corrupti.
Laudantium et laboriosam placeat quia consequatur perspiciatis id molestias.

Blanditiis magnam consequatur aperiam rerum rerum.
Voluptas cumque rerum et molestias quos at quis.""",
        # test 2
        """A quo autem hic quis id neque. Dolor numquam non iure.



Blanditiis magnam consequatur aperiam rerum rerum.
Voluptas cumque rerum et molestias quos at quis.
""",

    ]
    expected = [
        # test 1
        [
            '',
            """A quo autem hic quis id neque. Dolor numquam non iure.
Quod ipsum officia ad repudiandae est id.""",
            '',
            """Eveniet dolores quis debitis. Deserunt quod tempora rerum ea hic cum.
Est aperiam velit corrupti.
Laudantium et laboriosam placeat quia consequatur perspiciatis id molestias.""",
            '',
            """Blanditiis magnam consequatur aperiam rerum rerum.
Voluptas cumque rerum et molestias quos at quis.""",
        ],
        # test 2
        [
            "A quo autem hic quis id neque. Dolor numquam non iure.",
            '', '', '',
            """Blanditiis magnam consequatur aperiam rerum rerum.
Voluptas cumque rerum et molestias quos at quis.""",
        ],
    ]

    for i in range(0, len(tests)):
        blocks = justify.text2blocks(tests[i])
        assert len(blocks) == len(expected[i])
        assert blocks == expected[i]

def test_detect_common_prefix():
    tests = [
# test 1
"""# Lorem upsum
# Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis
# voluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas
# reiciendis velit itaque voluptatibus. Tempora repellendus iure qui natus rerum""",

# test 2
"""# Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis
# voluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas
#
#
# reiciendis velit itaque voluptatibus. Tempora repellendus iure qui natus rerum
# reiciendis""",

# test 3
"""\t\t\tHello
\t\t\tQuae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis
\t\t\tvoluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas
""",

# test 4
"""    Lorem upsum
    Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis
    voluptatibus id incidunt incidunt doloremque. Est ut laborum dolorum voluptas
""",

# test 5
"""    // LOREM UPSUM
    //
    // Tempora repellendus iure qui natus rerum
    // voluptatibus id incidunt incidunt doloremque.
    // Est ut laborum dolorum voluptas
    //
    //
    // Quae voluptatum earum sapiente unde ab corporis ducimus iure. Debitis
""",

    ]
    expected = [
        "# ", "# ", "\t\t\t", "    ", "    // "
    ]
    for i in range(0, len(tests)):
        assert expected[i] == justify.detect_common_prefix(tests[i])