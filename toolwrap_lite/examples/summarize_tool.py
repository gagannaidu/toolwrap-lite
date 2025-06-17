from toolwrap_lite import tool, get_registered_tools, export_tools_to_json

@tool
def summarize_tweets(username: str, count: int = 5, language: str = "en") -> str:
    """
    Summarize the most recent tweets from a given Twitter username.
    """
    return f"Summary of {count} tweets by @{username} in {language}."

if __name__ == "__main__":
    tools = get_registered_tools()
    print(tools["summarize_tweets"]["schema"])
    export_tools_to_json()
