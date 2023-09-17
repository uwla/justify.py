# JUSTIPY

Python script to justify plain text.

## Features

- custom line width
- preserve indentation
- preserve multiline prefix (comments)
- preserve paragraphs
- format text lists
- indent list items
- some LaTeX support

## Example

The following text A:

```
Minima est voluptas dicta consequatur quia aut. Iusto necessitatibus ut et et
aut labore cupiditate fugiat. Itaque omnis pariatur debitis odit placeat
dolores. Repellat eum cumque veritatis impedit nisi. Rerum facilis
recusandae velit voluptates officia veritatis. Nam molestiae nemo non placeat
rem consectetur iste eveniet.

Sint odit aut et amet consequatur magnam eos veniam. Dolor rerum labore ut. Ut
consectetur id voluptatem voluptas error laudantium. Non est sit libero sit
dolorem asperiores. Sed nemo dicta consequatur non minima aspernatur est.

        Cumque laborum sunt ipsa asperiores est repellendus quis voluptas. At
        incidunt consequuntur ullam. Est exercitationem quidem non et distinctio
        eum ipsam aut. Nam facilis ratione atque voluptate et hic. Voluptas
        voluptatem minus ut id neque placeat. Delectus reiciendis autem labore
        culpa consequatur omnis sint aspernatur.

Velit dignissimos eum ut provident cumque natus. Ut sed reiciendis quis maxime
dicta. Nihil quo aperiam reiciendis. Debitis et eveniet modi numquam aut qui
quis.

1. Occaecati quo quo aut ut.
2. Atque vel ducimus modi in consequatur.
3. Numquam et ut ipsam.
4. Eos molestiae tenetur ex assumenda et reiciendis.

Esse fuga debitis aperiam dolorum vero quia sed rerum. Sit temporibus voluptatem
nostrum quisquam accusantium ea non nulla.

    // Et architecto est fuga et et deserunt. Et blanditiis ut rerum qui aut quisquam
    // praesentium. Assumenda esse cum id temporibus corporis nihil inventore. Et
    // molestiae omnis quia dolorum eos.
    //
    //     * Corrupti at ipsam debitis et quod ut nobis fuga. Tenetur dolores
    //     omnis id. Sint quod aut sit. Iure in et ipsam minus recusandae odio. Libero consequuntur aut molestias dolor
    //     * Molestias officiis molestiae voluptas asperiores quam non temporibus. Possimus
    //     at voluptatibus et architecto deserunt.
    //     * Quidem blanditiis recusandae est inventore. Ut assumenda veritatis atque minima
    //     commodi necessitatibus et. Voluptatum odio aut ut aut qui voluptatem porro sed.
    //     Quo dolore repellendus nam et quae.
    //
    // Dolore occaecati vero incidunt
    // animi voluptatibus enim vel in. At consequatur illum qui consequatur iste
    // officiis qui nihil. Aut doloribus iusto odio.

\begin{itemize}
    \item Quidem quos sunt voluptates sed est. Voluptates magni voluptate minus error dolores eum atque. Aut adipisci modi et accusamus.
    \item Sit aut sit omnis rem quia sed maiores similique. Sed voluptas omnis ullam laboriosam cumque eveniet. Voluptate eum nesciunt eum alias quis velit.
    \begin{enumerate}
        \item Eum fuga id voluptas ullam et libero. Recusandae reiciendis et sequi. Possimus molestiae officiis nobis voluptas ut dignissimos vero. Reiciendis quia fuga earum nulla nesciunt quo pariatur. Quasi repellendus iure quam quibusdam. Eum quo animi vero aut asperiores fuga.
        \item Neque natus quam consequatur et laboriosam dolorum. Sequi repellat minus dolorem nisi et atque. Cum quis similique voluptas facere suscipit itaque.
    \end{enumerate}
    \item Beatae quae accusamus vero ut et architecto molestiae. Voluptas tempora saepe dolor ad voluptate doloremque. Odit voluptatem veniam officiis quis. Minima et quo accusantium reiciendis quo doloremque est qui. Nulla qui aliquid omnis incidunt.
\end{itemize}

Eaque delectus harum et cupiditate aut dolorum aut aut.

15. Dolor sed magni odio fugiat nisi sit temporibus officia. Fugiat sunt non ex doloremque voluptas quos facere ipsa. Consequatur assumenda deleniti culpa inventore vel dolores. Consectetur esse voluptatum omnis recusandae non. Et illum provident non veritatis assumenda numquam dolor ipsa. Adipisci voluptatibus nesciunt rerum et vel quaerat.
16. Assumenda tenetur quo et voluptates voluptatem blanditiis at illum. Tenetur quia incidunt voluptatem et in magni quis repudiandae. Maiores aut ut quo sequi error corrupti in vero.
```

Becomes the following text B:

