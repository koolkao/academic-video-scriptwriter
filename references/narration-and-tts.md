# Narration and TTS

The narration is written to be heard once, at speaking speed, by a text-to-speech voice.
Listeners cannot reread a sentence, so the writing has to carry them.

## Writing for the ear

- One idea per sentence. Most sentences under about twenty words; the checker warns above
  twenty-eight.
- Put the new information at the end of the sentence, where the voice lands.
- Name the thing before describing it: "The darkest ring is where most birds sit," not "Where
  most birds sit is shown by the darkest ring."
- Use the same word for the same thing every time. Synonyms make listeners think a new thing
  has arrived.
- Point with words when the eye has to move: "on the left," "the top row," "the orange
  island." This also serves viewers who cannot see the screen well.
- Say essential visual relationships out loud. If the takeaway is that a curve tilts upward,
  the narration says it tilts upward.
- Do not narrate the screen word for word, and do not put a different explanation on screen
  than the one being spoken. Labels, equations, and short headings on screen are fine.

## Sound like a person who knows the material

No disclaimers, stock qualifiers, presenter filler, or inflated vocabulary. The checker
enforces a list (`scripts/banned_phrases.txt`); the habit matters more than the list:

- Start with the content. "Gentoo penguins are the heavy ones," not "In this video, we'll
  dive into penguin body mass."
- State scope and uncertainty as facts inside the claim (see
  `evidence-and-integrity.md`, *Qualifiers without hedging*).
- Cut sentences that announce importance instead of showing it ("This is a crucial point").
- No rhetorical questions that the next sentence answers, more than once per video.
- No three-adjective lists, no "not just X, but Y" constructions, no closing moral.

## Numbers, spoken and shown

Every statistic has two forms.

- **On screen:** the full reported value, with its uncertainty and context. For example
  `5076 g · SD 504 · n = 123`, or `r = −0.24 · n = 342 · p < 0.001`. Keep the project's precision.
- **Spoken:** the part that matters for the argument, rounded only as far as it stays true.
  "Gentoos average about five thousand grams." "A weak negative correlation, minus point two
  four."

Speak a number only when the viewer needs it. Two or three spoken numbers per topic is plenty;
the rest can live on screen. Every line that states a fact carries its `{C..}` tag.

## Making text TTS-safe

TTS voices misread symbols, abbreviations, and digits in ways that differ between providers. The
script removes the ambiguity before it reaches any provider:

- Spell every number as it should be said: "three hundred and forty two," "point zero five,"
  "twenty twenty-three" (year) versus "two thousand and twenty-three" (count).
- Write symbols as words: "less than," "plus or minus," "percent," "per square meter,"
  "versus."
- No parentheses, slashes, or ampersands in spoken text. Rewrite as a sentence.
- Units in words: "millimeters," not "mm."
- Every acronym and every unusual term goes in the teaching plan's Pronunciation table with
  how to say it ("ANOVA → an-OH-vuh", "Gentoo → JEN-too"). Say whether an acronym is spoken as
  letters or as a word.
- Flag heteronyms that the context might not settle ("lead," "minute," "content," "row") in the
  Pronunciation table.
- Prefer full sentences to fragments; many voices flatten fragments.

## Pauses and emphasis

Pause marks are neutral. The production handoff maps them to whatever the chosen TTS supports
(for example SSML `<break>`, a provider's pause syntax, or silence inserted in editing).

| Mark | Length | Use |
| --- | --- | --- |
| `{beat}` | about 0.75 s | After a key number or a short claim, so it lands. |
| `{look:N}` | N seconds | While the viewer reads a figure or watches it change. Longer for denser figures: a bar chart may need two seconds, a heat map or 3D view five or more. |
| `{break}` | about 1.5 s | At a topic boundary, after the bridge and before the next announcement. |

Place pauses with a purpose: after a key number, before a takeaway, after a showpiece, and at
every topic boundary. Do not pause after every sentence; constant pauses sound like a slow
voice, not like emphasis.

`*word*` marks emphasis. Use it for contrast ("within *each* species") at most once or twice
per topic. Some voices ignore it; the sentence should still work without it.

## Speech rate

The teaching plan sets a planning rate (default 150 words per minute). It is an estimate for
budgeting, not a rule about learning. Real timing comes from the rendered audio. If the
estimate exceeds the target duration, cut scope; never raise the rate to fit.
