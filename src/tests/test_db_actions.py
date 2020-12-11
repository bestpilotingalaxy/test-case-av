# from datetime import datetime
# from bson import ObjectId

# import pytest

# from .conftest import create_timestamps
# from ..db import actions as db


# @pytest.mark.asyncio
# async def test_insert_and_find_pair(event_loop):
    
#     pair_id = await db.add_new_pair(
#         keyword="Клюшка", location="Москва", location_id=637640
#     )
#     inserted_pair = db.pairs_collection.find_one({"_id": ObjectId(pair_id)})
#     assert pair_id == str
#     assert inserted_pair != None
    

# @pytest.mark.asyncio    
# async def test_get_all_pairs(event_loop):
    
#     db.pairs_collection.drop()
#     db.pairs_collection.insert_many([
#         {
#             "keyword": "Тестировщик",
#             "location": "Москва",
#             "location_id": 637640
#         },
#         {
#             "keyword": "Бетон",
#             "location": "Москва",
#             "location_id": 637640
#         }
#     ])
#     pairs = await db.get_all_pairs()
#     assert len(pairs) == 2

    
# @pytest.mark.asyncio
# async def test_get_stats(event_loop):
    
#     pair_id = ObjectId()
#     db.stats_collection.insert_one({
#         "pair_id": pair_id,
#         "count": 322,
#         "timestamp": datetime.now().isoformat()
#     })
#     timestamps = create_timestamps(1, 0)
#     stats =  await db.get_stats(
#         str(pair_id), timestamps["start"], timestamps["end"]
#     )
#     assert stats == list
#     assert len(stats) == 1
#     assert stats[0]["count"] == 322
     