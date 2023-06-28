import guidance

guidance.llm = guidance.llms.OpenAI("text-davinci-003")


def execute_program():
    """Basic templating [2] ~ [4]"""
    program = guidance("""what is {{example}}?""")
    print(program)

    executed_program = program(example="truth")
    print(executed_program)

    print(executed_program["example"])


def lists_and_objects():
    """Basic templating [5] ~ [6]"""
    people = ["John", "Mary", "Bob", "Alice"]
    ideas = [
        {"name": "truth", "description": "the state of being the case"},
        {"name": "love", "description": "a strong feeling of affection"},
    ]

    program = guidance(
        """List of people:
{{#each people}} - {{this}}
{{~! This is a comment.}}
{{~! The ~ removes adjacent whitespace either before of after a tag,}}
{{~! depending on where you place it}}
{{/each~}}
List of ideas:
{{#each ideas}}{{this.name}}: {{this.description}}
{{/each}}"""
    )

    print(program(people=people, ideas=ideas))


def include_program():
    people = ["John", "Mary", "Bob", "Alice"]
    ideas = [
        {"name": "truth", "description": "the state of being the case"},
        {"name": "love", "description": "a strong feeling of affection"},
    ]

    program1 = guidance(
        """List of people:
{{#each people}} - {{this}}
{{/each~}}"""
    )

    program2 = guidance(
        """{{>program1}}
List of ideas:
{{#each ideas}}{{this.name}}: {{this.description}}
{{/each}}"""
    )

    print(program2(program1=program1, people=people, ideas=ideas))


if __name__ == "__main__":
    # execute_program()
    # lists_and_objects()
    include_program()
