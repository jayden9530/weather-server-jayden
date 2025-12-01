from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# 1. 서버 이름표 붙이기
mcp = FastMCP("weather")

# 2. 도구(Tool) 만들기
@mcp.tool()
async def get_weather_custom(latitude: float, longitude: float) -> str:
    """
    특정 위치(위도, 경도)의 날씨 예보를 반환합니다.
    
    Args:
        latitude: 위도 (예: 37.56)
        longitude: 경도 (예: 126.97)
    """
    # 오픈소스 날씨 API 주소 (별도의 키 발급 없이 사용 가능)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
    
    # 비동기(Async) 방식으로 웹사이트에 접속하여 데이터 가져오기
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    return str(data)

# 3. 서버 실행 (엔트리 포인트)
# if __name__ == "__main__":
#     mcp.run()


# Github 에 배포 후 사용 
def main():
    mcp.run()

if __name__ == "__main__":
    main()