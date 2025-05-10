import cohere

# Initialize Cohere client
co = cohere.Client("39R6tqfDIiW73u01tcIlFzE0QRnI9Of4DZu26ZNm")  # Replace with your real key

# User input
query = "Plan my coming weekend filled with fun activities and Christmas-themed activities in Bangalore for 21 and 22 Dec 2024."

# Structured prompt
prompt = f"""
You are a weekend planning assistant that helps users create a personalized weekend itinerary.

Instructions:
- Mention the timeframe, location, and year (e.g., '21–22 December 2024 in Bangalore').
- Provide the response in three sections: Events, Activities, Dining Options.

1. **Events**: Include name, date, time, location, a short description, and booking links (e.g., from BookMyShow or Insider.in).
2. **Activities**: Recommend fun and Christmas-themed activities with estimated duration, location, and tips (e.g., best time to visit).
3. **Dining Options**: Suggest restaurants or cafés in Bangalore with cuisine type and links (e.g., Zomato or Google Maps).

Ensure that all recommendations are current or future-based and avoid outdated suggestions. If specific event data is unavailable, suggest evergreen attractions or seasonal activities typical in Bangalore during Christmas.

User Query:
{query}
"""

# Call Cohere chat model
response = co.chat(
    model="command-r",
    message=prompt,
    temperature=0.7,
    max_tokens=800
)

# Print the formatted itinerary
print("\nWeekend Plan:\n")
print(response.text.strip())
