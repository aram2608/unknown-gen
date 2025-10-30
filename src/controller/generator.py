import random
import pandas as pd  # type: ignore
from typing import List


def generate_excel(
    gramp_list: List[str],
    gramn_list: List[str],
    sections: int,
    range_size: int,
    file_name: str,
):
    # We append the proper extension to the string
    file_name += ".xlsx"
    # We run this in a try block to catch any exceptions
    try:
        # We initialize the ExcelWriter object using xlswriter
        # We use a context manager to create the writer object
        with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:

            # Loop through the 8 sections
            for i in range(1, sections + 1):
                section_number = i
                # We initialize an empty list to store our data
                # Reset the list for each new section
                data_list = []

                # Determine range and section number
                start_num = (i - 1) * range_size + 1
                end_num = i * range_size
                section_numbers = list(range(start_num, end_num + 1))

                # We create an even distribution of bacteria
                num_positive = range_size // 2  # 10
                num_negative = range_size - num_positive  # 10

                # We can now select random choices of bacteria from the gram
                # positive and negative bacteria
                positive_selections = random.choices(gramp_list, k=num_positive)
                negative_selections = random.choices(gramn_list, k=num_negative)
                # We combine the selections into one master combination
                bacteria_selections = positive_selections + negative_selections

                # We can now shuffle the combined list to mix Gram-pos and Gram-neg randomly
                random.shuffle(bacteria_selections)

                # We need to create each sections data
                # We loop the range_size (ie class size)
                for j in range(range_size):
                    # We index oout the bacteria
                    bacteria_name = bacteria_selections[j]
                    # We create a boolean value determining the gram class
                    # We need to do this since Python does not have a ternary operator
                    gram_stain = (
                        "Gram-Positive"
                        if bacteria_name in gramp_list
                        else "Gram-Negative"
                    )

                    # We can now append a dictionary of all the data to our list
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

                # We now define the sheet name (ie, 'Section 1', 'Section 8')
                sheet_name = f"Section {section_number}"

                # We can now write the current section's DataFrame to the specified sheet
                df_section.to_excel(writer, sheet_name=sheet_name, index=False)
        # If our run was successful we return true
        return True
    except Exception as e:
        # If it failed we return false
        return False
