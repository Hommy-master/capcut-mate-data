from fastapi import APIRouter, Request, Depends
from src.schemas.timelines import TimelinesRequest, TimelinesResponse
from src import service
from src.utils.logger import logger
import config


router = APIRouter(prefix="/v1", tags=["v1"])

@router.post(path="/timelines", response_model=TimelinesResponse)
def timelines(request: TimelinesRequest) -> TimelinesResponse:
    """
    创建时间线 (v1版本)
    """
    logger.info("Received request to calculate timelines")
    
    # 调用service层处理业务逻辑
    timelines, all_timelines = service.timelines.timelines(
        duration=request.duration,
        num=request.num,
        start=request.start,
        type=request.type
    )

    return TimelinesResponse(timelines=timelines, all_timelines=all_timelines)