[comment]: # (progress: false)
[comment]: # (hash: true)
[comment]: # (transitionSpeed: 'fast')
[comment]: # (display: 'flex')
[comment]: # (width: 1920)
[comment]: # (height: 1080)
[comment]: # (margin: 0)

<style>
section {
  justify-content: center;
  align-items: center;
  flex-direction: column;
  font-size: 120%;
}

section.row {
  flex-direction: row;
}
</style>


# DÆNSK

The Danish language, improved

[comment]: # (!!!)

![](media/fotos/jellingesten.jpg)

<div>

- Knows Danish <!-- .element: class="fragment fade-up" -->
- Knows its flaws <!-- .element: class="fragment fade-up" -->
- Can fix them <!-- .element: class="fragment fade-up" -->

</div>

[comment]: # (!!! class="row" data-auto-animate)


# Danish alphabet

ᚠ ᚢ ᚦ ᚬ ᚱ ᚴ ᚼ ᚾ ᛁ ᛅ ᛋ ᛏ ᛒ ᛘ ᛚ ᛦ

⇓

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z **Æ Ø Å**

[comment]: # (!!!)


# Æ Ø Å

- åh: ah/oh
- øh: eh
- æh: uh

[comment]: # (!!! data-auto-animate)

# Æ Ø Å

- åh: ah/oh
- øh: eh
- æh: uh
- But also:
  - ah: ah
  - ih: ah/oh
  - uh: oh

[comment]: # (!!! data-auto-animate)


# Flaws of Danish

- Many vowel sounds
  - i, iː, y, yː, u, uː,\
    e, eː, ø, øː, ə, o, oː,\
    ɛ, ɛː, œ, œː, ɐ, ɔ, ɔː,\
    a, aː, ɑ, ɑː, ɒ, ɒː
- Big gap between spoken and written language

[comment]: # (!!! data-auto-animate)

# Flaws of Danish

- ~~Many vowel sounds~~
- ~~Big gap between spoken and written language~~
- Focus now: **Somewhat big alphabet**
- (Other flaws to come later in the presentation)

Note: I'm going to address the two flaws indirectly, but I want to focus
on something more specific.

[comment]: # (!!! data-auto-animate)


# Somewhat big alphabet

- **Danish:**
  - Population of Danish speakers: ~6 million
  - Number of letters in alphabet: 29
  - ~4.83 μ-letters per person

- **English:**
  - Population of English speakers: ~1.5 billion
  - Number of letters in alphabet: 26
  - ~0.02 μ-letters per person

Note: This is a measure of how big a burden each speaker of the language
needs to carry.  By trimming the language down in size, it will be
easier to carry it into the future.

[comment]: # (!!!)


# Somewhat big alphabet

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Æ Ø Å

[comment]: # (!!! data-auto-animate)

# Somewhat big alphabet

**A** B C D **E** F G H **I** J K L M N **O** P Q R S T **U** V W X **Y** Z **Æ** **Ø** **Å**

[comment]: # (!!! data-auto-animate)

# Somewhat big alphabet

- A
- E
- I
- O
- U
- Y
- Æ
- Ø
- Å

[comment]: # (!!! data-auto-animate)

# Somewhat big alphabet

- ~~A~~
- ~~E~~
- ~~I~~
- ~~O~~
- ~~U~~
- ~~Y~~
- Æ
- Ø
- Å

[comment]: # (!!! data-auto-animate)

# Somewhat big alphabet

- Æ
- Ø
- Å

[comment]: # (!!! data-auto-animate)

# Somewhat big alphabet

B C D F G H J K L M N P Q R S T V W X Z **Æ** **Ø** **Å**

[comment]: # (!!! data-auto-animate)

# Somewhat big alphabet

B C D F G H J K L M N P Q R S T V W X Z **Æ** **Ø** **Å**

29 - 6 = 23 letters (nice!)

[comment]: # (!!! data-auto-animate)


# DÆNSK

Note: We don't have an "a" anymore, so we'll use what sounds closest to
it.

[comment]: # (!!!)

# Going from dansk to dænsk

```sh
sed -r -e 's/[eiy]+/æ/g' -e 's/[ou]+/ø/g' -e 's/a+/å/g'
```

- e, i, y → æ
- o, u -> ø
- a -> å

Note: We collapse multiple equal vowels into just one in order to avoid
things like "æææ".

