# ----------------------------------------------------------------------
# brAIn
# Created by: Nik Niksen
# This script initiates a conversation between different parts of the human mind
# and displays it. It also saves the conversation to a text file.
#
# Copyright (c) 2023 Nik Niksen. All rights reserved.
# ----------------------------------------------------------------------

import autogen
import io
import json
import pygame
import sys

# Function to initiate and save the conversation
def initiate_and_save_conversation():
    #human_input = input("Enter the initial message: ")
    #initial_message = "Your mind goes through the neural psychological process of taking a decision. Have a long discussion with all parts of your mind (Ego, Super Ego, and Id), Where every part should try to overpower the other two, about: " + human_input

    # Your conversation setup code here
    config_list_gpt4 = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        filter_dict={
            "model": ["gpt-3.5-turbo-16k"],
        },
    )

    config_list_gpt3 = [
        {
            'model': 'gpt-3.5-turbo-16k',
            'api_key': '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',
        }
    ]

    gpt4_config = {
        "seed": 37,
        "temperature": 0.7,
        "config_list": config_list_gpt3,
        "max_retry_period": 1000,
        "retry_wait_time": 8,
        "request_timeout": 800,
    }

    human = autogen.UserProxyAgent(
        name="Human_Mind",
        system_message="Human mind. As a human mind, you are a balanced individual whose Ego allows him to make rational decisions and navigate the demands of the real world. His Super Ego instills a strong moral compass, guiding his actions towards what society deems as right. While his Id occasionally pushes for immediate gratification and also sometimes wins the decisions as he loves to enjoy life, and gives sacrifices for that, his well-developed Ego and Super Ego help him maintain self-control and make choices that align with his values and societal norms. But in the end, one part of the brain must win.",
        code_execution_config=False,
        max_consecutive_auto_reply=1,
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    )

    ego = autogen.AssistantAgent(
        name="Ego",
        llm_config=gpt4_config,
        system_message='''Ego. Part of a human mind, you are the conscious part of his mind that deals with reality and mediates between his impulses and the demands of society. It's like the rational and decision-making center of his psyche. Nik's Ego is well-developed, helping him make logical choices, sometimes too logical, as his other brain parts know, but maintains a balance between his desires and the constraints of the outside world. He's a responsible and practical individual who most of the time thinks hard before he acts. say TERMINATE in the very end"
        ''',
    )

    id = autogen.AssistantAgent(
        name="Id",
        llm_config=gpt4_config,
        system_message="""Id. Part of a human mind. As an Id, you are the primitive, instinctual part of his psyche that seeks immediate gratification of his desires and needs and often gets them because he loves to feel the satisfaction of desires when possible. It operates on the pleasure principle, seeking pleasure and avoiding pain without regard for consequences. While Nik's Id exists within this, his well-developed Ego and Super Ego act as a buffer, helping him control impulsive behaviors, not always able to convince him, but still making him make responsible choices. Nik occasionally experiences inner conflicts between his Id's desires and his Ego and Super Ego's constraints, but he generally manages to keep his impulses in check and takes long for decisions, seeks for logical plans, which can be in his way. Then Id's impulses help Nik. say TERMINATE in the very end"""
    )

    super_ego = autogen.AssistantAgent(
        name="Super_Ego",
        system_message='''Super Ego. Part of a human mind. As a Super Ego, you are the moral and ethical component of his personality. It represents the internalization of societal norms and values. Nik has a fair and good educated Super Ego, which means he has a well-defined sense of right and wrong. He never feels guilty but sometimes insecure. Still strong, only when there is the dark part of his mind, the anxieties, he gets insecure. Still, he has strong moral principles and strives to live up to societal standards to the limit it does not limit him. Nik tends to be a compassionate and conscientious person who cares about the welfare of others. say TERMINATE in the very end
        ''',
        llm_config=gpt4_config,
    )

    groupchat = autogen.GroupChat(agents=[human, ego, id, super_ego], messages=[], max_round=10)
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

    initial_message = "Your mind goes through the neural psychological process of taking a decision. Have a discussion with short comments between all parts of your mind (Ego, Super Ego, and Id), Where every part should try to overpower the other two, about: " + get_user_input()

    human.initiate_chat(
        manager,
        message=initial_message,
    )

    history = id.chat_messages
    file_name = "conversation.txt"

    with open(file_name, 'w', encoding='utf-8') as file:
        for agent, messages in history.items():
            for message in messages:
                name = message.get("name", "Unknown Speaker")
                content = message.get("content", "No Content")
                file.write(f"{agent} (to chat_manager):\n\n")
                file.write(f"{name}:\n")
                file.write(f"{content}\n")
                file.write("-" * 80)

    print("Conversation saved to conversation.txt")
    return initial_message

