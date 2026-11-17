# Engagement

Some speakers hold a room with material that would put a textbook reader to sleep. Much of it is
technique, not charisma, and technique can be written into a script. The methods here are the
ones that teachers such as Richard Feynman used constantly. They are not an imitation of any
person's voice or persona; a TTS voice "doing" a famous speaker sounds like a parody.

Engagement is fourth in the priority order. Every technique here works inside the teaching
structure (roadmap, announcements, wrap-ups, bridges) and never replaces it.

## 1. Open with a puzzle

Start from something odd that the viewer can see, and let the concept arrive as the answer.

- The puzzle is a concrete observation from the project's data, stated as fact with its claim
  tag, plus the question it raises: "Across three hundred and forty two penguins, longer bills
  come with shallower bills. That seems backwards. Shouldn't a bigger bill be bigger every
  way?" It is not a vague teaser ("What if everything you knew about penguins was wrong?").
- The puzzle must not give away the answer to a later prediction. Pose the question; keep the
  answer for the reveal. Check the goal and roadmap lines for the same leak.
- Plan it in the teaching plan (`## Puzzle`), because it shapes the outline: the topics are the
  steps to the answer.
- The roadmap still follows, in full.
- The conclusion answers it explicitly, in a `[reveal]` line. A puzzle that is never answered is
  a broken promise.

Mark the line `[puzzle]` (it can share a line with `hook`).

## 2. Ask the viewer to predict, then show

Before a reveal, ask the viewer to commit to an answer, give them time, then show it.

- Ask about something the viewer can reason toward with what they have learned so far. A
  prediction they can only guess at teaches nothing.
- Offer the choices when it helps: "Will each species tilt up, or down?"
- Give real thinking time: `{look:3}` or longer on the `[predict]` line. The checker requires at
  least two seconds.
- The storyboard keeps the answer off screen until the reveal. The scene that carries the
  question says what is withheld (`Withheld: species colors; dots stay gray`).
- The `[reveal]` comes later in the same topic, and says whether the obvious guess was right.
  When most viewers will guess wrong, say so without gloating: "If you said down, you're in good
  company. It's up."
- One or two predictions per video are usually enough; one per topic at most.

Asking people to commit to a prediction before they see an answer tends to improve how much they
remember, as well as holding attention. It works best when the reveal is explained, not just shown.

## 3. Reason out loud

Build the argument in front of the viewer instead of handing over conclusions.

- Use the shape: suppose, then what would follow, then check. "Suppose bigger birds simply have
  bigger bills in every direction. Then, within a species, longer bills should also be deeper.
  Let's check." Then show the data.
- Make the steps visible: each "then" in the narration is a step in the figure build.
- Show a wrong idea being ruled out when it helps, and say why it fails.
- Stay with the project's evidence: reasoning out loud is a way of explaining reported results,
  not a license to speculate about mechanisms the data cannot support.
- Every supposition must be one the data on screen can test, and stated in the data's own terms.
  "Suppose a bill grows in every direction at once; then a longer bill should also be deeper"
  is testable with two bill measurements. "Suppose bigger birds have bigger bills" brings in body
  size, which this figure does not show. After the test, say whether the supposition held.
- An explanation of why a pattern appears ("the pooled line tilts down because of where the
  species sit") is interpretation. Keep it to what the figures show, and list it under
  *Simplifications and analogies* in the evidence file.

## 4. Talk like a person

Write the way a knowledgeable person talks to one listener.

- Address the viewer as "you". Use "we" for things you and the viewer do together ("we split the
  data").
- Contractions: "it's", "doesn't", "you'll". Their absence is a strong sign of generated text.
- Vary sentence length. A short sentence after two longer ones lands.
- Plain words first. Use the technical term once the idea is in place, then stick to it.
- A little dry humor is welcome when it comes from the material ("The Gentoos, it turns out, are
  the heavyweights"). No jokes for their own sake, and no forced enthusiasm ("Amazing!").
- Never at the expense of accuracy: a vivid verb must not upgrade a claim ("Gentoos dominate"
  is not in the data).

## 5. Say plainly what isn't known

When the data cannot answer something the viewer will naturally wonder, say so in one plain
sentence, as a fact about the evidence.

- "Nobody in this study measured diet, so these data can't tell us why the bills differ."
- Use the `[unknown]` role, tagged with the gap claim it refers to (`{C12}`). This is the only
  role in which a gap claim may be spoken.
- This is not a hedge or a disclaimer. It names the specific missing evidence. "More research is
  needed" names nothing and stays banned.
- One per video is typical; place it where the question would arise, often in a wrap-up or the
  conclusion.

## Short videos

A puzzle, a roadmap, five roles per topic, and a prediction cost words. Under about three
minutes: let the puzzle share a line with the goal (`[puzzle+goal]`), use compressed roles, and
ask at most one prediction. If it still does not fit, cut content, not the roadmap or wrap-ups.

## Optional: explain before naming

Introduce the idea before its technical name, then name it ("This reversal has a name: Simpson's
paradox"). It helps when the name would intimidate or mislead. It is not required; for an expert
audience, naming first is often clearer.

## Toning it down

A formal research talk or a regulatory audience may call for fewer of these. Record the choice
in the teaching plan's Brief (`Engagement: reduced, because …`). Even then, keep the plain
statement of unknowns and the conversational register; drop the puzzle opening or predictions
first.
