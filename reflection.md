# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it did not really work. The hints were backwards, the score went negative, and the guess button stopped working after I won. The difficulty ranges were also not matched correctly, so Hard was actually easier than Normal.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed "25" when secret was higher | "Go Higher" hint | "Go Lower" hint | None |
| Start a new game after winning | The guess button should work | The guess button did not work | None |
| Finish the game | Positive score | Negative score | None |

---

## 2. How did you use AI as a teammate?

I used Claude for this project. The hint fix was correct and it is kind of obvious once Claude pointed it out, and feel more comfortable when playing the game again. One suggestion I did not accept as written was removing the `+1` from the score formula — Claude said that would fix the negative score but it did not really fixed it. So I asked it to add a floor base to the score instead, which actually worked.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed by running the game and testing it manually. Just looking at the code was not enough, I had to actually play it and see if the behavior changed. Claude explained to me what each test does, what is special about it, and what each function is expected to return. Running pytest and seeing all 11 tests pass showed me the functions were handling more than just the normal cases.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the whole script every time you click anything, so regular variables just reset every click. That is why the secret number kept changing in the broken game. `session_state` is like a notepad that saves values across reruns so they do not get wiped. The `if "secret" not in st.session_state` pattern makes sure you only set the value once and leave it alone after.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is always running the app manually after fixing something, not just assuming the code looks right. Next time I would also verify each fix one at a time so I know exactly what worked and what did not. This project changed the way I think about AI-generated code — I used to think it was probably fine, but now I know I still need to test it and question it before trusting it.
