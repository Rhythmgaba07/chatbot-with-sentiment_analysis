# main.py
from src.chatbot import Chatbot

def main():
    bot = Chatbot(model_name="vader")
    print("🤖 Liapus AI Chatbot | Sentiment-Aware")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ("exit", "quit", "bye"):
            print("Bot: Goodbye! Take care.")
            break

        response, sentiment = bot.reply(user_input)
        print(f"Bot: {response}")
        print(f"[Sentiment] Label: {sentiment['label']}  Score: {sentiment['compound']:.3f}\n")


    # After chat session, show mood analysis
    print("\n📊 Conversation Summary:")
    summary = bot.finalize_conversation_report()
    print(f"Overall Sentiment: {summary['overall_sentiment']['label']}  "
      f"Score: {summary['overall_sentiment']['compound']:.3f}")

    print(f"Mood Trend: {summary['mood_trend']}")

if __name__ == "__main__":
    main()
