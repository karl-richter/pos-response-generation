import spacy

nlp = spacy.load('en')

def skip_and_print(*args):
    """ Act like print(), but skip a line before printing. """
    print('\n' + str(args[0]), *args[1:])

def print_table(rows, padding=0):
    """ Print `rows` with content-based column widths. """
    col_widths = [
        max(len(str(value)) for value in col) + padding
        for col in zip(*rows)
    ]
    total_width = sum(col_widths) + len(col_widths) - 1
    fmt = ' '.join('%%-%ds' % width for width in col_widths)
    print(fmt % tuple(rows[0]))
    print('~' * total_width)
    for row in rows[1:]:
        print(fmt % tuple(row))


document_string = """
Where is my car parked?
"""

doc = nlp(document_string)


rows = [['Chunk', '.root', 'root.dep_', '.root.head']]
for chunk in doc.noun_chunks:
    rows.append([
        chunk,            # A Span object with the full phrase.
        chunk.root,       # The key Token within this phrase.
        chunk.root.dep_,  # The grammatical role of this phrase.
        chunk.root.head   # The grammatical parent Token.
    ])
print_table(rows, padding=4)

# Remove starting, ending, and duplicated whitespace characters.
document_string = ' '.join(document_string.split())

skip_and_print('Working with string: "%s"' % document_string)
doc = nlp(document_string)

# For each sentence, spacy identifies a root of the dependency
# tree. You can think of this as the grammatically most
# meaningful word in the sentence.

skip_and_print('Root word of each sentence:')
rows = [['Root', '|', 'Sentence']]
for sentence in doc.sents:
    rows.append([sentence.root, '|', sentence.text])
print_table(rows)