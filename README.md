# fastapi sqlalchemy 사용 예제 - response model을 커스텀하기

>fastapi uvicorn[standard] sqlalchemy

- python main.py로 실행할 수 있도록 설정함.
- service, router, model, schema 등을 분리하여 작성함.
- sqlalchemy 2.0 권장방법으로 db 쿼리를 작성함.
- lifespan을 사용하여 앱 시작과 끝에 원하는 작업을 설정할 수 있도록 함