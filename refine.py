from summarize import summarize
import openai

def fixer(urlArr, urlBase, summary):
    summariesNotGenerated = ["There is no information provided to summarize.",
                            "Loading is happening.",
                            "Website didn't allowed scrapping", 
                            "summary about a website",
                            "The server could not find the requested",
                            "The URL requested was not found on the server",
                            "The requested page",
                            "The requested resource is unavailable",
                            "The request was rejected due to administrative rules.",
                            """The phrase "Access denied" indicates""",
                            "JavaScript is required",
                            "JavaScript and cookies need to be enabled to continue.",
                            "The request for access was denied.",
                            "Error 404",
                            "The 403 error",
                            "Access denied",
                            "The page is not found",
                            "Access to the page",
                            "The website requires JavaScript and cookies to be enabled for page reload.",
                            "The request for access was denied.",
                            "The signal is unacceptable.",
                            "The website uses cookies for better user experience"]
    summary = summary.strip()
    for errors in summariesNotGenerated:
        if summary.lower().startswith(errors.lower()):
            # print("URL: ", "/".join(urlArr[:3]), " ", errors)
            summary = summarize("/".join(urlArr[:3]))
            break
    summary = summary.strip()
    for errors in summariesNotGenerated:
        if summary.lower().startswith(errors.lower()):
            # print("URL: ", urlBase, " ", errors)
            summary = summarize(urlBase)
            break
    summary = summary.strip()
    for errors in summariesNotGenerated:
        if summary.lower().startswith(errors.lower()):
            # print("URL by openai: ", "/".join(urlArr), " ", errors)
            response = openai.chat.completions.create(
                model = "gpt-3.5-turbo-16k",
                messages = [
                    {"role" : "user", "content": f"What can you tell about the page this url is directing by understanding url in 50 words: {"/".join(urlArr)}"}
                ],
                temperature=0.1,
                max_tokens=512,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            summary = response.choices[0].message.content
            break
    return summary