import tkinter as tk
from googletrans import Translator

def translate_text():
    text = text_entry.get("1.0", "end-1c")
    input_language = input_lang.get()
    target_language = output_lang.get()

    translator = Translator()
    translated_text = translator.translate(text, src=input_language, dest=target_language)
    translated_entry.delete("1.0", "end")
    translated_entry.insert("1.0", translated_text.text)

def main():
    global text_entry, translated_entry, output_lang, input_lang

    root = tk.Tk()
    root.title("Translator App")

    # Input Text Area
    input_label = tk.Label(root, text="Enter text to translate:")
    input_label.pack()
    text_entry = tk.Text(root, height=5, width=40)
    text_entry.pack()

    # Output Text Area
    translated_label = tk.Label(root, text="Translated text:")
    translated_label.pack()
    translated_entry = tk.Text(root, height=5, width=40)
    translated_entry.pack()

    # Language Selection
    languages = {
        'English': 'en',
        'Spanish': 'es',
        'French': 'fr',
        'German': 'de',
        # Add more languages and their language codes here
    }

    input_lang = tk.StringVar(root)
    input_lang.set('en')  # Default input language is English

    output_lang = tk.StringVar(root)
    output_lang.set('en')  # Default output language is English

    input_lang_label = tk.Label(root, text="Select input language:")
    input_lang_label.pack()

    input_lang_menu = tk.OptionMenu(root, input_lang, *languages.values())
    input_lang_menu.pack()

    output_lang_label = tk.Label(root, text="Select output language:")
    output_lang_label.pack()

    output_lang_menu = tk.OptionMenu(root, output_lang, *languages.values())
    output_lang_menu.pack()

    # Translate Button
    translate_button = tk.Button(root, text="Translate", command=translate_text)
    translate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
