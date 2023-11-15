import json
import demoji
import pandas as pd
from datetime import datetime
from typing import List, Tuple
from collections import Counter
from collections import defaultdict


def Q3_memory(data: pd.DataFrame) -> List[Tuple[str, int]]:
    mention_count = defaultdict(int)
    
    try:
        for index, row in data.iterrows():
            # Manejo de errores al acceder a mentionedUsers
            try:
                mentioned_users = row.get("mentionedUsers")
            except (KeyError, AttributeError) as mentioned_users_error:
                print(f"Error al acceder a mentionedUsers en la fila {index}: {mentioned_users_error}")
                continue

            # Verificar si mentioned_users no es nulo
            if mentioned_users is not None:
                for user in mentioned_users:
                    # Manejo de errores al acceder a username
                    try:
                        username = user.get("username")
                    except (KeyError, AttributeError) as username_error:
                        print(f"Error al acceder a username en la fila {index}: {username_error}")
                        continue

                    if username is not None:
                        mention_count[username] += 1

    except Exception as general_error:
        print(f"Error inesperado: {general_error}")
        return []

    top_users = sorted(mention_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_users