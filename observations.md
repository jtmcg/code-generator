I don't know if my prompts are different enough each time to yield very different results. I think there are a few approaches I could take to highlight the differences in each iteration to make the prompts more likely to return something different:
- Feed the model diffs so it knows what changed since the last time the code was added
- Create new prompts for successful iterations towards a functional answer. For example, when a new test passes, the prompt can say "this is closer than it was before" or something similar. When it degrades, the prompt can say "this is worse than it was before" and direct the model back to whatever the last, most successful attempt was.