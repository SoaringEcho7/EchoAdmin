from robyn import Response
import json
import logging

logger = logging.getLogger('app.utils')

def json_response(data, status_code=200):
    """
    创建一个JSON响应，并自动记录可读的日志
    """
    json_str = json.dumps(data, ensure_ascii=False)
    logger.debug(f"Response data: {json_str}")
    return Response(
        status_code=status_code,
        headers={"Content-Type": "application/json; charset=utf-8"},
        description=json_str
    )
