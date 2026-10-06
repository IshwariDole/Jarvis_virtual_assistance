import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import os
import time

import musicLibrary

from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# ============================================================
# GEMINI CLIENT
# ============================================================

if GEMINI_API_KEY:
    gemini_client = genai.Client(
        api_key=GEMINI_API_KEY
    )
else:
    gemini_client = None


# ============================================================
# SPEECH RECOGNIZER
# ============================================================

recognizer = sr.Recognizer()


# ============================================================
# SPEAK FUNCTION
# ============================================================

def speak(text):
    """
    Convert text to speech.

    A new pyttsx3 engine is created for every sentence.
    This is intentional because reusing the same engine
    was causing only the first sentence to be spoken
    on this Windows system.
    """

    print("Jarvis:", text)

    try:

        engine = pyttsx3.init()

        engine.setProperty(
            "rate",
            160
        )

        engine.setProperty(
            "volume",
            1.0
        )

        engine.say(text)

        engine.runAndWait()

        engine.stop()

        time.sleep(0.3)

    except Exception as e:

        print(
            "Voice Error:",
            e
        )


# ============================================================
# GEMINI AI PROCESSING
# ============================================================
def ai_process(command):

    if gemini_client is None:
        return "Sorry mam, Gemini API key is not configured."

    models = [
        "gemini-3.8-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite",
        "gemini-3.5-flash"
    ]

    prompt = (
        "You are Jarvis, a helpful voice assistant. "
        "Answer the user's question clearly and briefly because "
        "your answer will be spoken aloud. "
        "Do not use markdown, tables, bullet points, or unnecessary formatting. "
        "Keep the answer easy to understand.\n\n"
        f"User question: {command}"
    )

    for model in models:

        for attempt in range(2):

            try:
                print(f"Trying Gemini model: {model} "
                      f"(attempt {attempt + 1})")

                interaction = gemini_client.interactions.create(
                    model=model,
                    input=prompt
                )

                answer = interaction.output_text

                if answer:
                    print("Gemini answer received.")
                    return answer.strip()

                print("Gemini returned an empty response.")

            except Exception as e:

                error_text = str(e)

                print(f"Gemini error with {model}: {error_text}")

                # Retry temporary server overload
                if "503" in error_text or "UNAVAILABLE" in error_text:
                    if attempt == 0:
                        print("Temporary Gemini server issue. Retrying...")
                        time.sleep(3)
                        continue

                # Try next model
                break

    return (
        "Sorry mam, Gemini is temporarily unavailable. "
        "Please try again in a moment."
    )
# ============================================================
# NEWS
# ============================================================

def get_news():

    if not NEWS_API_KEY:
        speak("News API key is not configured.")
        return

    try:

        print("Getting latest news...")

        url = "https://newsapi.org/v2/top-headlines"

        params = {
            "country": "in",
            "category": "general",
            "pageSize": 5,
            "apiKey": NEWS_API_KEY
        }

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        print(
            "News API status:",
            response.status_code
        )

        data = response.json()

        if response.status_code != 200:

            print("News API Error:")
            print(data)

            speak(
                "Sorry mam, the news service "
                "returned an error."
            )

            return

        print(
            "News API total results:",
            data.get("totalResults", 0)
        )

        articles = data.get(
            "articles",
            []
        )

        if not articles:

            # Try a second query using a keyword
            print(
                "No country headlines found. "
                "Trying keyword search..."
            )

            search_params = {
                "q": "India",
                "language": "en",
                "pageSize": 5,
                "apiKey": NEWS_API_KEY
            }

            search_response = requests.get(
                "https://newsapi.org/v2/everything",
                params=search_params,
                timeout=15
            )

            print(
                "News search status:",
                search_response.status_code
            )

            search_data = search_response.json()

            if search_response.status_code == 200:

                articles = search_data.get(
                    "articles",
                    []
                )

        if not articles:

            speak(
                "Sorry mam, no news articles "
                "are currently available."
            )

            return

        speak(
            "Here are the latest news headlines."
        )

        for index, article in enumerate(
            articles[:5],
            start=1
        ):

            title = article.get("title")

            if title:

                print(
                    f"{index}. {title}"
                )

                speak(
                    f"Headline {index}. {title}"
                )

    except requests.exceptions.Timeout:

        print(
            "News API request timed out."
        )

        speak(
            "Sorry mam, the news service "
            "is taking too long to respond."
        )

    except requests.exceptions.RequestException as e:

        print(
            "News connection error:",
            e
        )

        speak(
            "Sorry mam, I couldn't connect "
            "to the news service."
        )

    except Exception as e:

        print(
            "News error:",
            e
        )

        speak(
            "Sorry mam, something went wrong "
            "while getting the news."
        )

        # ------------------------------------------------
        # CHECK API STATUS
        # ------------------------------------------------

        if data.get("status") != "ok":

            print(
                "News API returned:",
                data
            )

            speak(
                "Sorry mam, I couldn't get "
                "the latest news."
            )

            return

        # ------------------------------------------------
        # GET ARTICLES
        # ------------------------------------------------

        articles = data.get(
            "articles",
            []
        )

        print(
            "Number of articles:",
            len(articles)
        )

        if not articles:

            speak(
                "Sorry mam, no news articles "
                "were returned."
            )

            return

        # ------------------------------------------------
        # SPEAK HEADLINES
        # ------------------------------------------------

        speak(
            "Here are the latest news headlines."
        )

        for index, article in enumerate(
            articles[:5],
            start=1
        ):

            title = article.get(
                "title"
            )

            if title:

                print(
                    f"{index}. {title}"
                )

                speak(
                    f"Headline {index}. {title}"
                )

    except requests.exceptions.Timeout:

        print(
            "News API request timed out."
        )

        speak(
            "Sorry mam, the news service "
            "is taking too long to respond."
        )

    except requests.exceptions.RequestException as e:

        print(
            "News connection error:",
            e
        )

        speak(
            "Sorry mam, I couldn't connect "
            "to the news service."
        )

    except Exception as e:

        print(
            "News error:",
            e
        )

        speak(
            "Sorry mam, something went wrong "
            "while getting the news."
        )

