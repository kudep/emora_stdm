
from emora_stdm import DialogueFlow

chatbot = DialogueFlow('start')
transitions = {
    'state': 'start',
    '"Hello. How are you?"': {
        '[{good, okay, fine, ok}]': {
            '"Good. I am doing well too."': {
                'error': {
                    '"See you later!"': 'end'
                }
            }
        },
        'error': {
            '"Well I hope your day gets better!"': {
                'error': {
                    '"Bye!"': 'end'
                }
            }
        }
    }
}
chatbot.load_transitions(transitions)

if __name__ == '__main__':
    chatbot.run()