# -*- coding: utf-8 -*-
"""
    photolog.database
    ~~~~~~~~~~~~~~~~~

    DB 연결 및 쿼리 사용을 위한 공통 모듈.
    SQLAlchemy 공통 적용 모듈
    :copyright: (c) 2013 by 4mba.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBManager:
	"""데이터베이스 처리를 담당하는 공통 클래스"""

	__engine = None
	__session = None

	@staticmethod
	def init (db_url, db_log_flag=True):
		'''
        DB에 접속하기 위해 Engine객체를 얻는다.
        Args:
            db_url: 연결할 db의 위치
            db_log_flag: db로그 기록 여부 from config

        Returns:

        '''
		DBManager.__engine = create_engine(db_url, echo=db_log_flag)
		# 연결된 DB객체를 다루기 위한 세션 객체를 얻는다.
		# sessionmaker 클래스를 이용해 세션을 생성할 전역 세션 팩토리 객체를 얻고, 실제 DB에 작업을 요청할 때 이 세션 팩토리를 이용해 세션을 생성한다.
		DBManager.__session = scoped_session(sessionmaker(autocommit=False,
		                                                  autoflush=False,
		                                                  bind=DBManager.__engine))

		global dao
		dao = DBManager.__session

	@staticmethod
	def init_db ():
		from photolog.model import *
		from photolog.model import Base
		Base.metadata.create_all(bind=DBManager.__engine)


dao = None
