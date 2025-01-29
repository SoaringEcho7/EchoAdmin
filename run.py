from app import app
import logging

# 配置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting server...")
    app.start(host="127.0.0.1", port=8000)
