def generate_html(title, content):
    html_text_1 = '''
	<div class="lesson">
    <div class="title">
        ''' + title
    html_text_2 = '''
    </div>
    <div class="content">
    <p>''' + content
    html_text_3 = '''
	</p>
    </div>
	</div>'''
    
    full_html = html_text1 + html_text2 + html_text3
    return full_html

def get_title(lesson):
    start_location = lesson.find('TITLE:')
    end_location = lesson.find('DESCRIPTION:')
    title = lesson[start_location+7 : end_location-1]
    return title

def get_description(lesson):
    start_location = lesson.find('DESCRIPTION:')
    description = lesson[start_location+13 :]
    return content

def get_lesson_by_number(text, lesson_number):
    counter = 0
    while counter < lesson_number:
        counter = counter + 1
        next_lesson_start = text.find('TITLE:')
        next_lesson_end = text.find('TITLE:', next_lesson_start + 1)
        if next_lesson_end >= 0:
            lesson = text[next_lesson_start:next_lesson_end]
        else:
            next_lesson_end = len(text)
            lesson = text[next_lesson_start:]
        text = text[next_lesson_end:]
    return lesson

TEXT = """LESSON:Introduction to Serious Programming
TITLE: Computer
DESCRIPTION: The power of the computer is to do anything. It is a 
universal machine that we can program to do essential computation.
TITLE: Computer Program
DESCRIPTION: A computer program, or just a program, is a sequence 
of instructions, written to perform a specified task on a computer.  
Some examples of computer programs are web browsers, games, mobile apps,  
and simple print statements.
TITLE: Programming Language
DESCRIPTION: A programming language is a formal constructed 
language designed to  communicate instructions to a machine, particularly  
a computer. Python is one example of a programming language.
TITLE: Grammar
DESCRIPTION: Why do we need to invent new languages like Python to program  
computers, rather than natural languages like English or Mandarin? 
One reason is.. ambiguity! In order to learn about computer programming, 
we have to learn new languange.Python has a grammar - the way we're writing 
grammar in Python is called "notation". BNF (Backus-Naur Form) is one of the  
notation techniques for context-free grammars, often used to describe the syntax 
of languages used in computing.
TITLE: Python Expressions
DESCRIPTION: A Python "expression" is a legal Python statement. For example: 
print 1 + 1 is a valid expression, but print 1 + without a number 
at the end) is not."""


def generate_all_html(text):
    current_lesson_number = 1
    lesson = get_lesson_by_number(text, current_lesson_number)
    all_html = ''
    while lesson != '':
        title = get_title(lesson)
        content = get_description(lesson)
        lesson_html = generate_html(title, content)
        all_html = all_html + lesson_html
        current_lesson_number = current_lesson_number + 1
        lesson = get_lesson_by_number(text, current_lesson_number)
    return all_html


print generate_all_html(TEXT)
