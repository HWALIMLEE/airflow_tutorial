import os
import click
from PyInquirer import prompt, Validator, ValidationError, style_from_dict, Token


class DagNameValidator(Validator):
    def validate(self, document):
        if len(document):
            return True
        else:
            raise ValidationError


style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


def ask_default_args():
    questions = [
        {
            'type': 'input',
            'name': 'dag_name',
            'message': 'dag name',
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'description',
            'default': ''
        },
        {
            'type': 'input',
            'name': 'owner',
            'message': 'owner',
            'default': 'hwalim'
        },
        {
            'type': 'input',
            'name': 'retries',
            'message': 'retries',
            'default': '3'
        },
        {
            'type': 'input',
            'name': 'retry_delay',
            'message': 'retry delay minutes',
            'default': '1'
        },
        {
            'type': 'input',
            'name': 'start_date',
            'message': 'start date (ex. 2023, 1, 1, 17, 30)',
            'default': '2023, 1, 1, 17, 30'
        },
        {
            'type': 'input',
            'name': 'schedule_interval',
            'message': 'schedule interval'
        },
        {
            'type': 'input',
            'name': 'catchup',
            'message': 'catchup',
            'default': 'False'
        },
        {
            'type': 'input',
            'name': 'tags',
            'message': 'tags',
            'default': 'etl'
        }
    ]
    default_args = prompt(questions, style=style)
    return default_args


def create_dag_file(conf):
    conf["catchup"] = conf.get("catchup") == "True"
    conf["tags"] = str(conf.get("tags").split(','))
    os.system(
        'bash '+os.path.join(os.path.dirname(os.path.abspath(__file__)), 'support.sh')+' "{dag_name}" "{owner}" "{retries}" "{retry_delay}" "{description}" "{schedule_interval}" "{start_date}" "{catchup}" "{tags}"'.format(**conf)
        )


@click.command()
def main():
    default_info = ask_default_args()
    create_dag_file(default_info)


if __name__ == '__main__':
    main()