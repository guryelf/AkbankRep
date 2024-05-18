import json
import pandas as pd

class CategoryTranslator:
    def __init__(self, translations_file):
        self.translations_file = translations_file
        self.category_mapping = self.load_mapping()

    def load_mapping(self):
        try:
            with open(self.translations_file, 'r', encoding='utf-8') as f:
                translations = json.load(f)
                category_mapping = translations.get('category_translations', {})
                print("DEBUG: Successfully loaded translations:", category_mapping)
                return category_mapping
        except Exception as e:
            print("DEBUG: Error loading translations:", e)
            return {}

    def translate_categories(self, df, column_name):
        print("DEBUG: Loaded translations:", self.category_mapping)
        df['translated_category'] = df[column_name].map(self.category_mapping.get)
        return df

    def get_translation(self, category):
        return self.category_mapping.get(category)