[comment]: # (!!!)


# Some improvements and almost no problems

[comment]: # (!!!)

<section class="row">

![](media/864px-CairoEgMuseumTaaMaskMostlyPhotographed.jpg)

<div>

## Egyptology

- Previously:
  - "egyptologi" *or*
  - "ægyptologi"
- Now: Always just "ægæptøløgæ" <!-- .element: class="fragment fade-up" -->

</div>

</section>

Note: This is a common schism in Danish.

[comment]: # (!!!)


## snædæ

- sneede (*snowed*)
- snyde (*cheat*)

[comment]: # (!!! data-background-image="media/sne.jpg" data-background-size="contain")


## øffæcæl

- officiel (*official*)
- uofficiel (*unofficial*)

[comment]: # (!!! data-auto-animate)

## øffæcæl

- officiel (*official*)
- uofficiel (*unofficial*)

<br>

**Solution:** ikke (*not*) or **ækkæ**

- øffæcæl (*official*)
- ækkæ øffæcæl (*unofficial*)

[comment]: # (!!! data-auto-animate)

## øffæcæl

- officiel (*official*)
- uofficiel (*unofficial*)

<br>

**Solution:** ikke (*not*) or **ækkæ**

- øffæcæl (*official*)
- ækkæ øffæcæl (*unofficial*)

<br>

**Further simplification:**

- øffæcæl (*official*)
- ækøffæcæl (*unofficial*)

[comment]: # (!!! data-auto-animate)

![](media/Flag_of_Finland.svg) <!-- .element: style="width: 500px; position: absolute; top: 50px; left: 100px" -->

## fænsk

- finsk (*Finnish*)
- fynsk (*of Funen*)

![](media/Location_map_Funen.svg) <!-- .element: style="width: 500px; position: absolute; top: 50px; right: 100px" -->


[comment]: # (!!!)


# Some improvements and almost no problems

- Only around 1% of Danish words are causing problems
- There are always workarounds


[comment]: # (!!!)


# Encoding Dænsk

**Problem:** Existing character encodings support more characters than necessary

[comment]: # (!!!)

# Encoding Dænsk: UTF-8

Already too big for normal Danish

[comment]: # (!!!)

# Encoding Dænsk: ISO-8859-1

Much better:

![](media/Latin-1-infobox.svg)

**But still supports too many characters**

[comment]: # (!!!)

# New encoding

- Goal: Save bytes
- Inspiration: UTF-8

[comment]: # (!!! data-auto-animate)

# ØTF-2

- Goal: Save bytes
- Inspiration: UTF-8


[comment]: # (!!! data-auto-animate)

# ØTF-TØ

- Goal: Save bytes
- Inspiration: UTF-8

[comment]: # (!!! data-auto-animate)

# ØTF-TØ

- Always at least 2 bits:
  - `0 0`: **æ**
  - `0 1`: **ø**
  - `1 0`: **å**
  - `1 1`: 5 extra bits in this case:
    - 20 spots for consonants
    - 11 spots for punctuation and symbols
    - 1 reserved
- ⇒ Each letter is represented with either 2 or 7 bits.

[comment]: # (!!! data-auto-animate)

# ØTF-TØ testing

**Idea:**

1. Find a text in Danish
2. Check how much space it takes up in UTF-8
3. Check how much space it would take up in dænsk in ØTF-TØ

[comment]: # (!!! data-auto-animate)

# ØTF-TØ testing

**Idea:**

1. Find a text in Danish

Project Gutenberg?

[comment]: # (!!! data-auto-animate)

# ØTF-TØ testing

**Idea:**

1. Find a text in Danish

~~Project Gutenberg?~~

Problem: Old Danish text doesn't use **Å**

[comment]: # (!!! data-auto-animate)

# ØTF-TØ testing

![](media/wikidanmark.png)

[comment]: # (!!!)

