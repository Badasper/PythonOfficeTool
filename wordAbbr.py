import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return " ".join(fullText).split(" ")


def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result


def abbrMaker(filename):
    fullText = getText(filename)
    abbrList = []
    for word in fullText:
        letterTemp = ""
        abbr = ""
        for letter in word:
            if "Я" >= letter >= "А":
                condA = "Я" >= letterTemp >= "А"
                condB = letterTemp in ["\"", "\u00AB", ""]
                if  condA or condB:
                    abbr += letter
                    if len(abbr) == len(word) and len(abbr) >= 2:
                        abbrList.append(abbr)
            else:
                if len(abbr) >= 2:
                    abbrList.append(abbr)
            letterTemp = letter
    abbrList = sorted(abbrList)
    return unique(abbrList)


print(abbrMaker("Test.docx"))
