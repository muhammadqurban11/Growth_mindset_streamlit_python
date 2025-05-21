import streamlit as st
import random
import datetime

# Growth mindset questions & scores


questions = [
    ("How do you handle failure?", ["See it as a learning experience", "Feel discouraged"]),
    ("Do you believe intelligence can grow?", ["Yes, through effort", "No, it's fixed"]),
    ("How do you respond to feedback?", ["Use it to improve", "Ignore or take it personally"]),
]

# Store user responses
def calculate_mindset_score(answers):
    return answers.count(0)  # Count growth-oriented answers

st.title("🌱 Growth Mindset Coach")
st.subheader("Discover and strengthen your growth mindset!")

# Growth Quiz
st.write("🧠 Take this quick quiz to check your mindset!")
answers = []
for question, options in questions:
    choice = st.radio(question, options, index=0, key=question)
    answers.append(options.index(choice))

# Show results
if st.button("Check My Mindset Score"):
    score = calculate_mindset_score(answers)
    st.success(f"Your Growth Mindset Score: {score}/{len(questions)}")
    if score == len(questions):
        st.balloons()
        st.write("🚀 You have a strong growth mindset! Keep growing.")
    else:
        st.write("💡 There’s always room for growth! Try new challenges.")

# AI-Powered Coaching
st.subheader("🤖 Need Mindset Advice?")
user_challenge = st.text_input("Describe a challenge you're facing:")
if st.button("Get Growth Advice"):
    advice_list = [
        "Every failure is a step closer to success. Keep learning!",
        "Embrace feedback—it’s the key to improvement.",
        "Success comes from effort and persistence. Keep going!",
    ]
    st.write(random.choice(advice_list))

# Journal for Reflections



st.subheader("📖 Growth Journal")
user_entry = st.text_area("Write about a recent experience that helped you grow:")
if st.button("Save Entry"):
    today = datetime.date.today()
    st.write(f"✅ Entry saved for {today}: {user_entry}")

st.write("💡 Keep logging your reflections daily to see your growth over time!")
