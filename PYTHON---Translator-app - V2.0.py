import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

def translate_text(text, target_language):
    """
    Translates the given text into the target language using Google Translate API.

    :param text: str, the text to translate
    :param target_language: str, the target language code (e.g., 'es' for Spanish, 'fr' for French)
    :return: str, the translated text
    """
    translator = Translator()

    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        return f"An error occurred: {e}"

def translate_button_action():
    text = text_input.get("1.0", tk.END).strip()
    target_language = language_input.get().strip()

    if not text:
        messagebox.showwarning("Input Error", "Please enter the text to translate.")
        return

    if not target_language:
        messagebox.showwarning("Input Error", "Please enter the target language code.")
        return

    translated_text = translate_text(text, target_language)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated_text)

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Text Translator")

    # Input text label and text box
    tk.Label(root, text="Enter text to translate:").pack(pady=5)
    global text_input
    text_input = tk.Text(root, height=10, width=50)
    text_input.pack(pady=5)

    # Target language label and entry
    tk.Label(root, text="Enter target language code (e.g., 'es' for Spanish):").pack(pady=5)
    global language_input
    language_input = tk.Entry(root, width=10)
    language_input.pack(pady=5)

    # Translate button
    translate_button = tk.Button(root, text="Translate", command=translate_button_action)
    translate_button.pack(pady=10)

    # Output text label and text box
    tk.Label(root, text="Translated text:").pack(pady=5)
    global output_text
    output_text = tk.Text(root, height=10, width=50)
    output_text.pack(pady=5)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
