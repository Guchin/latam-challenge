from typing import List, Tuple
import emoji
import json
from memory_profiler import profile

@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:

 
    totaL_emojis = {}
    with open(file_path) as f:
        for line in f:
            jsonline = json.loads(line)            
            content = jsonline['content']
            emoji_list = emoji.distinct_emoji_list(content)            
            for emoji_sign in emoji_list:
                if emoji_sign not in totaL_emojis:
                    totaL_emojis[emoji_sign] = 0
                totaL_emojis[emoji_sign] += 1
        
        # Obtener las 10 fechas con más publicaciones
        sorted_items = sorted(totaL_emojis.items(), key=lambda x: x[1], reverse=True)
        
        top_10_emojis = sorted_items[:10]

    
    return top_10_emojis