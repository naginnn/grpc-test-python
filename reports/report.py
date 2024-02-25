import io
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

import dateutil.parser
import pandas as pd
from sqlalchemy import select
from sqlalchemy.sql.expression import func
from models.accounts import Account
from settings.db import get_sync_session, sync_db


class ReportAbstract(ABC):
    session = get_sync_session()

    def __init__(self, param: str = None,
                 start: int = None,
                 end: int = None):
        self.param = param
        self.start = datetime.fromtimestamp(start) if start else None
        self.end = datetime.fromtimestamp(end) if end else None

    @abstractmethod
    def get_report(self):
        pass


class ClusterConfig(ReportAbstract):
    def get_report(self):
        # query = select(func.max(Account.created_at))
        query = (select(Account).filter(Account.created_at <= self.end))
                 # .filter(Account.created_at >= self.start))
        # accounts = self.session.execute(query).scalars().all()
        df = pd.read_sql(query, sync_db)
        excel_bytes = io.BytesIO()
        df.to_excel(excel_bytes)
        excel_bytes.seek(0)
        b = excel_bytes.read()
        # super().get_report()
        return b


if __name__ == '__main__':
    s = ClusterConfig(
        end=dateutil.parser.parse("2024-02-24").timestamp()
    )
    s.get_report()
