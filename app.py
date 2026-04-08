import streamlit as st
from langchain_groq import ChatGroq

# 🔹 LLM Setup
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.1-8b-instant",
    groq_api_key="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"
)

# 🔹 Function to calculate average
def calculate_average(marks):
    marks = list(map(int, marks.split()))
    return sum(marks) / len(marks)

# 🔹 UI Title
st.title("🎓 Student Performance Analyzer")

# 🔹 Inputs
name = st.text_input("Enter Student Name")
marks = st.text_input("Enter Marks (space separated)")

# 🔹 Button
if st.button("Analyze"):

    if name and marks:
        avg = calculate_average(marks)

        # Performance Logic
        if avg > 80:
            performance = "Excellent"
        elif avg >= 60:
            performance = "Good"
        else:
            performance = "Needs Improvement"

        # AI Suggestion
        prompt = f"""
        Student: {name}
        Average Marks: {avg}
        Performance: {performance}

        Give a short suggestion to improve performance.
        """

        response = llm.invoke(prompt)

        # 🔹 Output
        st.success("Analysis Complete ✅")
        st.write(f"**Name:** {name}")
        st.write(f"**Average:** {avg}")
        st.write(f"**Performance:** {performance}")
        st.write(f"**Suggestion:** {response.content}")

    else:
        st.warning("Please enter all details!")