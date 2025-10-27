import random
import pandas as pd # type: ignore

# Convert Enums to lists of string names
gram_positive_list = ["S Aureus", "S epidermidis", "A agalactiae", "E faecalis"]
gram_negative_list = ["E coli", "S marscecens", "P aeurginosa", "S enterica", "S flexneri"]

SECTIONS = 8
RANGE_SIZE = 20 # Each section has 20 numbers
excel_filename = 'microbes_fall_2025_unknowns.xlsx'

# Initialize the ExcelWriter object
# 'engine='xlsxwriter'' is often recommended for better performance and features
try:
    with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
        
        # Loop through the 8 sections
        for i in range(1, SECTIONS + 1):
            section_number = i
            data_list = [] # Reset the list for each new section
            
            # --- 1. Determine Range and Numbers ---
            start_num = (i - 1) * RANGE_SIZE + 1
            end_num = i * RANGE_SIZE
            section_numbers = list(range(start_num, end_num + 1))
            
            # --- 2. Calculate and Select Bacteria (Even Distribution) ---
            num_positive = RANGE_SIZE // 2 # 10
            num_negative = RANGE_SIZE - num_positive # 10

            positive_selections = random.choices(gram_positive_list, k=num_positive)
            negative_selections = random.choices(gram_negative_list, k=num_negative)
            bacteria_selections = positive_selections + negative_selections
            
            # Shuffle the combined list to mix Gram-pos and Gram-neg randomly
            random.shuffle(bacteria_selections)
            
            # --- 3. Create Section Data ---
            for j in range(RANGE_SIZE):
                bacteria_name = bacteria_selections[j]
                is_positive = bacteria_name in gram_positive_list
                gram_stain = "Gram-Positive" if is_positive else "Gram-Negative"
                
                data_list.append({
                    'Section': section_number,
                    'Number': section_numbers[j],
                    'Bacteria': bacteria_name,
                    'GramStain': gram_stain
                })

            # --- 4. Create and Write DataFrame to a Sheet ---
            df_section = pd.DataFrame(data_list)
            
            # Define the sheet name (e.g., 'Section 1', 'Section 8')
            sheet_name = f'Section {section_number}'
            
            # Write the current section's DataFrame to the specified sheet
            df_section.to_excel(writer, sheet_name=sheet_name, index=False)
            
            print(f"Created sheet: '{sheet_name}' with numbers {start_num}-{end_num}")

    print(f"\n--- SUCCESS ---")
    print(f"All 8 sections saved to separate sheets in '{excel_filename}'")

except Exception as e:
    print(f"\n--- ERROR ---")
    print(f"An error occurred while saving to Excel: {e}")