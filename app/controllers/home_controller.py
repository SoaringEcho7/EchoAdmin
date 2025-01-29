from pathlib import Path
from robyn.robyn import Response, Request

# 获取模板目录路径
TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

async def index(request: Request) -> Response:
    """首页路由处理"""
    with open(TEMPLATE_DIR / "index.html", "r", encoding="utf-8") as f:
        content = f.read()
    return Response(
        status_code=200,
        headers={"Content-Type": "text/html; charset=utf-8"},
        description=content
    )
