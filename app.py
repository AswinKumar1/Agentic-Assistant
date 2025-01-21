from modules.voice import listen, speak
from modules.internet_search import search_web
from modules.vectordb import store_knowledge, query_knowledge
from modules.ai_agent import create_agent
from modules.note_manager import save_note, list_notes, read_note

def main():
    speak("Welcome! How can I assist you today?")
    while True:
        command = listen()
        
        if "take a note" in command:
            speak("What should I note down?")
            note = listen()
            save_note(note, "note.txt")
            speak("Note saved.")
        elif "read notes" in command:
            notes = list_notes()
            speak(f"You have {len(notes)} notes.")
            for note in notes:
                speak(read_note(note))
        elif "search internet" in command:
            speak("What should I search for?")
            query = listen()
            results = search_web(query)
            speak("Here are the top results.")
            for result in results[:3]:
                speak(result)
        elif "find knowledge" in command:
            speak("What should I look for?")
            query = listen()
            result = query_knowledge(query)
            if result:
                speak(f"I found this in the database: {result}")
            else:
                speak("No relevant knowledge found. Searching the internet.")
                results = search_web(query)
                speak("Here are the top results.")
                for result in results[:3]:
                    speak(result)
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that.")

if __name__ == "__main__":
    main()
