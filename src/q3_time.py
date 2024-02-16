from typing import List, Tuple
from collections import defaultdict
import json
from memory_profiler import profile

@profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    usernames_dic = {}
    with open(file_path) as f:
        for line in f:
            jsonline = json.loads(line)
            try: 
                mentioned = jsonline['mentionedUsers']
                usernames = [mention['username'] for mention in mentioned]
            except:
                pass             
                                
            for user in usernames:
                if user not in usernames_dic:
                    usernames_dic[user] = 0
                usernames_dic[user] += 1
        
        # Obtener las 10 fechas con más publicaciones
        sorted_items = sorted(usernames_dic.items(), key=lambda x: x[1], reverse=True)
        
        top_10 = sorted_items[:10]

    
    return top_10