```
Minima est voluptas dicta consequatur quia aut. Iusto necessitatibus  ut  et  et
aut labore  cupiditate  fugiat.  Itaque  omnis  pariatur  debitis  odit  placeat
dolores. Repellat eum cumque veritatis impedit nisi.  Rerum  facilis  recusandae
velit  voluptates  officia  veritatis.  Nam  molestiae  nemo  non  placeat   rem
consectetur iste eveniet.

Sint odit aut et amet consequatur magnam eos veniam. Dolor rerum labore  ut.  Ut
consectetur id voluptatem voluptas error laudantium.  Non  est  sit  libero  sit
dolorem asperiores. Sed nemo dicta consequatur non minima aspernatur est.

        Cumque laborum sunt ipsa asperiores est repellendus  quis  voluptas.  At
        incidunt consequuntur ullam. Est exercitationem quidem non et distinctio
        eum ipsam aut. Nam facilis ratione  atque  voluptate  et  hic.  Voluptas
        voluptatem minus ut id neque placeat. Delectus reiciendis  autem  labore
        culpa consequatur omnis sint aspernatur.

Velit dignissimos eum ut provident cumque natus. Ut sed reiciendis  quis  maxime
dicta. Nihil quo aperiam reiciendis. Debitis et eveniet  modi  numquam  aut  qui
quis.

1. Occaecati quo quo aut ut.
2. Atque vel ducimus modi in consequatur.
3. Numquam et ut ipsam.
4. Eos molestiae tenetur ex assumenda et reiciendis.

Esse fuga debitis aperiam dolorum vero quia sed rerum. Sit temporibus voluptatem
nostrum quisquam accusantium ea non nulla.

    // Et architecto est fuga et et deserunt. Et blanditiis  ut  rerum  qui  aut
    // quisquam praesentium. Assumenda esse cum  id  temporibus  corporis  nihil
    // inventore. Et molestiae omnis quia dolorum eos.
    //
    //     * Corrupti at ipsam debitis et quod ut nobis  fuga.  Tenetur  dolores
    //       omnis id. Sint quod aut sit. Iure  in  et  ipsam  minus  recusandae
    //       odio. Libero consequuntur aut molestias dolor
    //     * Molestias  officiis  molestiae   voluptas   asperiores   quam   non
    //       temporibus. Possimus at voluptatibus et architecto deserunt.
    //     * Quidem blanditiis recusandae est inventore. Ut assumenda  veritatis
    //       atque minima commodi necessitatibus et. Voluptatum odio aut ut  aut
    //       qui voluptatem porro sed. Quo dolore repellendus nam et quae.
    //
    // Dolore occaecati  vero  incidunt  animi  voluptatibus  enim  vel  in.  At
    // consequatur illum qui consequatur iste officiis qui nihil. Aut  doloribus
    // iusto odio.

\begin{itemize}
    \item Quidem quos sunt voluptates sed est. Voluptates magni voluptate  minus
          error dolores eum atque. Aut adipisci modi et accusamus.
    \item Sit aut sit omnis rem quia sed maiores similique. Sed  voluptas  omnis
          ullam laboriosam cumque eveniet. Voluptate eum nesciunt eum alias quis
          velit.
    \begin{enumerate}
        \item Eum fuga id voluptas ullam et  libero.  Recusandae  reiciendis  et
              sequi. Possimus molestiae officiis nobis voluptas  ut  dignissimos
              vero. Reiciendis quia fuga  earum  nulla  nesciunt  quo  pariatur.
              Quasi repellendus iure quam quibusdam.  Eum  quo  animi  vero  aut
              asperiores fuga.
        \item Neque natus quam consequatur et laboriosam dolorum. Sequi repellat
              minus dolorem nisi et atque. Cum quis  similique  voluptas  facere
              suscipit itaque.
    \end{enumerate}
    \item Beatae quae  accusamus  vero  ut  et  architecto  molestiae.  Voluptas
          tempora saepe dolor ad voluptate doloremque.  Odit  voluptatem  veniam
          officiis quis. Minima et quo accusantium reiciendis quo doloremque est
          qui. Nulla qui aliquid omnis incidunt.
\end{itemize}

Eaque delectus harum et cupiditate aut dolorum aut aut.

15. Dolor sed magni odio fugiat nisi sit temporibus officia. Fugiat sunt non  ex
    doloremque voluptas quos facere ipsa. Consequatur assumenda  deleniti  culpa
    inventore vel dolores. Consectetur esse voluptatum omnis recusandae non.  Et
    illum  provident  non  veritatis  assumenda  numquam  dolor  ipsa.  Adipisci
    voluptatibus nesciunt rerum et vel quaerat.
16. Assumenda tenetur quo et voluptates voluptatem blanditiis at illum.  Tenetur
    quia incidunt voluptatem et in magni quis repudiandae. Maiores  aut  ut  quo
    sequi error corrupti in vero.
```

## Limitations

- It has some bugs
- It can only detect indentation in a text block
- It cannot detect different indentation within the same text block

A text block is a sequence of non-empty lines surrounded by an empty line  above
the first line and an empty line after the last line. An empty line  is  defined
as a line that has no characters or has only tabs and spaces.

## Roadmap

- Overcome the describe limitations
