from app.db.session import SessionLocal
from app.models.request_log import RequestLog

def log_request(operation: str, parameters: str, result: str):
    db = SessionLocal()
    try:
        log = RequestLog(
            operation=operation,
            parameters=parameters,
            result=result
        )
        db.add(log)
        db.commit()
    finally:
        db.close()
