class TextAnalyzer():
    def __init__(self, raw_text='', stop_words='', output_file='entregable.txt'):
        
        with open(raw_text, 'r', encoding='utf-8') as file:
            raw_text = file.read()

        self.formato1 = raw_text.lower()
        
        self.formato2 = self.formato1.replace("(", "").replace(")", "").replace(",", "").replace(".", "").replace("\n", "")
  
        import re
        self.formato3 = re.sub(r'\d', '', self.formato2)

        self.fmttext = self.formato3
        
        self.formato4 = self.fmttext.split()

        with open(stop_words, 'r', encoding='utf-8') as file:
            stopwords = set(file.read().splitlines())

        self.formato5 = [word for word in self.formato4 if word not in stopwords]

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(" ".join(self.formato5))


analyzed = TextAnalyzer('raw-text.txt', 'stop-words.txt', 'entregable.txt')

print("1. En minusculas:")
print(analyzed.formato1)
print()
print("2. Sin saltos y caracteres:")
print(analyzed.formato2)
print()
print("3. sin digitos")
print(analyzed.formato3)
print()
print("4. Tokenizado")
print(analyzed.formato4)
print()
print("5. sin stopwords")
print(analyzed.formato5)

