import re
import json
from collections import Counter

def get_most_used_words(file_path):    
    words_list = []
    stop_words = {
        "the", "a", "i", "you", "to", "and", "is", "it", "in", "my", "of", "for", 
        "me", "that", "on", "he", "she", "we", "they", "was", "with", "at", "as",
        "do", "don't", "can", "can't", "just", "but", "so", "what", "where", "when",
        "how", "will", "would", "from", "up", "out", "get", "go", "no", "yes", "ok",
        "okay", "lol", "hahaha", "haha", "yeah", "hey", "hi", "hello", "good",
        "day", "like", "know", "think", "really", "want", "time", "if", "or",
        "be", "been", "have", "had", "are", "by", "this", "your", "its", "im", "am", "pm",
        "gt", "okay", "ya", "na", "wo"
    }

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            if ':' in line and len(line.split(':', 1)) > 1:
                message = line.split(':', 1)[1].strip().lower()
            else:
                message = line.lower().strip()

            message = re.sub(r'http\S+|www\S+', '', message)
            message = re.sub(r'[\U00010000-\U0010ffff]', '', message)
            clean_words = re.findall(r'\b[a-z]{3,}\b', message) 
            
            words_list.extend([w for w in clean_words if w not in stop_words])

    most_common = Counter(words_list).most_common(70) 
    
    output_data = [{"word": word, "count": count} for word, count in most_common]
    
    with open('words.json', 'w', encoding='utf-8') as json_file:
        json.dump(output_data, json_file, indent=4)
    
    print(f"Generated words.json with {len(output_data)} most frequent words.")

get_most_used_words(r"C:\Users\mawlo\OneDrive\Desktop\mesh bday\WhatsApp Chat with Mesh.txt")