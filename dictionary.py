import tkinter as tk
import requests

def fetch_word_info():
    word = entry.get()
    api_key = '65503323-86d9-492f-b203-d9c2d307b077'
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            word_info = data[0]
            meaning = word_info.get("shortdef", ["Not found"])
            origin = word_info.get("et", ["Not found"])
            first_use = word_info.get("date", ["Not found"])
            synonyms = word_info.get("meta", {}).get("syns", [["Not found"]])
            antonyms = word_info.get("meta", {}).get("ants", [["Not found"]])
            part_of_speech = word_info.get("fl", ["Not found"])
            result_text.delete("1.0", tk.END)

            result_text.insert(tk.END, f"Meaning: {', '.join(meaning)}\n")
            result_text.insert(tk.END, f"Origin: {origin[0]}\n" if origin != ["Not found"] else "Origin: Not found\n")
            result_text.insert(tk.END, f"First Use: {', '.join(first_use)}\n")
            result_text.insert(tk.END, f"Synonyms: {', '.join([syn for sublist in synonyms for syn in sublist])}\n" if synonyms != [["Not found"]] else "Synonyms: Not found\n")
            result_text.insert(tk.END, f"Antonyms: {', '.join([ant for sublist in antonyms for ant in sublist])}\n" if antonyms != [["Not found"]] else "Antonyms: Not found\n")
            result_text.insert(tk.END, f"Part of Speech: {part_of_speech}\n")
        else:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "The city you entered is not not found in the dictionary.")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "An error occurred while connecting to the API.")

#Tkinter window
window = tk.Tk()
window.title("Word/City Dictionary")
window.configure(background="black")
#HEADER
title_label = tk.Label(window, text="city name", bg="black", fg="white", font=("Helvetica", 20))
title_label.pack(pady=20)
#ENTRY FIELD
entry = tk.Entry(window, font=("Montserrat", 15),bg="grey")
entry.insert(0, "Enter the word/city name")
entry.pack(pady=10)

#SUBMIT BUTTON
submit_button = tk.Button(window, text="Submit", command=fetch_word_info, font=("Roboto", 14),bg="green")
submit_button.pack(pady=10)
result_text = tk.Text(window, width=60, height=10)
result_text.pack()
window.mainloop()
