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

def test_detect_multiline_prefix():
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
        assert expected[i] == justify.detect_multiline_prefix(tests[i])

def test_remove_multiline_prefix():
    original = "Magnam rerum ea cupiditate pariatur ipsam.\nEst sed sed suscipit et error maxime qui non.\nEt iure sequi nihil enim dolorum.\nConsequatur similique quam culpa et."
    tests = [
        "# Magnam rerum ea cupiditate pariatur ipsam.\n# Est sed sed suscipit et error maxime qui non.\n# Et iure sequi nihil enim dolorum.\n# Consequatur similique quam culpa et.",
        "    Magnam rerum ea cupiditate pariatur ipsam.\n    Est sed sed suscipit et error maxime qui non.\n    Et iure sequi nihil enim dolorum.\n    Consequatur similique quam culpa et.",
        "//  Magnam rerum ea cupiditate pariatur ipsam.\n//  Est sed sed suscipit et error maxime qui non.\n//  Et iure sequi nihil enim dolorum.\n//  Consequatur similique quam culpa et.",
    ]
    for test in tests:
        prefix = justify.detect_multiline_prefix(test)
        result = justify.remove_multiline_prefix(test, prefix)
        assert result == original

def test_prepend_multineline_prefix():
    original = "Magnam rerum ea cupiditate pariatur ipsam.\nEst sed sed suscipit et error maxime qui non.\nEt iure sequi nihil enim dolorum.\nConsequatur similique quam culpa et."
    tests = ["# ", "    ", "//  " ]
    expected = [
        "# Magnam rerum ea cupiditate pariatur ipsam.\n# Est sed sed suscipit et error maxime qui non.\n# Et iure sequi nihil enim dolorum.\n# Consequatur similique quam culpa et.",
        "    Magnam rerum ea cupiditate pariatur ipsam.\n    Est sed sed suscipit et error maxime qui non.\n    Et iure sequi nihil enim dolorum.\n    Consequatur similique quam culpa et.",
        "//  Magnam rerum ea cupiditate pariatur ipsam.\n//  Est sed sed suscipit et error maxime qui non.\n//  Et iure sequi nihil enim dolorum.\n//  Consequatur similique quam culpa et.",
    ]
    for i in range(0, len(tests)):
        prefix = tests[i]
        result = justify.prepend_multiline_prefix(original, prefix)
        assert expected[i] == result

def test_justify_block():
    text = "Labore ex id et laborum itaque. Nihil aspernatur aut officiis quos eveniet ex est. Quis mollitia voluptate optio. Nisi laboriosam nam animi et accusamus. Voluptatem explicabo qui facilis voluptate ut. Ut et dolores quas omnis. Et aut repellendus omnis facilis. Aliquam et rerum placeat quis deleniti saepe sed. Fugiat inventore sapiente nihil cupiditate dolores quia fuga velit. Veniam dolore porro aut ratione sed quis. Debitis voluptatem soluta eius delectus eum sint. Atque illo quae provident rem minus."
    sizes = [50, 80, 120]
    expected = [
        "Labore ex id et laborum itaque.  Nihil  aspernatur\naut officiis quos eveniet ex  est.  Quis  mollitia\nvoluptate optio.  Nisi  laboriosam  nam  animi  et\naccusamus.  Voluptatem   explicabo   qui   facilis\nvoluptate ut. Ut et dolores  quas  omnis.  Et  aut\nrepellendus  omnis  facilis.  Aliquam   et   rerum\nplaceat quis deleniti saepe sed. Fugiat  inventore\nsapiente nihil cupiditate dolores quia fuga velit.\nVeniam dolore porro aut ratione sed quis.  Debitis\nvoluptatem soluta eius delectus  eum  sint.  Atque\nillo quae provident rem minus.",
        "Labore ex id et laborum itaque. Nihil aspernatur aut officiis  quos  eveniet  ex\nest. Quis mollitia voluptate optio. Nisi  laboriosam  nam  animi  et  accusamus.\nVoluptatem explicabo qui facilis voluptate ut. Ut et dolores quas omnis. Et  aut\nrepellendus omnis facilis. Aliquam et rerum placeat  quis  deleniti  saepe  sed.\nFugiat inventore sapiente nihil  cupiditate  dolores  quia  fuga  velit.  Veniam\ndolore porro aut ratione sed quis. Debitis voluptatem soluta eius  delectus  eum\nsint. Atque illo quae provident rem minus.",
        "Labore ex id et laborum itaque. Nihil aspernatur aut officiis quos eveniet ex est. Quis mollitia voluptate  optio.  Nisi\nlaboriosam nam animi et accusamus. Voluptatem explicabo qui facilis voluptate ut. Ut  et  dolores  quas  omnis.  Et  aut\nrepellendus omnis facilis. Aliquam et rerum placeat quis deleniti saepe sed. Fugiat inventore sapiente nihil  cupiditate\ndolores quia fuga velit. Veniam dolore porro aut ratione sed quis. Debitis voluptatem soluta  eius  delectus  eum  sint.\nAtque illo quae provident rem minus."
    ]
    l = len(sizes)
    for i in range(0, l):
        n = sizes[i]