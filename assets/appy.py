from flask import Flask, render_template, request

app = Flask(__name__)

# ホームページ
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # POSTリクエストの処理（例えば、問い合わせフォームなど）
        pass
    return render_template('index.html')  # ホームページのテンプレートを表示

# グループホームの紹介ページ
@app.route('/about')
def about():
    return render_template('about.html')  # グループホーム紹介ページのテンプレートを表示

# 入居相談フォームページ
@app.route('/consultation', methods=['GET', 'POST'])
def consultation():
    if request.method == 'POST':
        # フォームデータを取得
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # ここでデータベースへの保存やメール送信などの処理を行う
        return 'ご相談を受け付けました。ご連絡ありがとうございます。'
    
    # GETリクエスト時にはフォームを表示
    return render_template('consultation.html')

# アプリケーションのエントリーポイント
if __name__ == '__main__':
    app.run(debug=True)
