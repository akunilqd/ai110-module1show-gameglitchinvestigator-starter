# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked playable but it was not working correctly at all.

- List at least two concrete bugs you noticed at the start  
  + The hints were backwards
  + The score was negative and not reset when pressing the new game button
  + The difficulty ranges were not matched correctly

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guessed "25" | "Go Higher" hint | "Go Lower" hint | None |
|Start a new game after winning | The guess button should work | The guess button did not work | None |
|Finish the game | Positive score | Negative score | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project? Claude.

- Give one example of an AI suggestion that was correct.
The hint fix (it is kind of obvious once Claude pointed it out, and feel more comfortable when playing the game again).
'''
The hint messages in check_guess were swapped:

# buggy
if guess > secret:
    return "Too High", "📈 Go HIGHER!"   # wrong — should say Go LOWER
else:
    return "Too Low", "📉 Go LOWER!"    # wrong — should say Go HIGHER

If your guess is bigger than the secret, you went too high — so the hint should tell you to go lower, not higher. The messages were just on the wrong branches. The fix was swapping them:

# fixed
if guess > secret:
    return "Too High", "📉 Go LOWER!"
else:
    return "Too Low", "📈 Go HIGHER!"

- Give one example of an AI suggestion you did not accept as written.
Removing the "+1" from the score formula: Claude said that would fix the negative score but it did not really fixed it. So I asked it to add a floor base to the score instead.
'''
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the game manually and played it to see if the behavior actually changed.

- Describe at least one test you ran and what it showed you.
Running pytest with all 11 tests passing showed the functions were handling edge cases like empty input, None, floats, and mixed strings.

- Did AI help you design or understand any tests? How?
Yes, Claude explained to me what each test does, what is special about it, and what each function is expected to return.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend?
Streamlit reruns the whole script every time you click anything, so regular variables reset every click. session_state is like a notepad that saves values across reruns so they do not get wiped.

---

## 5. Looking ahead: your developer habits

- What is one habit you want to reuse in future projects? Always run the app manually after a fix, not just assume the code looks right.
- What is one thing you would do differently next time?  Verify each fix one at a time so I know exactly what worked and what did not.
- How did this project change the way you think about AI-generated code? I used to think it was probably fine, but now I know I still need to test it and question it before trusting it.
