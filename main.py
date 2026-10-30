from flask import Flask, render_template
import os

app = Flask(__name__)

# 1. اكتب هنا منتجاتك وأسعارها (تقدر تزود أو تعدل براحتك)

PRODUCTS = [
    {
        "name": "المنتج الأول (اكتب اسمه هنا)",
        "price": "500 جنيه",
        "description": "اكتب هنا وصف قصير ومميز لمنتجك عشان العميل يتشجع يشتريه."
    },
    {
        "name": "المنتج الثاني (مثال: عباية سوداء شيك)",
        "price": "1200 جنيه",
        "description": "خامات ممتازة وتقفيل عالي الجودة متوفر بجميع المقاسات."
    }
]

# 2. اكتب رقم تليفونك بالصيغة الدولية (لمصر ابدأ بـ 20 ثم رقمك بدون أصفار في الأول)
# مثال لو رقمك 01012345678 اكتبه كدة: 201012345678
MY_PHONE_NUMBER = "201000000000"

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS, phone=MY_PHONE_NUMBER)

if __name__ == '__main__':
    # السطر ده عشان يشتغل محلياً وعلى الإنترنت
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)