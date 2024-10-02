import praw


reddit = praw.Reddit("coomer", user_agent="Dr. Coomer Bot")

# New PRAW devs: Please replace "Dr. Coomer bot" with a different string of your choice
# This helps prevent API errors and will probably also prevent me from being banned.

subreddit = reddit.subreddit("Coomerbottesting")

prefix = "bm:"
botNotice = "\n>!  \n" \
            "     I am a bot\n"\
            "!<"

for comment in subreddit.stream.comments():

    if prefix in comment.body:
        def checkDatabase():
            database = open("commentdatabase.txt")
            for line in database:
                if line == comment.id + "\n":
                    return("True")
                else:
                    pass

        doNotComment = checkDatabase()

        if doNotComment != "True":
            with open("commentdatabase.txt", "a") as database:
                database.write(comment.id + "\n")
            command = comment.body
            action = command.replace(prefix, "")
            if action == "hello":
                comment.reply("hello\n" + botNotice)
                print("Replied hello to a comment | ID: " +  comment.id)
            else:
                pass

