import os
from PyInquirer import style_from_dict, Token, prompt

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'input',
        'name': 'BUILDKITEKEY',
        'message': 'What is your buildkite agent token?'
    },
    {
        'type': 'input',
        'name': 'SSH_FINGERPRINT',
        'message': 'What is your digital ocean ssh key fingerprint?'
    }
]

answers = prompt(questions, style=style)

homedir=os.path.expanduser('~')
os.makedirs(homedir + "/.my-scripts", mode=0o755, exist_ok=True)

with open("./buildkite_digitalocean/dobk-stop.sh") as src:
    with open(homedir + "/.my-scripts/dobk-stop", "w") as dest:
        dest.write(src.read())

with open("./buildkite_digitalocean/dobk-start.sh") as src:
    content = src.read()
    updatedContent = content.replace("INSERT_SSH_FINGERPRINT", answers['SSH_FINGERPRINT'])
    with open(homedir + "/.my-scripts/dobk-start", "w") as dest:
        dest.write(updatedContent)

with open("./buildkite_digitalocean/bk-config.yml") as src:
    content = src.read()
    updatedContent = content.replace("BUILDKITEKEY", answers['BUILDKITEKEY'])
    with open(homedir + "/.my-scripts/bk-config.yml", "w") as dest:
        dest.write(updatedContent)
        
os.chmod(homedir + "/.my-scripts/dobk-start", 0o755)
os.chmod(homedir + "/.my-scripts/dobk-stop", 0o755)