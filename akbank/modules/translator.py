import json
import pandas as pd

class CategoryTranslator:
    def __init__(self, translations_file):
        self.translations_file = translations_file
        self.category_mapping = self.load_mapping()

    def load_mapping(self):
        with open(self.translations_file, 'r', encoding='utf-8') as f:
            translations = json.load(f)
            return translations.get('category_translations', {})

    def translate_categories(self, df, column_name):
        # Create a new column for the Turkish translations
        df['translated_category'] = df[column_name].map(self.category_mapping.get)
        return df

    def get_translation(self, category):
        # Get the translation for a specific category
        return self.category_mapping.get(category)