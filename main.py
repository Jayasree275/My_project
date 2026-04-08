from langchain_groq import ChatGroq

# 🔹 Step 1: LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.1-8b-instant",
    groq_api_key="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"
)

# 🔹 Step 2: Function (Tool logic manually)
def calculate_average(marks):
    marks = list(map(int, marks.split()))
    return sum(marks) / len(marks)

# 🔹 Step 3: Input
name = input("Enter student name: ")
marks = input("Enter marks (space separated): ")

# 🔹 Step 4: Calculate average
avg = calculate_average(marks)

# 🔹 Step 5: Performance logic (Python handles it)
if avg > 80:
    performance = "Excellent"
elif avg >= 60:
    performance = "Good"
else:
    performance = "Needs Improvement"

# 🔹 Step 6: Ask AI for suggestion only
prompt = f"""
Student: {name}
Average Marks: {avg}
Performance: {performance}

Give a short suggestion to improve performance.
"""

response = llm.invoke(prompt)

# 🔹 Step 7: Output
print("\n🎯 Final Result:\n")
print(f"Name: {name}")
print(f"Average: {avg}")
print(f"Performance: {performance}")
print(f"Suggestion: {response.content}")