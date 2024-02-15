import json
from typing import List, Tuple
from collections import Counter
import emoji
import heapq

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    top_10_emojis = []
    
    with open(file_path) as f:
        emoji_counter = Counter()
        
        for line in f:
            jsonline = json.loads(line)
            content = jsonline['content']
            emoji_list = emoji.distinct_emoji_list(content)
            emoji_counter.update(emoji_list)
        
        # Mantener un seguimiento de los 10 emojis principales usando un heap
        for emoji_sign, count in emoji_counter.items():
            if len(top_10_emojis) < 10:
                heapq.heappush(top_10_emojis, (count, emoji_sign))
            else:
                heapq.heappushpop(top_10_emojis, (count, emoji_sign))
    
    # Ordenar los 10 emojis principales en orden descendente por recuento
    top_10_emojis.sort(reverse=True)
    
    return top_10_emojis





    """totaL_emojis = {}
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

    
    return top_10_emojis"""