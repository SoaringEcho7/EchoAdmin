from robyn import SubRouter, Response
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
import logging
from ..utils import json_response

# 配置日志
logger = logging.getLogger('app.controllers.dashboard')

router = SubRouter(__file__)
TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

@router.get("/")
async def index(request):
    try:
        template_path = TEMPLATE_DIR / "index.html"
        logger.debug(f"Template path: {template_path}")
        logger.debug(f"Template exists: {template_path.exists()}")
        
        if not template_path.exists():
            logger.error(f"Template file not found: {template_path}")
            return Response(
                status_code=404,
                headers={"Content-Type": "text/plain"},
                description="Template not found"
            )
            
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
            logger.debug(f"Template content length: {len(content)}")
            
        return Response(
            status_code=200,
            headers={"Content-Type": "text/html; charset=utf-8"},
            description=content
        )
    except Exception as e:
        logger.error(f"Error in index route: {str(e)}", exc_info=True)
        return Response(
            status_code=500,
            headers={"Content-Type": "text/plain"},
            description=f"Internal Server Error: {str(e)}"
        )

@router.get("/api/prefetch")
async def get_prefetch(request):
    data = {"message": "数据已预加载"}
    return json_response({"value": data['message']})

@router.get("/api/webtitle")
async def get_webtitle(request):
    data = {"message": "EchoAdmin"}
    return json_response({"value": data['message']})

@router.get("/api/stats/visits")
async def get_visits(request):
    return Response(
        status_code=200,
        headers={"Content-Type": "application/json"},
        description=json.dumps({"value": random.randint(1000, 5000)})
    )

@router.get("/api/stats/sales")
async def get_sales(request):
    return Response(
        status_code=200,
        headers={"Content-Type": "application/json"},
        description=json.dumps({"value": random.randint(10000, 50000)})
    )

@router.get("/api/stats/orders")
async def get_orders(request):
    return Response(
        status_code=200,
        headers={"Content-Type": "application/json"},
        description=json.dumps({"value": random.randint(100, 1000)})
    )

@router.get("/api/stats/conversion")
async def get_conversion(request):
    return Response(
        status_code=200,
        headers={"Content-Type": "application/json"},
        description=json.dumps({"value": f"{random.uniform(1, 5):.1f}%"})
    )

@router.get("/api/stats/trend")
async def get_trend(request):
    try:
        days = 30
        data = []
        start_date = datetime.now() - timedelta(days=days)
        
        for i in range(days):
            current_date = start_date + timedelta(days=i)
            data.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "value": random.randint(1000, 5000)
            })
        
        return Response(
            status_code=200,
            headers={"Content-Type": "application/json"},
            description=json.dumps({"data": data})
        )
    except Exception as e:
        logger.error(f"Error in get_trend route: {str(e)}", exc_info=True)
        return Response(
            status_code=500,
            headers={"Content-Type": "text/plain"},
            description=f"Internal Server Error: {str(e)}"
        )

@router.get("/api/stats/sources")
async def get_sources(request):
    try:
        sources = [
            {"name": "搜索引擎", "value": random.randint(800, 1200)},
            {"name": "直接访问", "value": random.randint(600, 900)},
            {"name": "邮件营销", "value": random.randint(400, 700)},
            {"name": "社交媒体", "value": random.randint(300, 600)},
            {"name": "其他", "value": random.randint(200, 400)}
        ]
        return Response(
            status_code=200,
            headers={"Content-Type": "application/json"},
            description=json.dumps({"data": sources})
        )
    except Exception as e:
        logger.error(f"Error in get_sources route: {str(e)}", exc_info=True)
        return Response(
            status_code=500,
            headers={"Content-Type": "text/plain"},
            description=f"Internal Server Error: {str(e)}"
        )