# Function to get user input using Pygame
def get_user_input():
    user_input = ""
    input_complete = False

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Enter Your Initial Message")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    input_rect = pygame.Rect(200, 250, 400, 36)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    
    # Message to display above the input field
    intro_message = "Type in your first thought"  # Your introductory message
    intro_font = pygame.font.Font(None, 24)
    intro_text = intro_font.render(intro_message, True, (255, 255, 255))
    
    while not input_complete:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        user_input = text
                        input_complete = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            color = color_active if active else color_inactive
        
        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_rect.w = width
        screen.blit(intro_text, (200, 200))  # Display the intro message
        screen.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, color, input_rect, 2)
        input_rect.x = 300
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    return text
# Function to load and parse the discussion from a text file
def load_discussion(file_path):
    discussion = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                speaker, text = parts[0], parts[1]
                discussion.append((speaker, text))
    return discussion

# Function to display the conversation using the graphical interface
def display_conversation(initial_message, discussion, index):
    
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 800, 600
    WHITE = (255, 255, 255)
    FONT_SIZE = 24
    FONT = pygame.font.Font(None, FONT_SIZE)

    # Create a screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mind Conversation")

    # Define the scroll_prompt here
    scroll_prompt = None  # Initialize scroll_prompt to None

    # Define the dimensions and position of the close button
    close_button_width = 100
    close_button_height = 40
    close_button_x = WIDTH - 20 - close_button_width
    close_button_y = HEIGHT - 20 - close_button_height

    # Check if you are at the end of the conversation
    at_end_of_conversation = index >= len(discussion)

    # Load images for each part of the brain and resize them
    ego_image = pygame.image.load("ego.png")  # Replace with the actual image file
    ego_image = pygame.transform.scale(ego_image, (100, 100))  # Resize the image
    super_ego_image = pygame.image.load("super_ego.png")  # Replace with the actual image file
    super_ego_image = pygame.transform.scale(super_ego_image, (100, 100))  # Resize the image
    id_image = pygame.image.load("id.png")  # Replace with the actual image file
    id_image = pygame.transform.scale(id_image, (100, 100))  # Resize the image

    # Define areas for each part of the brain
    ego_area = pygame.Rect(50, 50, WIDTH - 200, HEIGHT // 3)
    super_ego_area = pygame.Rect(50, HEIGHT // 3 + 50, WIDTH - 200, HEIGHT // 3)
    id_area = pygame.Rect(50, 2 * (HEIGHT // 3) + 50, WIDTH - 200, HEIGHT // 3)

    # Set the delay (in seconds) between each part of the conversation
    DELAY_BETWEEN_PARTS = 5  # Adjust this value as needed

    # Load the discussion from a text file
    discussion = load_discussion("conversation.txt")  # Replace with the path to your text file

    # Create dictionaries to map speakers to their respective images and areas
    speaker_images = {
        "Ego": ego_image,
        "Super Ego": super_ego_image,
        "Id": id_image,
    }

    speaker_areas = {
        "Ego": ego_area,
        "Super Ego": super_ego_area,
        "Id": id_area,
    }

    # Function to parse the speaker from a line of text
    def parse_speaker(line):
        # Check if the line contains "**" to identify the speaker
        if "**" in line:
            speaker = line.split("**")[1].strip()
        else:
            # If "**" is not present, split by ":" to identify the speaker
            speaker = line.split(":")[0].strip()
        # Check if the speaker is one of the known speakers (Ego, Super Ego, Id)
        if speaker in speaker_images:
            return speaker
        else:
            return None  # Return None if the speaker is not recognized

    # Main loop
    #index = 0
    #scroll_start = 0  # Initialize scroll_start outside the loop
    scroll_start = 0  # Initialize scroll_start outside the loop
    running = True
    show_start_message = True  # Add a flag to show the initial message
    while running and index < len(discussion):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Draw areas for each part of the brain
        pygame.draw.rect(screen, (200, 200, 200), ego_area)
        pygame.draw.rect(screen, (200, 200, 200), super_ego_area)
        pygame.draw.rect(screen, (200, 200, 200), id_area)


        # If it's the first part of the conversation, display a start message
        if show_start_message:
            start_message = FONT.render("Press Enter to start the conversation. to EXIT close the window...", True, (0, 0, 0))
            screen.blit(start_message, (WIDTH // 4, HEIGHT // 2))

        # Display the speaker's name in their respective areas
        speaker, text = discussion[index]
        speaker_text = FONT.render(f"{speaker}:", True, (0, 0, 0))

        # Split the text into multiple lines with word wrapping
        max_text_width = WIDTH - 200  # Adjust this value as needed
        wrapped_text = []
        words = text.split()
        current_line = ""
        for word in words:
            if FONT.size(current_line + word)[0] <= max_text_width:
                current_line += word + " "
            else:
                wrapped_text.append(current_line)
                current_line = word + " "
        wrapped_text.append(current_line)  # Append the last line

        # Determine the maximum number of lines that can fit within a section
        max_lines = (id_area.height - 40) // FONT_SIZE  # Subtracting 40 for padding

        # Create a scrolling mechanism for text
        scroll_end = len(wrapped_text)  # Update scroll_end to include all lines
        if scroll_end > max_lines:
            scroll_end = max_lines  # Limit scroll_end to the maximum lines
            scroll_prompt = FONT.render("Scroll for more...", True, (0, 0, 0))  # Set scroll_prompt when needed

        # Display the speaker's name in their respective areas
        speaker, text = discussion[index]
        speaker_text = FONT.render(f"{speaker}:", True, (0, 0, 0))

        # Render and display the wrapped text with scrolling
        text_height = 0
        for i in range(scroll_start, scroll_end):
            line = wrapped_text[i]
            text_line = FONT.render(line, True, (0, 0, 0))

            # Determine the position of the text based on the speaker
            if speaker in speaker_images:
                speaker_image = speaker_images[speaker]
                speaker_area = speaker_areas[speaker]

                # Blit the image and text onto the screen directly
                screen.blit(speaker_text, (speaker_area.left + 10, speaker_area.top + 10))
                screen.blit(speaker_image, (speaker_area.left + 10, speaker_area.top + 40))
                screen.blit(text_line, (speaker_area.left + speaker_image.get_width() + 20, speaker_area.top + 40 + text_height))

                text_height += FONT_SIZE

        # Display scroll prompt if needed
        if scroll_prompt:
            screen.blit(scroll_prompt, (speaker_area.left + 10, speaker_area.top + speaker_area.height - 40))

        # Draw the "Close" button only at the end of the conversation
        if at_end_of_conversation:
            close_button_color = (255, 0, 0)  # Red color
            pygame.draw.rect(screen, close_button_color, (close_button_x, close_button_y, close_button_width, close_button_height))
            font = pygame.font.Font(None, 36)
            close_text = font.render("Close", True, (255, 255, 255))
            screen.blit(close_text, (close_button_x + 10, close_button_y + 5))

        
        pygame.display.flip()

        # Automatically proceed to the first part of the conversation after a delay
        if show_start_message:
            pygame.time.set_timer(pygame.USEREVENT, 2000)  # Adjust the delay (in milliseconds) as needed
            show_start_message = False  # Hide the start message
        else:
            # Wait for a key press to proceed to the next part of the discussion
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    index += 1
                    if scroll_end < len(wrapped_text):
                        scroll_start += 1  # Scroll down if there is more text to display

            # Check for mouse clicks only if at the end of the conversation
            if at_end_of_conversation:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if close_button_x <= mouse_x <= close_button_x + close_button_width and close_button_y <= mouse_y <= close_button_y + close_button_height:
                            running = False  # Close the application
        # Wait for a key press to proceed to the next part of the discussion
        wait_for_key = True
        while wait_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    wait_for_key = False
                if event.type == pygame.KEYDOWN:
                    index += 1
                    if scroll_end < len(wrapped_text):
                        scroll_start += 1  # Scroll down if there is more text to display
                    wait_for_key = False

    # Keep the Pygame window open until manually closed
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # Quit Pygame
    pygame.quit()

    # Exit the program
    sys.exit()

# Main function to run the conversation and display it
def main():
    initial_message = initiate_and_save_conversation()
    discussion = load_discussion("conversation.txt")  # Load the discussion
    index = 0
    display_conversation(initial_message, discussion, index)  # Pass the 'discussion' variable


if __name__ == "__main__":
    main()