```c
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <ctype.h>

enum letter_kind {
  ae, oe, aa, other
};

int main() {
  int c;
  size_t bit_count = 0;
  enum letter_kind prev = other;

  // Assume that input is in ISO 8859-1 such that æ, ø, and å are one byte each.
  while ((c = getchar()) != EOF) {
    switch (c) {
    case 'e':
    case 'i':
    case 'y':
    case 0xe6: // æ
      if (prev != ae) {
        bit_count += 2;
        prev = ae;
      }
      break;
    case 'o':
    case 'u':
    case 0xf8: // ø
      if (prev != oe) {
        bit_count += 2;
        prev = oe;
      }
      break;
    case 'a':
    case 0xe5: // å
      if (prev != aa) {
        bit_count += 2;
        prev = aa;
      }
      break;
    default: // Like ASCII
      // Assume that input contains only non-æøå characters that are also supported in ønæcødæ.
      bit_count += 5;
      prev = other;
      break;
    }
  }

  printf("Bits: %lu\nBytes: %lu\n", bit_count, bit_count / 8);
}
```
<!-- .element: style="font-size: 15px; height: 950px;" -->

[comment]: # (!!!)

# ØTF-TØ testing

- UTF-8: 3033 bytes
- ØTF-TØ: 688 bytes
- **Over 4 times smaller**

[comment]: # (!!!)

[comment]: # (!!! data-background-image="media/æøå.svg" data-background-size="contain")


# Back to the flaws of Danish

- We have addressed an important *word-level* problem
- We have yet to do something about the *language structure*

[comment]: # (!!!)

# Central flaw

## Difficult to parse by old technology

Note: This is at least my claim.  Why is this a flaw?  Let's take a look at modern software.

[comment]: # (!!!)

# Current software

## Typical stack

1. Transistors
2. CPU
3. Operating system kernel
4. Virtual operating system kernel
5. Machine code
6. Deployed image
7. Executable file format
8. Compiler
9. Build system
10. Source code
11. Integrated development environment

Note: This is not an original point I'm making.  Software complexity is
bad, and many people are saying it.

[comment]: # (!!! data-auto-animate)

# Slightly older software

## Typical stack

1. Transistors
2. CPU
3. Operating system kernel
4. Machine code
5. Executable file format
6. Compiler
7. Source code
8. Editor

Note: This feels like a better compromise.  If we look at software from
this era, it can have lots of complexity, but the overall complexity of
the system is limited by the fewer and more expensive computing
resources available back then.

[comment]: # (!!! data-auto-animate)

# Year cutoff: *1989* <!-- .element: class="fragment fade-up" -->

![](media/walter.jpg) <!-- .element: height="800" class="fragment fade-up" -->

Note: For any technology that I'll use from now on, I'll make sure to
indicate that it's from before the 90's.

[comment]: # (!!!)

# Parsing troubles

Parsing: Converting text characters into structured data

![](media/knuth-lr-1965.png)

[comment]: # (!!!)

# Parsing troubles

- Great at parsing programming languages
- Less good at parsing human languages

[comment]: # (!!!)

# Modern approaches

- Machine learning based on statistical methods
- Lots of compute

Note: This is also for translation.

[comment]: # (!!!)

Note: Statistics also existed in the 80's, but it wouldn't have been
feasible for a hobbyist to really use such methods back then because of
the lack of big compute.

[comment]: # (!!! data-background-image="media/techcheck-machine-learning.svg" data-background-size="contain")

# Classic approaches

[comment]: # (!!!)

![](media/danish-field-grammar-page1.png) <!-- .element: height="1000" -->

- "Danish Field Grammar in Typed Prolog"
- Year: 1986
- Uses Prolog to parse Danish for sentence analysis

Note: I found this paper over 10 years ago.

[comment]: # (!!! class="row")

[comment]: # (!!! data-background-image="media/techcheck-prolog.svg" data-background-size="contain")

# But it's slow

![](media/danish-field-grammar-øl.png) <!-- .element: height="300" -->

# ... in 1986 <!-- .element: class="fragment fade-up" -->

Note: So maybe this will be fast enough today?

[comment]: # (!!!)

# Addressing the final flaw

- I claimed that Danish was hard to parse by old technology
- But this is old technology which claims to parse Danish
- Is my claim wrong?
- Let's try to parse Danish

[comment]: # (!!!)

# Scouring the literature

[comment]: # (!!!)

![](media/didepåprolog.png) <!-- .element: height="1000" -->

[comment]: # (!!!)

![](media/didepåprolog-brok.png) <!-- .element: height="165" -->

![](media/didepåprolog-bus.png)

Note: The actual complaints are not relevant, but I like how the author
spends a good chunk dissing the software.

[comment]: # (!!!)

# Diderichsen?

![](media/didepåprolog-titel.png)

![](media/diderichsen-dst.png) <!-- .element: class="fragment fade-up" -->
