from flask import Flask, render_template, request, redirect, url_for

# Инициализация приложения Flask
# Flask автоматически ищет шаблоны в папке 'templates' 
# и статические файлы в папке 'static'.
app = Flask(__name__)

# --- Настройка путей для отображения страниц (Роуты) ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/collections')
def collections():
    return render_template('collections.html')

# --- Обработка формы контактов ---

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Сбор данных из формы
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # !!! ЛОГИКА СЕРВЕРА !!!
        # Здесь в реальном проекте вы бы отправляли email или сохраняли данные в БД.
        print("\n--- NEW CONTACT SUBMISSION ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        print("------------------------------\n")
        
        # Перенаправление с параметром success=True для отображения уведомления
        return redirect(url_for('contact', success=True))
    
    # Отображение страницы контактов (GET запрос)
    return render_template('contact.html')

# --- Запуск приложения ---
if __name__ == '__main__':
    # Включаем режим отладки для удобства разработки
    app.run(debug=True)