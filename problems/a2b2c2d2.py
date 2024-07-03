# def compress_string(input_str):
#     if not input_str:
#         return ""
#
#     compressed_str = ""
#     current_char = input_str[0]
#     count = 1
#
#     for i in range(1, len(input_str)):
#         if input_str[i] == current_char:
#             count += 1
#         else:
#             compressed_str += current_char + str(count)
#             current_char = input_str[i]
#             count = 1
#
#     # Append the last character and its count
#     compressed_str += current_char + str(count)
#
#     return compressed_str
#
#
# # Example usage:
# input_str = "aabbcccdd"
# compressed_output = compress_string(input_str)
# print(compressed_output)




