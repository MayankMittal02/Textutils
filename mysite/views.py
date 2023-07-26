from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("hello")
    return render(request, "index.html")


def remove_punc(s: str) -> str:
    # return HttpResponse("remove punc")
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    ans = ""
    for c in s:
        if c not in punctuations:
            ans = ans + c
    return ans


def capitalize(s: str) -> str:
    s = s.upper()
    return s


def space_remover(s: str) -> str:
    # s.replace("  ", "a")
    # return s

    s2 = ""
    if s[0] != " ":
        s2 = s2 + s[0]
    n = len(s)
    for i in range(1, n):
        if s[i] == " " and s[i - 1] == " ":
            continue
        else:
            s2 = s2 + s[i]
    s2 = s2[::-1]
    s2 = s2.replace(" ", "", 1)
    s2 = s2[::-1]
    return s2


def nl_remover(s: str) -> str:
    s = s.replace("\n", "")
    return s


def char_count(s: str) -> int:
    a = len(s)
    return a


def check_brackets(s: str) -> bool:
    stack = []
    for c in s:
        if c == "{" or c == "(" or c == "[":
            stack.append(c)

        elif c == ")" or c == "}" or c == "]":
            if len(stack) == 0:
                return False

            elif c == ")" and stack.pop() != "(":
                return False
            elif c == "}" and stack.pop() != "{":
                return False
            elif c == "]" and stack.pop() != "[":
                return False
    if len(stack) != 0:
        return False
    return True


def check_grammar(s: str) -> str:
    s2 = "this feature is comming soon"
    return s2


def analyze(request):
    removepunc = request.GET.get("removepunc", "off")
    cap = request.GET.get("capitalise", "off")
    nlremove = request.GET.get("newlineremove", "off")
    spaceremove = request.GET.get("spaceremove", "off")
    charcount = request.GET.get("charcount", "off")
    text = request.GET.get("data", "default")
    checkbrackets = request.GET.get("checkbrackets", "off")
    checkgrammer = request.GET.get("checkgrammar", "off")

    Dict = {"finaltext": text, "tc": ""}
    che = ""
    text2 = text

    if removepunc == "on":
        text2 = remove_punc(text)

    if cap == "on":
        text2 = capitalize(text2)

    if spaceremove == "on":
        text2 = space_remover(text2)

    if nlremove == "on":
        # text = nl_remover(text)
        text2 = text2.replace("\n", "1")

    if checkbrackets == "on":
        if check_brackets(text2) == True:
            che = "brackets matched\n"
        else:
            che = "brackets mismatched\n"

    if charcount == "on":
        che = che + "your character count is " + str(char_count(text2)) + "\n"
    if checkgrammer == "on":
        che = che + check_grammar(text2)
    Dict["finaltext"] = text2
    Dict["tc"] = che
    Dict["originaltext"] = text

    return render(request, "ans.html", Dict)
