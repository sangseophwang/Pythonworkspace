import os

from flask import Flask


def create_app(test_config=None):
    # 웹 애플리케이션을 만들고 설정합니다.

    # Flask 인스턴스를 만듭니다.
    app = Flask(__name__, instance_relative_config=True)
    # __name__은 현재 python 모듈의 이름입니다.
    # Flask 앱은 일부 경로를 설정하기 위해 위치를 알아야하며,
    # __name__을 통해 알려주는 방법은 아주 편리한 방법입니다.

    # instance_relative_config=True 코드는 구성 파일이 인스턴스 폴더에
    # 상대적인 위치를 가지고 있다고 앱에 알리는 역할을 합니다.
    # 인스턴스 폴더는 elice_flask_board 폴더 외부에 있으며 애플리케이션의 보안을 위해 데이터베이스와 같이
    # 원격 저장소(Git)에 파일이 커밋되지 않아야하는 로컬 데이터를 저장할 수 있습니다.

    # Flask 웹 애플리케이션에서 사용할 키와 데이터베이스를 설정합니다.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'elice_flask_board.sqlite'),
    )
    # SECRET_KEY='dev' 현재 개발 중이라는 표시입니다.
    # 나중에 배포시 임의의 값으로 수정되어야 합니다.
    # DATABASE는 SQLITE3를 사용합니다.

    if test_config is None:
        # 테스트를 실행하지 않을 때, 인스턴스의 설정을 불러옵니다.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 테스트를 실행했을 때
        app.config.from_mapping(test_config)

    # 인스턴스 폴더가 있는지 확인합니다. 없다면 에러가 발생합니다.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, Elice!'

    # 데이터베이스를 불러옵니다.
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import board
    app.register_blueprint(board.bp)
    app.add_url_rule('/', endpoint='index')

    return app
