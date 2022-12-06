# This solution was created by chat.openai.com. OpenAI Assistant. (2022, December 6)

def find_first_marker(datastream: str, marker_length: int) -> int:
    # Keep track of the last marker_length characters we've seen
    last_chars = []
    for i, c in enumerate(datastream):
        # Add the current character to the list of the last marker_length characters
        last_chars.append(c)
        # If the list of the last marker_length characters is longer than marker_length, remove the oldest character
        if len(last_chars) > marker_length:
            last_chars.pop(0)
        # If the last marker_length characters are all distinct, we have found the start-of-packet marker
        if len(set(last_chars)) == marker_length:
            # Return the index of the first character in the marker (which is one greater than the index of the last character)
            return i + 1
    # If we reach the end of the datastream without finding a marker, return -1
    return -1


# Open the file in read mode and read its contents
with open("input.txt", "r") as f:
    datastream = f.read()

# Remove leading and trailing whitespace from the input string
datastream = datastream.strip()

marker_length = 4
first_marker_index = find_first_marker(datastream, marker_length)
print(first_marker_index)
marker_length = 14
first_marker_index = find_first_marker(datastream, marker_length)
print(first_marker_index)
