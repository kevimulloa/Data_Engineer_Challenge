import json
import demoji
import pandas as pd
from datetime import datetime
from typing import List, Tuple
from collections import Counter
from collections import defaultdict


def extract_emojis(text: str) -> List[str]:
    try:
        return list(demoji.findall(text).keys())
    except Exception as extraction_error:
        print(f"Error al extraer emojis: {extraction_error}")
        return []

def Q2_memory(data: pd.DataFrame) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    try:
        for _, entry in data.iterrows():
            # Manejo de errores al acceder al contenido
            try:
                content = entry.get('content', '')
            except (KeyError, AttributeError) as content_error:
                print(f"Error al acceder al contenido: {content_error}")
                continue

            emojis = extract_emojis(content)
            emoji_counter.update(emojis)

    except Exception as general_error:
        print(f"Error inesperado: {general_error}")
        return []

    return emoji_counter.most_common(10)