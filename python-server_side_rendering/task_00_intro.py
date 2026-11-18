from string import Template
import os


def generate_invitations(template_content, attendees):

    if not isinstance(template_content, str):
        raise TypeError("template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("attendees must be a list")
    if not all(isinstance(item, dict) for item in attendees):
        raise TypeError("attendees must be a list of dictionaries")

    if not template_content:
        print("Template is empty, no output files generated.")
        raise SystemExit(1)

    if not attendees:
        print("No data provided, no output files generated.")
        raise SystemExit(1)

    i = 0
    for dic in attendees:
        i += 1
        output = template_content
        for key in ("name", "event_title", "event_date", "event_location"):
            value = dic.get(key)
            output = output.replace("{" + key + "}", "N/A" if value is None else str(value))
            try:
                with open(f"output_{i}.txt", 'w') as file:
                    file.write(output)
            except OSError:
                print(f"could not write to output_{i}.txt")
                raise SystemExit(1)
