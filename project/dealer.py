# dealer_ai.py
import threading
import pyttsx3
from anthropic import Anthropic
from settings import VOICE_SPEED
from enums import Result

class Dealer:
    def __init__(self):
        self.client = Anthropic()
        self.tts_engine = pyttsx3.init()
        
        voices = self.tts_engine.getProperty('voices')
        for voice in voices:
            if 'en' in voice.languages or 'english' in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break
        self.tts_engine.setProperty('rate', VOICE_SPEED)
        self.ai_said_game_over = False

    def _speak(self, text):
        engine = pyttsx3.init()
        voices = self.tts_engine.getProperty('voices')
        for voice in voices:
            if 'en' in voice.languages or 'english' in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break
        engine.setProperty('rate', VOICE_SPEED)
        engine.say(text)
        engine.runAndWait()

    def generate_and_speak_taunt(self, player_hand, dealer_hand, player_score, dealer_score, status):
        if status in {result.name for result in Result}:
            if self.ai_said_game_over:
                return
            else:
                self.ai_said_game_over = True
        thread = threading.Thread(target=self._process_ai_speech, args=(player_hand, dealer_hand, player_score, dealer_score, status))
        thread.daemon = True
        thread.start()

    def _process_ai_speech(self, player_hand, dealer_hand, player_score, dealer_score, status):
        try:
            player_cards = ''
            for card in player_hand:
                player_cards += card.text + ', '
            dealer_cards = ''
            for card in dealer_hand:
                dealer_cards += card.text + ', '
            prompt = (
                f'You are a sarcastic, manipulative casino Blackjack dealer. Your absolute goal is to '
                f'make the player nervous and psychologically trick them into making a bad move (e.g., '
                f'mocking them if they stand on a low score, or baiting them to hit when they are already at 18). '
                f'Keep your response extremely short (maximum 1 or 2 short sentences) and speak in English. '
                f'You can see your hand here {dealer_cards} and player has the following cards {player_cards}'
                f'Current situation: The player has {player_score} points. You (the dealer) have {dealer_score} points showing. '
                f'The exact game event triggering this is: {status}.'
                f'Keep your andwer shorter than 140 chars and use only letters and numbers. No emojis or symbols.'
            )

            message = self.client.messages.create(
                model='claude-sonnet-4-6',
                max_tokens=60,
                temperature=0.85,
                system='You are a witty, mean Las Vegas blackjack dealer. Speak short, sharp sentences.',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            
            ai_response = message.content[0].text
            print(f"Dealer says: {ai_response}")
            self._speak(ai_response)

        except Exception as e:
            print(f"AI Dealer error: {e}")