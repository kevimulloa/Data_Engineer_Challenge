import json
import demoji
import pandas as pd
from datetime import datetime
from typing import List, Tuple
from collections import Counter
from collections import defaultdict

def Q1_memory(data: pd.DataFrame) -> List[Tuple[datetime.date, str]]:
    date_user_count = {}
    
    try:
        for index, entry in data.iterrows():
            # Manejo de errores al convertir la fecha
            try:
                date_str = entry.get('date', '').split('T')[0]
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except (ValueError, TypeError) as date_error:
                print(f"Error al convertir la fecha en la fila {index}: {date_error}")
                continue

            # Manejo de errores al acceder al usuario
            try:
                user = entry.get('user', {}).get('username', '')
            except (KeyError, AttributeError) as user_error:
                print(f"Error al acceder al nombre de usuario en la fila {index}: {user_error}")
                continue

            if date not in date_user_count:
                date_user_count[date] = Counter()
            date_user_count[date][user] += 1
    
    except Exception as general_error:
        print(f"Error inesperado: {general_error}")
        return []

    top_users_by_date = [(date, user_count.most_common(1)[0][0]) for date, user_count in date_user_count.items()]
    return sorted(top_users_by_date, key=lambda x: x[0], reverse=True)[:10]
