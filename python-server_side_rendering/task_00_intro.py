from string import Template
import os


def generate_invitations(template_content, attendees):

    if not isinstance(template_content, str):
        print("template must be a string")
        return
    if not isinstance(attendees, list):
        print("attendees must be a list")
        return
    if not all(isinstance(item, dict) for item in attendees):
        print("attendees must be a list of dictionaries")
        return

    if not template_content:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, dic in enumerate(attendees, start=1):
        output = template_content
        for key in ("name", "event_title", "event_date", "event_location"):
            value = dic.get(key)
            output = output.replace("{" + key + "}", "N/A" if value is None else str(value))
        try:
            with open(f"output_{i}.txt", 'w') as file:
                file.write(output)
        except OSError:
            print(f"could not write to output_{i}.txt")
            return
