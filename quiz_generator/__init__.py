from quiz_generator.ascii import ASCIIReader, ASCIIWriter
from quiz_generator.core.pool import QuestionPool
from quiz_generator.generator import QuizGenerator
from quiz_generator.io import IOReader, IOWriter

if __name__ == '__main__':
    questions_filepath = input('Questions filepath: ')
    quiz_output_dir = input('Directory to generate handouts into: ')
    handout_count = int(input('Handouts: '))
    question_size = int(input('Questions per handout: '))

    reader: IOReader = ASCIIReader(questions_filepath)
    writer: IOWriter = ASCIIWriter(quiz_output_dir)

    pool: QuestionPool = QuestionPool(reader)

    quiz_generator = QuizGenerator(pool, question_size)

    writer.write_all(quiz_generator.generate_handouts(handout_count))
