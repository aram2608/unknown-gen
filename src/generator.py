import random
import pandas as pd  # type: ignore


class Generator:
    def generate_excel(self, gramp_list, gramn_list, sections, range_size, file_name):
        file_name = file_name + ".xlsx"
        try:
            # Initialize the ExcelWriter object using xlswriter
            # We use a context manager to create the writer object
            with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:

                # Loop through the 8 sections
                for i in range(1, sections + 1):
                    section_number = i
                    data_list = []  # Reset the list for each new section

                    # Determine range and section number
                    start_num = (i - 1) * range_size + 1
                    end_num = i * range_size
                    section_numbers = list(range(start_num, end_num + 1))

                    # We create an even distribution of bacteria
                    num_positive = range_size // 2  # 10
                    num_negative = range_size - num_positive  # 10

                    positive_selections = random.choices(gramp_list, k=num_positive)
                    negative_selections = random.choices(gramn_list, k=num_negative)
                    bacteria_selections = positive_selections + negative_selections

                    # Shuffle the combined list to mix Gram-pos and Gram-neg randomly
                    random.shuffle(bacteria_selections)

                    # We need to create each sections data
                    for j in range(range_size):
                        bacteria_name = bacteria_selections[j]
                        is_positive = bacteria_name in gramp_list
                        gram_stain = "Gram-Positive" if is_positive else "Gram-Negative"

                        data_list.append(
                            {
                                "Section": section_number,
                                "Number": section_numbers[j],
                                "Bacteria": bacteria_name,
                                "GramStain": gram_stain,
                            }
                        )

                    # Save df
                    df_section = pd.DataFrame(data_list)

                    # Define the sheet name (e.g., 'Section 1', 'Section 8')
                    sheet_name = f"Section {section_number}"

                    # Write the current section's DataFrame to the specified sheet
                    df_section.to_excel(writer, sheet_name=sheet_name, index=False)

                    print(
                        f"Created sheet: '{sheet_name}' with numbers {start_num}-{end_num}"
                    )

            print(f"All 8 sections saved to separate sheets in '{file_name}'")

        except Exception as e:
            print(f"An error occurred while saving to Excel: {e}")
