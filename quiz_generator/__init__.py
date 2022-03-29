from quiz_generator.ascii_io import ASCIIReader, ASCIIWriter
from quiz_generator.core.handout import Handout
from quiz_generator.core.pool import QuestionPool
from quiz_generator.generator import QuizGenerator
from quiz_generator.io import IOReader, IOWriter
from quiz_generator.json_io.json_writer import JSONWriter

if __name__ == '__main__':
    questions_filepath = input('Questions filepath: ')
    quiz_output_dir = input('Directory to generate handouts into: ')
    # handout_count = int(input('Handouts: '))
    # question_size = int(input('Questions per handout: '))

    reader: IOReader = ASCIIReader(questions_filepath)
    writer: IOWriter = JSONWriter(quiz_output_dir)

    writer.write(Handout(reader.get()))

    # pool: QuestionPool = QuestionPool(reader)

    # quiz_generator = QuizGenerator(pool, question_size)

    # handouts = quiz_generator.generate_handouts(handout_count)
    # writer.write_all(handouts)
