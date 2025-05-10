import cohere

# Initialize Cohere client
co = cohere.Client("39R6tqfDIiW73u01tcIlFzE0QRnI9Of4DZu26ZNm")  # Replace with your real key

# User input
preferences = """I am looking for running shoes with the following preferences:
Color: Black
Purpose: Comfortable for long-distance running
Budget: Under Rs. 10,000"""

# Define the prompt
prompt = f"""
You are a product recommender AI. Based on the following user preferences, suggest 2–3 real product options from trusted Indian e-commerce sites like Amazon, Flipkart, Myntra, or Nike. 
Only suggest products that are likely to be in stock and from verified brands. Clearly mention product name, price, brand, and what makes it suitable.

User Preferences:
{preferences}
"""

# Use the chat API with command-r
response = co.chat(
    model="command-r",
    message=prompt,
    temperature=0.7,
    max_tokens=500
)

# Display the result
print("\nProduct Recommendations:\n")
print(response.text.strip())
