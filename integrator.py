import bot2 as cb
conversation_context = ""
question = "What is naturopathy?"
response = cb.get_response_from_bot(question)
conversation_context += f"Question: {question}\nAnswer: {response}\n"
cb.store_context(conversation_context)
print(response)