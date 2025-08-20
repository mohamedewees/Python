import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from transformers import pipeline
import warnings



warnings.filterwarnings("ignore", category=DeprecationWarning)
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ar-en")
arabic_text="وفقًا للقانون رقم ١٢ لسنة ٢٠٠٣، يلتزم صاحب العمل بتوفير بيئة عمل آمنة"
prompt = f"ترجم النص التالي إلى الإنجليزية بصيغة قانونية دقيقة دون تغيير الأرقام أو التواريخ {arabic_text}"


translated = translator(prompt)[0]['translation_text']

print(translated)
# print(translator(prompt,max_length=512))