# ============================================================
# PROCESS COMMAND
# ============================================================

def process_command(command):

    command = command.lower().strip()

    print(
        "Command:",
        command
    )


    # --------------------------------------------------------
    # GOOGLE
    # --------------------------------------------------------

    if "open google" in command:

        speak(
            "Opening Google."
        )

        webbrowser.open(
            "https://www.google.com"
        )


    # --------------------------------------------------------
    # YOUTUBE
    # --------------------------------------------------------

    elif "open youtube" in command:

        speak(
            "Opening YouTube."
        )

        webbrowser.open(
            "https://www.youtube.com"
        )


    # --------------------------------------------------------
    # FACEBOOK
    # --------------------------------------------------------

    elif "open facebook" in command:

        speak(
            "Opening Facebook."
        )

        webbrowser.open(
            "https://www.facebook.com"
        )


    # --------------------------------------------------------
    # INSTAGRAM
    # --------------------------------------------------------

    elif "open instagram" in command:

        speak(
            "Opening Instagram."
        )

        webbrowser.open(
            "https://www.instagram.com"
        )


    # --------------------------------------------------------
    # LINKEDIN
    # --------------------------------------------------------

    elif "open linkedin" in command:

        speak(
            "Opening LinkedIn."
        )

        webbrowser.open(
            "https://www.linkedin.com"
        )


    # --------------------------------------------------------
    # MUSIC
    # --------------------------------------------------------

    elif command.startswith("play"):

        words = command.split(
            maxsplit=1
        )

        if len(words) < 2:

            speak(
                "Please tell me the song name."
            )

            return True

        song = words[1]

        if song in musicLibrary.music:

            speak(
                f"Playing {song}."
            )

            webbrowser.open(
                musicLibrary.music[song]
            )

        else:

            speak(
                "Sorry mam, that song is "
                "not in my music library."
            )


    # --------------------------------------------------------
    # NEWS
    # --------------------------------------------------------

    elif "news" in command:

        get_news()


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    elif (
        "exit" in command
        or "quit" in command
        or "stop jarvis" in command
        or "goodbye" in command
    ):

        speak(
            "Goodbye mam."
        )

        return False


    # --------------------------------------------------------
    # GEMINI AI
    # --------------------------------------------------------

    else:

        speak(
            "Let me think mam."
        )

        response = ai_process(
            command
        )

        speak(
            response
        )


    return True


# ============================================================
# LISTEN FOR WAKE WORD
# ============================================================

def listen_for_wake_word():

    try:

        with sr.Microphone() as source:

            print(
                "\nListening for Jarvis..."
            )

            audio = recognizer.listen(

                source,

                timeout=5,

                phrase_time_limit=3
            )

        word = recognizer.recognize_google(
            audio
        )

        print(
            "You said:",
            word
        )

        return word.lower()


    except sr.WaitTimeoutError:

        return ""


    except sr.UnknownValueError:

        return ""


    except sr.RequestError as e:

        print(
            "Speech Recognition Error:",
            e
        )

        return ""


# ============================================================
# LISTEN FOR COMMAND
# ============================================================

def listen_for_command():

    try:

        with sr.Microphone() as source:

            print(
                "Jarvis Active..."
            )

            audio = recognizer.listen(

                source,

                timeout=5,

                phrase_time_limit=8
            )

        command = recognizer.recognize_google(
            audio
        )

        print(
            "You said:",
            command
        )

        return command


    except sr.WaitTimeoutError:

        speak(
            "I didn't hear anything mam."
        )

        return ""


    except sr.UnknownValueError:

        speak(
            "Sorry mam, I didn't understand."
        )

        return ""


    except sr.RequestError as e:

        print(
            "Speech Recognition Error:",
            e
        )

        speak(
            "Speech recognition service "
            "is unavailable."
        )

        return ""


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    speak(
        "Initializing Jarvis."
    )

    while True:

        # Listen for "Jarvis"
        word = listen_for_wake_word()

        # Wake Jarvis
        if "jarvis" in word:

            speak(
                "Yes mam?"
            )

            # Listen for command
            command = listen_for_command()

            if command:

                should_continue = process_command(
                    command
                )

                if not should_continue:

                    break