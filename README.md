# 기초데이터베이스 개인프로젝트 과제


실험 방법 :
1. 디렉토리에 clone한다
2. cmd를 관리자권한으로 열어서 포트 3306을 차지하고 있는 프로세스를 죽인다
3. clone한 디렉토리에서 다음의 코드를 실행한다 (docker가 깔려있어야 한다)
<pre>
<code>
docker-compose build
docker-compose up
</code>
</pre>
4. http://127.0.0.1:5000 로 접속한다

wait-for-it.sh 출처:
https://github.com/vishnubob/wait-for-it/blob/master/wait-for-it.sh
