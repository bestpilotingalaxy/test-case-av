# import pytest

# from ..parsing.parsing import get_location_id, parse_count


# @pytest.mark.asyncio
# async def test_get_location_id():
    
#     moscow_id = await get_location_id("Москва")
#     assert moscow_id == 637640
    

# @pytest.mark.asyncio
# async def test_get_invalid_location_id():
    
#     nun = await get_location_id("Абракадабра")
#     assert nun == None
    

# @pytest.mark.asyncio
# async def test_parse_count():
    
#     count = await parse_count("Модные чешки", 637640)
#     assert type(count) == int
    