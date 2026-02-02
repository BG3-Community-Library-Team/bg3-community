---
title: Considering Performance
description: 
published: true
date: 2026-02-02T19:14:35.473Z
tags: osiris
editor: markdown
dateCreated: 2026-02-02T19:14:35.473Z
---

Osiris is a very efficient scripting language and we can do quite a lot with it without impacting the game's performance. However, there are already an enormous number of scripts running all at once, and so it's good to be mindful of the impact our additions could have.

## Number of Evaluations

Perhaps the most important consideration for writing efficient rules is limiting how many times it has to be evaluated. For example, consider the following rule that does something if Wyll and Karlach are both members of the party:

```
IF
DB_Players(_First)
AND
DB_Players(_Second)
AND
_First == S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d
AND
_Second == S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c
THEN
Action1;
```

Any time a new player character joins the party, the rule will be triggered for evaluation by the database conditions. Also, because we're combining a database with itself before filtering the results, the number of times this rule has to be evaluated is the size of `DB_Players` multiplied by itself. This is very inefficient.

We can clearly see the exponential growth in the number of times this rule is evaluated with a diagram, where both database conditions create a new version of the rule for every character in `DB_Players`. Assuming a full party of four characters, we end up with this:

![osirisrules_efficiency_worst.webp](/tutorials/osiris/understanding-osiris-rules/osirisrules_efficiency_worst.webp)

However, we can easily improve this by changing the order of the conditions:

```
IF
DB_Players(_First)
AND
_First == S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d
AND
DB_Players(_Second)
AND
_Second == S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c
THEN
Action1;
```

Again, the rule will be triggered for evaluation every time a new player joins the party. However, this time the rule only has to be evaluated once for each fact in `DB_Players` before it reaches a condition that requires Wyll's GUID to be assigned to `_First`. If it's not, then the rule stops evaluating. This means that at most only one version of the rule (where `_First` equals Wyll's GUID) will reach the second undeclared variable that creates multiple versions of the rule again for every fact in `DB_Players`.

This still isn't ideal, but at least the number of evaluations no longer grows exponentially, as we can see in the following diagram:

![osirisrules_efficiency_better.webp](/tutorials/osiris/understanding-osiris-rules/osirisrules_efficiency_better.webp)

We can do even better with this improvement:

```
IF
DB_Players(S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d)
AND
DB_Players(S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c)
THEN
Action1;
```

Because we only care about Wyll and Karlach specifically, we can just hard-code their GUIDs. This means the database conditions will _only ever_ trigger the rule for evaluation if one of them joins the party, and the rule will immediately stop evaluating if the other one isn't also present. Plus, there is only one version of the rule to evaluate. This is incredibly efficient in both regards.

![osirisrules_efficiency_most.webp](/tutorials/osiris/understanding-osiris-rules/osirisrules_efficiency_most.webp)

## Other

Feel free to expand this to include other considerations.