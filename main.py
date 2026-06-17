from test_cases import TEST_CASES
from prompt_template import COT_PROMPT
from ollama_client import generate_response
from utils import create_output_folder
from utils import save_output


def run_test_case(question, index):

    prompt = COT_PROMPT.format(
        question=question
    )

    print("\n")
    print("=" * 80)
    print(f"TEST CASE {index}")
    print("=" * 80)

    print("\nQUESTION:")
    print(question)

    print("\nGenerating reasoning...\n")

    result = generate_response(prompt)

    print(result)

    output_file = f"outputs/output_{index}.txt"

    save_output(
        output_file,
        result
    )

    print(f"\nSaved -> {output_file}")


def main():

    create_output_folder()

    for index, question in enumerate(
        TEST_CASES,
        start=1
    ):

        run_test_case(
            question,
            index
        )

    print("\n")
    print("=" * 80)
    print("PROJECT EXECUTION COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    main()