from robyn import Robyn
from pathlib import Path
import logging
from app.controllers.dashboard_controller import router as dashboard_router

# 配置日志格式和级别
logging.basicConfig(
    level=logging.INFO,  # 将默认级别设为 INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 单独设置 Robyn 相关日志级别
logging.getLogger('robyn').setLevel(logging.WARNING)  # 将 Robyn 的日志级别设为 WARNING

# 保持应用自身的日志级别为 DEBUG
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

# 获取应用根目录
ROOT_DIR = Path(__file__).parent
logger.debug(f"Root directory: {ROOT_DIR}")

app = Robyn(__file__)

# 注册静态文件目录
STATIC_DIR = ROOT_DIR / "static"
logger.debug(f"Static directory: {STATIC_DIR}")
app.serve_directory("/static", str(STATIC_DIR))

# 注册模板目录
TEMPLATE_DIR = ROOT_DIR / "templates"
logger.debug(f"Template directory: {TEMPLATE_DIR}")
app.serve_directory("/templates", str(TEMPLATE_DIR))

# 注册仪表盘路由
app.include_router(dashboard_router)
