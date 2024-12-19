from flask import Flask, request, redirect, url_for, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Flask 앱 생성
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션 암호화 키

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/ticket_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 데이터베이스 초기화
db = SQLAlchemy(app)

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

# 티켓 모델 정의
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=True)

# 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()

# 로그인 페이지
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 사용자 검증
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('로그인 성공!', 'success')
            return redirect(url_for('index'))
        
        flash('아이디 또는 비밀번호가 올바르지 않습니다.', 'danger')
    
    return render_template('login.html')

# 회원가입 페이지
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 중복 확인
        if User.query.filter_by(username=username).first():
            flash('이미 존재하는 사용자입니다.', 'danger')
            return redirect(url_for('register'))

        # 새 사용자 추가
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        flash('회원가입 성공! 로그인해주세요.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('로그아웃 되었습니다.', 'info')
    return redirect(url_for('login'))

# 메인 페이지
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 티켓 등록
        try:
            data = request.form
            new_ticket = Ticket(
                title=data['title'],
                price=float(data['price']),
                date=datetime.strptime(data['date'], '%Y-%m-%d'),
                description=data.get('description', ''),
                category=data.get('category', '기타')  # 카테고리 필드
            )
            db.session.add(new_ticket)
            db.session.commit()
            print(f"[INFO] 티켓 등록 성공: {new_ticket.title}")
            return redirect(url_for('index'))  # 현재 페이지로 리다이렉트
        except Exception as e:
            print(f"[ERROR] 등록 오류: {str(e)}")

    # GET 요청 시 필터 및 검색 적용
    filters = request.args
    query = Ticket.query

    # 검색: 제목
    search_keyword = filters.get('search', '').strip()
    if search_keyword:
        query = query.filter(Ticket.title.ilike(f"%{search_keyword}%"))  # 대소문자 구분 없이 검색

    # 필터: 가격
    min_price = filters.get('min_price', type=float)
    max_price = filters.get('max_price', type=float)
    if min_price is not None:
        query = query.filter(Ticket.price >= min_price)
    if max_price is not None:
        query = query.filter(Ticket.price <= max_price)

    # 필터: 날짜
    date = filters.get('date')
    if date:
        query = query.filter(Ticket.date == datetime.strptime(date, '%Y-%m-%d').date())

    # 필터: 종류
    category = filters.get('category')
    if category and category != '전체':
        query = query.filter(Ticket.category == category)

    # 정렬
    tickets = query.order_by(Ticket.date).all()

    return render_template('mainpage.html', tickets=tickets)

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)
