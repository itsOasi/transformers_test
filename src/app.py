from transformers import pipeline

def get_sentiment(text):
	classifier = pipeline("sentiment-analysis")
	res = classifier(text)
	return res

if __name__ == "__main__":
	classifier = pipeline("sentiment-analysis")
	res = classifier("I've been waiting for a HuggingFace course my whole life.")

	print(res)
