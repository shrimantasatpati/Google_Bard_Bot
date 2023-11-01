# Google_Bard_Bot 

Welcome to the **Google Bard Bot** project! A chat interface in Gradio seamlessly interact with 🤖 **Google Bard**, a remarkable conversational AI developed by Google.

## Getting Started 🚀

Let's embark on a journey to set up and launch the project on your local machine for developmental and testing purposes.

### Prerequisites 📋

Before we dive in, ensure you have the following prerequisites:

- Python 3.11 or newer 🐍
- IDE (Visual Studio Code)

### Installation 🛠️

1. Begin by cloning the repository:
    git clone https://github.com/shrimantasatpati/Google_Bard_Bot.git
    cd Google_Bard_Bot

2. Create a virtual environment and install the necessary packages:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Launch the application on localhost:
   Run the following command: python bardtesten.py in the terminal/console.

Your application should now be live at `http://localhost:8000`.

### Usage 📦

To utilize the power of the Google Bard API, follow these steps:

1. Obtain the cookies as mentioned on **bard.google.com** from an authorized session. These cookies will be used to send POST requests to the `/ask` endpoint, accompanied by a message in a JSON payload. Make sure to include the `session_id`, which corresponds to the `__Secure-1PSID` cookie, in your request.

## License 📜

The code presented in this repository is generously licensed for unrestricted use, devoid of limitations or warranties.

## Acknowledgments 🙌

A special thanks to:

- Google for creating the visionary Google Bard
- FastAPI for providing an elegant and efficient web framework

Your participation and contributions are truly appreciated! Happy coding! 🎉
