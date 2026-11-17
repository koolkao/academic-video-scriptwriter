# Script: Longer bills, shallower bills?

## Opening

[S01] [puzzle] Here's something odd. Across three hundred and forty two penguins, birds with longer bills tend to have shallower bills. That seems backwards. Shouldn't a bigger bill be bigger every way? {C01} {C02} {beat}
[S01] [goal] By the end, you'll be able to read the figures that answer that, and you'll see what the pooled trend is really telling us.
[S01] [roadmap] We'll go step by step: reading a contour plot, the pooled trend, splitting by species, species profiles, and every pair of measurements. {break}

## T1 · Reading a contour plot

[S02] [announce] First: reading a contour plot.
[S02] [introduce] You've probably read one already, on a hiking map. The rings there are height lines. Here they work the same way, except they count birds instead of meters.
[S03] [explain] Across the bottom is bill length, in millimeters. Up the side is bill depth: how tall the bill is where it meets the head. {look:2}
[S03] [explain] This one ring joins every spot where birds are equally common. {beat}
[S03] [explain] Now all the rings. Where they bunch up into a peak, lots of birds share those measurements.
[S04] [wrap-up] So a contour plot doesn't show single birds. It shows where birds are common. A peak is a crowd, not a hill. {look:2}
[S04] [bridge] Now that you can read the map, let's see what it says about bills. {break}

## T2 · The pooled trend

[S05] [announce+introduce] Next: the pooled trend. Pooled means we throw all three species together and treat them as one population. {C01}
[S06] [explain] Follow the rings from left to right. As bills get longer, they sit lower. Longer, but shallower. {look:2}
[S06] [explain] The correlation is minus point two four, across three hundred and forty two birds. That's weak, but it's clearly negative. {C02} {beat}
[S07] [wrap-up] Taken together, the penguins say: longer bill, shallower bill. {look:2}
[S07] [bridge] But that's a statement about the mixture. To see what the mixture is made of, we have to split it apart. {break}

## T3 · Splitting by species

[S08] [announce+introduce] Splitting by species. Same axes, same birds. Only now, each species is about to get its own color.
[S08] [explain] Think about it for a second. Suppose a bill simply grows in every direction at once. Then inside one species, a longer bill should also be a deeper bill.
[S08] [predict] So here's the question. When each species gets its own color, will each group tilt up, or tilt down, like the whole cloud? {look:4}
[S09] [reveal] Here they are. The single landscape breaks into three islands. Adelie penguins sit at the upper left, with short, deep bills. {C11}
[S09] [explain] Chinstraps sit at the upper right, long and deep. Gentoos sit at the lower right, long and shallow. {C11} {look:2}
[S10] [reveal] Now trace each island on its own. Every one of them tilts *up*. If you guessed up, your reasoning held. {look:2}
[S10] [explain] Within Adelies, the correlation is point three nine. Within Chinstraps, point six five. Within Gentoos, point six four. {C03} {C04} {C05} {beat}
[S11] [wrap-up] Inside *every* species, longer bills are deeper bills. The downward trend came from where the islands sit, not from inside any of them. This flip has a name: Simpson's paradox. {beat}
[S11] [bridge] So why do the islands sit where they do? Because the species differ in more than their bills. {break}

## T4 · Species profiles

[S12] [announce+introduce] Species profiles. To see all the measurements at once, we'll use a radar plot.
[S12] [explain] Each spoke is one measurement: bill length, bill depth, flipper length, and body mass. The middle ring is the average penguin. Further out means above average; further in means below. {look:3}
[S12] [explain] Every spoke is measured in standard deviations, so they all share one scale.
[S13] [explain] Here's the Gentoo. Its bill depth falls about one standard deviation below average, while its flippers and body mass reach well above. {C08} {beat}
[S13] [explain] Adelies are small birds with short but deep bills. Chinstraps have long, deep bills on smaller than average bodies. {C06} {C07} {look:2}
[S14] [wrap-up] Gentoos are big birds with long, shallow bills. Put them next to short, deep Adelie bills, and you get the downward pooled trend. {look:2}
[S14] [bridge] Bills are just one pair of measurements. If pooling can flip one pair, it could flip others, so let's check them all. {break}

## T5 · Every pair of measurements

[S15] [announce+introduce] Every pair of measurements. A heat map puts every correlation among the measurements into one grid.
[S15] [explain] Each cell is one pair. Warm cells are positive, cool cells are negative, and pale cells are near zero. {look:2}
[S16] [explain] Start with one cell: flipper length against body mass, all birds pooled. Point eight seven, strongly positive. {C09} {beat}
[S16] [explain] Now run along the bill depth row. Pooled, bill depth runs negative against every other measurement. {C09} {look:2}
[S16] [predict] You've seen this trick once already. When we keep only the Gentoos, what will that cool row do? {look:4}
[S17] [reveal] Here's the Gentoo grid. Every cell turns warm, from point six four to point seven two. The cool row is gone. {C10} {look:3}
[S17] [wrap-up] Inside one species, deeper bills go with longer bills, longer flippers, and heavier bodies. Only the pooled grid says otherwise. {C10}
[S17] [bridge] That's the last piece, so let's go back to where we started. {break}

## Conclusion

[S18] [synthesis] We learned to read a contour plot, and found a pooled trend: longer bills, shallower bills. Splitting by species flipped it inside every group. {C02} {C03} {C04} {C05}
[S18] [synthesis] The species profiles showed why: Gentoos pair long bills with shallow ones. And the heat map showed the same flip for bill depth within Gentoos. {C08} {C10} {beat}
[S18] [reveal] So yes: inside each species, longer bills do tend to be deeper. The pooled trend isn't wrong, though. {C03} {C04} {C05} It describes the mixture of species. The within-species trend describes how bill length and depth go together in one kind of penguin.
[S18] [unknown] What these data can't tell us is why the species' bills differ. Nobody in this study measured diet. {C12}
[S18] [synthesis] All of it comes from one archipelago, over three seasons, from two thousand seven to two thousand nine. {C01} {look:3}
