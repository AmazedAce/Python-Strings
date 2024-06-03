# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:07:50 2024

@author: Loren
"""

# 1. Product Review Analysis

# reviews = [
#     "This product is really good. I'm impressed with its quality.",
#     "The performance of this product is excellent. Highly recommended!",
#     "I had a bad experience with this product. It didn't meet my expectations.",
#     "Poor quality product. Wouldn't recommend it to anyone.",
#     "The product was average. Nothing extraordinary about it."
# ]

# keywords = ["good", "excellent", "bad", "poor", "average"]

# def highlight_keywords(review, keywords):
#     for keyword in keywords:
#         review = review.replace(keyword, keyword.upper())
#     return review

# for review in reviews:
#     highlighted_review = highlight_keywords(review, keywords)
#     print(highlighted_review)
    
    
# Task 2:
    
    
    
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# def tally_sentiment(review, positive_words, negative_words):
#     positive_count = sum(review.count(word) for word in positive_words)
#     negative_count = sum(review.count(word) for word in negative_words)
#     return positive_count, negative_count

# for review in reviews:
#     positive_count, negative_count = tally_sentiment(review, positive_words, negative_words)
#     print(f"Review: {review}")
#     print(f"Positive words: {positive_count}, Negative words: {negative_count}\n
          
# Task 3: 


# def create_summary(review, length=30):
#     if len(review) <= length:
#         return review
#     else:
#         end = review[:length].rfind(' ')
#         return review[:end] + "…"

# for review in reviews:
#     summary = create_summary(review)
#     print(f"Summary: {summary}")



# 2. User Input Data Processor

# def validate_name_length(first_name, last_name):
#     if len(first_name) < 2:
#         print("First name must be at least 2 characters long.")
#     if len(last_name) < 2:
#         print("Last name must be at least 2 characters long.")

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# validate_name_length(first_name, last_name)

# Task 2:
    
    
# import re

# def check_password_complexity(password):
#     if len(password) < 8:
#         print("Password must be at least 8 characters long.")
#     elif not re.search(r'[A-Z]', password):
#         print("Password must contain at least one uppercase letter.")
#     elif not re.search(r'[a-z]', password):
#         print("Password must contain at least one lowercase letter.")
#     elif not re.search(r'[0-9]', password):
#         print("Password must contain at least one number.")
#     else:
#         print("Password is valid.")

# password = input("Enter your password: ")
# check_password_complexity(password)

# Task 3: 
    
# def format_email(email):
#     return email.lower().strip()

# email = input("Enter your email address: ")
# formatted_email = format_email(email)
# print(f"Formatted Email: {formatted_email}")