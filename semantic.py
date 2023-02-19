import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Similarities seem to be forged not just out of categories but perceived relationships
# between individual items in different categories.  It's very similar to comparing
# something like cow, pig and milk, where there are two obvious connections that take 
# different approaches (cow and pig as farmyard animals, cow and milk as one being the
# product of the other, and maybe a relationship between pig and milk through the concept 
# of the farm).

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)

# Running sm vs md: sm is a smaller model which does not have word vectors - 
# as a result, similarity judgements are based on different aspects which 
# are not as useful as they are context sensitive.  The sm model does run 
# faster as it is a much smaller model than md. 