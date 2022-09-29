from feel_it import SentimentClassifier, EmotionClassifier

sentimento = SentimentClassifier()
emozioni = EmotionClassifier()

#emozioni.predict(["cazzo", "ti amo", "vita mia", "diocane"])
#sentimento.predict(["cazzo", "ti amo", "vita mia", "diocane"])
print("cazzo", "ti amo", "vita mia", "Uomo nero")
print(emozioni.predict(["cazzo", "ti amo", "vita mia", "Uomo nero"]))
print(sentimento.predict(["cazzo", "ti amo", "vita mia", "Uomo nero"]))

