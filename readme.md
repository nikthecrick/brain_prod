

# Mind Conversation with AI Assistants

Welcome to the Mind Conversation application, which allows you to engage in a conversation with AI agents representing different aspects of the mind, such as the Ego, Super Ego, and Id. You can explore psychological decision-making and engage in dialogues with these agents using Pygame and OpenAI's GPT-3 models.

![Demo](demo.gif)

## Installation

To set up the project environment, please follow these steps:

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/nikthecrick/brain_prod.git
   cd brain_prod
   ```

2. Create a virtual environment to isolate project dependencies.

   - **Windows:**

     ```bash
     python -m venv venv
     ```

   - **macOS and Linux:**

     ```bash
     python3 -m venv venv
     ```

3. Activate the virtual environment:

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

4. Install the required Python libraries using pip. This includes `pygame` for the graphical interface and `autogen` to interact with GPT-3.

   ```bash
   pip3 install pygame
   pip3 install pyautogen
   pip3 install openai
   ```
## OpenAI API Key Configuration

Before you can run the project, you need to obtain an OpenAI API key and configure it in the `config.json` file included in the repository. Follow these steps:

1. **Sign Up for OpenAI:**
   - If you don't have an OpenAI account, you can sign up for one on the [OpenAI website](https://beta.openai.com/signup/).

2. **Get Your API Key:**
   - After signing up and logging in to OpenAI, navigate to your dashboard to find your API key. It will look something like this:
     ```
     api_key = 'sk-abcdefghijklmnopqrstuvwxyz123456'
     ```

3. **Configure Your API Key:**
   - In your project directory, open the `config.json` file. Replace the value for `api_key` with your actual OpenAI API key.

Here's an example of how the `config.json` file should look:

```json
{
    "api_key": "sk-abcdefghijklmnopqrstuvwxyz123456"
}


## Usage

Now that you've set up the environment, you can start the application:

1. **Configure Conversation:**

   - You can adjust the conversation setup and GPT-3/4/Opensource models in the `brAIn.py` script.

2. **Initiate Conversation:**

   Run the following command to start the application:

   ```bash
   python3 brAIn.py
   ```

3. **Start the Conversation:**

   You will be prompted to enter your initial message. After that, the conversation will be initiated with AI agents representing different aspects of the mind, and a discussion will take place.

4. **Explore the Dialogues:**

   You can explore the dialogues between the Ego, Super Ego, and Id as they discuss the topic. The conversation will be displayed graphically, and you can read through the dialogues.

5. **Exit Application:**

   To exit the application, simply close the Pygame window.

## Customization

Feel free to customize the application by modifying the conversation setup, graphical elements, or even the content of the conversation. You can also add or modify images for different aspects of the mind and adjust the display as needed.

