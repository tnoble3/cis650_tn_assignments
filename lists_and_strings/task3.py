responses = [
"The product quality is excellent and delivery was fast",
"Terrible experience, very slow shipping and poor packaging",
"Great value for money, I am very happy with my purchase",
"The item arrived damaged, completely unacceptable service",
"Fast delivery and excellent customer support, highly recommend",
"Poor quality product, broke after one week, very disappointed",
"Amazing product, exceeded all my expectations",
"Shipping was slow but the product quality is good",
"Excellent quality and great packaging, will buy again",
"Very unhappy with the service, product was missing parts"
]

positive_keywords = ["excellent", "great", "fast", "happy",
"amazing", "good", "recommend"]
negative_keywords = ["terrible", "poor", "slow", "damaged",
"unacceptable", "disappointed", "unhappy"]

punctuation = ".,!?;:\"'"

positive_counts = [0]*len(positive_keywords)
negative_counts = [0] * len(negative_keywords)
total_positive = 0 
total_neutral = 0
total_negative = 0

for response in responses:
    lower_response = response.lower()
    words = lower_response.split()
    n_positive = 0
    n_negative = 0
    
    for word in words:
        cleaned_word = word.strip(punctuation)
        if cleaned_word in positive_keywords:
            index = positive_keywords.index(cleaned_word)
            positive_counts[index] = positive_counts[index] + 1
            n_positive = n_positive + 1
        if cleaned_word in negative_keywords:
            index = negative_keywords.index(cleaned_word)
            negative_counts[index] = negative_counts[index] + 1
            n_negative = n_negative + 1

    if n_positive > n_negative:
        total_positive = total_positive + 1
    elif n_positive < n_negative:
        total_negative = total_negative + 1
    else:
        total_neutral = total_neutral + 1

most_common_positive_index = 0
for i in range(len(positive_counts)):
    if positive_counts[i] > positive_counts[most_common_positive_index]:
        most_common_positive_index = i
most_common_negative_index = 0
for i in range(len(negative_counts)):
    if negative_counts[i] > negative_counts[most_common_negative_index]:
        most_common_negative_index = i

total_responses = len(responses)
positive_rate = (total_positive / total_responses) * 100

print("Survey Analysis Report")
print("-----------------------")
print("Total Responses : " + str(total_responses))
print("Positive : " + str(total_positive))
print("Negative : " + str(total_negative))
print("Neutral : " + str(total_neutral))
print("Positive Response Rate: " + str(positive_rate) + "%")
print("Keywords Found:")
print("Most Common Positive: " + positive_keywords[most_common_positive_index] + " (" + str(positive_counts[most_common_positive_index]) + ")")
print("Most Common Negative: " + negative_keywords[most_common_negative_index] + " (" + str(negative_counts[most_common_negative_index]) + ")")