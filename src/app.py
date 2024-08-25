from transformers import pipeline

def get_sentiment(prompt):
	classifier = pipeline("sentiment-analysis")
	res = classifier(prompt)
	return res

def get_generated(prompt):
	generator = pipeline("text-generation")
	res = generator(prompt)
	return res

def get_answer(prompt):
	answer = pipeline("question-answering")
	res = answer(prompt)
	return res

if __name__ == "__main__":
	classifier = pipeline("sentiment-analysis")
	res = classifier("I've been waiting for a HuggingFace course my whole life.")
	print(res)
