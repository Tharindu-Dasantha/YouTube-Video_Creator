# taking the idea file and removing new lines and adding "."s

ideafile = open("Finalized_Ideas/Idea.txt", "r")
lines = ideafile.readlines()
newText = ""
for line in lines:
    line = line.strip()
    newText += (". "+line)
    
newText = newText.lstrip(".")
newText = newText + "."
    
writingfile = open("Finalized_Ideas/FinalIdea.txt", "w")
writingfile.write(f"{newText}")