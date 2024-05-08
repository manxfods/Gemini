import google.generativeai as genai

genai.configure(api_key="AIzaSyBQwjDQLQUgbGZRxsTac8qpn4MWzMut4AE")

# You can see the models avalible
#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

# Importing python program
with open('codes/test.py', 'r') as archive:
    code = archive.read()

# Model optimezed to text
model = genai.GenerativeModel('gemini-pro')

# Chose origin programming language
origin_lang = "Python"

# Chose target programming language
target_lang = "C#"

response = model.generate_content(f"Translate from {origin_lang} to {target_lang}: {code}")

print(response.text)