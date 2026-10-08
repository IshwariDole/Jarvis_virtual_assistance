# 🤖 Jarvis Virtual Assistant

A Python-based voice assistant that listens for the wake word **"Jarvis"**, understands spoken commands, performs web and music-related tasks, provides current news, and answers general questions using the **Google Gemini API**.

The project uses speech recognition, text-to-speech, external APIs, and Python automation to create a simple real-world voice assistant.

---

## ✨ Features

* 🎙️ **Wake Word Detection**

  * Activates when you say **"Jarvis"**

* 🔊 **Voice Responses**

  * Uses `pyttsx3` for text-to-speech

* 🎤 **Speech Recognition**

  * Converts your voice commands into text using Google Speech Recognition

* 🌐 **Website Automation**

  * Open Google
  * Open YouTube
  * Open Facebook
  * Open Instagram
  * Open LinkedIn

* 🎵 **Music Playback**

  * Play songs from the configured music library
  * Opens the corresponding YouTube video

* 🤖 **AI Question Answering**

  * Uses Google Gemini API
  * Answers general questions conversationally
  * Designed for short voice-friendly responses

* 📰 **News**

  * Fetches news using NewsAPI

* 🚪 **Exit Commands**

  * Supports commands such as:

    * `exit`
    * `quit`
    * `stop Jarvis`
    * `goodbye`

* 🔐 **Environment Variables**

  * API keys are stored in `.env`
  * `.env` is excluded from GitHub using `.gitignore`

---

## 🛠️ Technologies Used

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Core programming language       |
| SpeechRecognition | Speech-to-text                  |
| PyAudio           | Microphone input                |
| pyttsx3           | Text-to-speech                  |
| Google Gemini API | AI question answering           |
| NewsAPI           | News retrieval                  |
| python-dotenv     | Environment variable management |
| Requests          | API requests                    |
| Webbrowser        | Opening websites                |
| YouTube           | Music playback                  |


## ⚙️ Requirements

* Python 3.x
* Working microphone
* Internet connection
* Google Gemini API key
* NewsAPI key



### ⚠️ Important

Never upload `.env` to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---


## 🎤 Example Commands

### Open Websites

```text
Jarvis → open Google
```

```text
Jarvis → open YouTube
```

```text
Jarvis → open Instagram
```

```text
Jarvis → open LinkedIn
```

### Play Music

```text
Jarvis → play Perfect
```

```text
Jarvis → play Believer
```

### Ask Questions

```text
Jarvis → What is Python?
```

```text
Jarvis → What is artificial intelligence?
```

```text
Jarvis → Explain machine learning
```

Jarvis sends the question to Gemini and speaks the generated response.

### News

```text
Jarvis → Tell me the news
```

### Exit

```text
Jarvis → exit
```

or:

```text
Jarvis → quit
```

---

## 🧠 How It Works

The basic workflow is:

```text
                ┌─────────────────┐
                │   User speaks   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ SpeechRecognition│
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Detect "Jarvis" │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Listen Command   │
                └────────┬────────┘
                         ↓
              ┌──────────┴──────────┐
              ↓                     ↓
       Local Commands          AI / API Commands
              ↓                     ↓
    ┌──────────────────┐    ┌─────────────────┐
    │ Websites / Music │    │ Gemini / NewsAPI│
    └────────┬─────────┘    └────────┬────────┘
             │                       │
             └──────────┬────────────┘
                        ↓
                 ┌──────────────┐
                 │   pyttsx3    │
                 │ Voice Output │
                 └──────────────┘
```

---

## 🔄 AI Question Flow

For general questions, Jarvis uses the Gemini API:

```text
Voice Command
      ↓
Speech Recognition
      ↓
Text Command
      ↓
Gemini API
      ↓
AI Generated Response
      ↓
Text-to-Speech
      ↓
Jarvis Speaks
```

The application uses multiple Gemini Flash models with fallback handling for temporary service availability issues.

---



## 🚧 Limitations

* Speech recognition requires an internet connection.
* Gemini responses depend on API availability and usage limits.
* News availability depends on the NewsAPI service and API plan.
* Music playback opens YouTube in the browser.
* Background noise can affect speech recognition.
* The assistant currently uses a simple wake-word detection approach rather than a dedicated offline wake-word engine.

---

## 🔮 Future Improvements

Possible future enhancements:

* 🧠 Conversation memory
* 🎙️ Better wake-word detection
* 📱 GUI interface
* 🖥️ Desktop application
* 📧 Email automation
* 🌦️ Weather information
* ⏰ Reminders and alarms
* 📁 File and folder automation
* 🔍 Web search
* 🗣️ More natural voice output
* 🔐 User authentication
* 📴 Offline speech recognition
* 🤖 More advanced AI agent capabilities

---

## 👩‍💻 Author

**Ishwari Dole**

B.Tech Computer Science Engineering Graduate
June 2026 Passout

GitHub:

https://github.com/IshwariDole

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for learning, experimentation, and portfolio purposes.
