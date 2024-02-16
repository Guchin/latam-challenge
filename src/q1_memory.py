import json
from typing import List, Tuple
from collections import defaultdict
from datetime import datetime
from memory_profiler import profile

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    user_posts_count = defaultdict(lambda: defaultdict(int))
        
    with open(file_path) as f:
        for line in f:
            jsonline = json.loads(line)
            date_string = jsonline['date'][:10]
            date = datetime.strptime(date_string, '%Y-%m-%d').date()
            username = jsonline['user']['username']
            user_posts_count[date][username] += 1 

        # Obtener las 10 fechas con más publicaciones
        sorted_items = sorted(user_posts_count.items(), key=lambda x: sum(x[1].values()), reverse=True)
        top_10_dates = [key for key, _ in sorted_items[:10]]        

        # Obtener las publicaciones máximas por día y filtrar según las 10 fechas principales
        max_posts_by_day = [(date, max(user_counts, key=user_counts.get)) for date, user_counts in user_posts_count.items() if date in top_10_dates]
    
    return max_posts_by_day