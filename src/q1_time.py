import json
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
from operator import itemgetter
from memory_profiler import profile


@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    user_posts_count = defaultdict(lambda: defaultdict(int))
    dates = {}
        
    with open(file_path) as f:
        for line in f:
            jsonline = json.loads(line)
            date_string = jsonline['date'][:10]
            date = datetime.strptime(date_string, '%Y-%m-%d').date()
            username = jsonline['user']['username']
            user_posts_count[date][username] += 1 
            if date not in dates:
                dates[date] = 0
            dates[date] += 1

        sorted_items = sorted(dates.items(), key=itemgetter(1), reverse=True)
        top_10_keys = [key for key, _ in sorted_items[:10]]        

        max_posts_by_day = []
        for date, user_counts in user_posts_count.items():
            max_user = max(user_counts, key=user_counts.get)
            max_posts_by_day.append((date, max_user))
        
        filter_results = [dato for dato in max_posts_by_day if dato[0] in top_10_keys]
    
    return filter_results