


# import os
# import re
# import matplotlib.pyplot as plt
# import xlsxwriter
# import pandas as pd

# # Define the directory where the files are stored
# #directory = 'F:/BE_EXTC_Grp9_3April2023/out_data/weights/generator'
# directory = 'E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/generator'
# # Get a list of all files in the directory
# files = os.listdir(directory)

# # Use regular expressions to extract the values of a and b from each file name
# a_values = []
# b_values = []
# for filename in files:
#     match = re.match(r'epoch(\d+)_loss(\d+\.\d+)', filename)
#     if match:
#         a_values.append(int(match.group(1)))
#         b_values.append(float(match.group(2)))

# # Create a scatter plot of epochs vs loss
# plt.plot(a_values, b_values)
# plt.xlabel('epochs')
# plt.ylabel('loss')
# plt.title('Generator')

# xticks = []
# for i in range(1600, 2000, 100):
#     xticks.append(i)
# plt.xticks(xticks)
# plt.show()

# # # Save values to Excel sheet using XlsxWriter
# # try:
# #     workbook = xlsxwriter.Workbook('generator_data.xlsx')
# #     worksheet = workbook.add_worksheet()
# #     worksheet.write_row(0, 0, ['Epochs', 'Loss'])
# #     for i in range(len(a_values)):
# #         worksheet.write_row(i + 1, 0, [a_values[i], b_values[i]])
# #     workbook.close()
# #     print("Values saved to generator_data.xlsx")
# # except Exception as e:
# #     print("Error saving values to Excel: {}".format(e))

# try:
#     workbook = xlsxwriter.open_workbook('generator_data.xlsx')
#     worksheet = workbook.add_worksheet()
#     row = worksheet.dim_rowmax()
#     worksheet.write_row(row + 1, 0, ['Epochs', 'Loss'])
#     for i in range(len(a_values)):
#         worksheet.write_row(row + i + 2, 0, [a_values[i], b_values[i]])
#     workbook.close()
#     print("Values appended to generator_data.xlsx")
# except Exception as e:
#     print("Error appending values to Excel: {}".format(e))

import os
import re
import matplotlib.pyplot as plt
import pandas as pd

# Define the directory where the files are stored
directory = 'E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/generator'

# Get a list of all files in the directory
files = os.listdir(directory)

# Use regular expressions to extract the values of a and b from each file name
a_values = []
b_values = []
for filename in files:
    match = re.match(r'epoch(\d+)_loss(\d+\.\d+)', filename)
    if match:
        a_values.append(int(match.group(1)))
        b_values.append(float(match.group(2)))

# Create a scatter plot of epochs vs loss
plt.plot(a_values, b_values)
plt.xlabel('epochs')
plt.ylabel('loss')
plt.title('Generator')

xticks = []
for i in range(1600, 2000, 100):
    xticks.append(i)
plt.xticks(xticks)
plt.show()

# Append values to existing Excel sheet using pandas and XlsxWriter
try:
    # Load existing data from Excel sheet to a DataFrame
    df = pd.read_excel('generator_data.xlsx')
    
    # Create a new DataFrame with the new values
    new_data = pd.DataFrame({'Epochs': a_values, 'Loss': b_values})
    
    # Append the new data to the existing data
    df = df.append(new_data, ignore_index=True)
    
    # Write the updated data to the Excel sheet
    writer = pd.ExcelWriter('generator_data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    print("Values appended to generator_data.xlsx")
except Exception as e:
    print("Error appending values to Excel: {}".format(e))