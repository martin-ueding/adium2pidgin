# adium2pidgin

Converts Adium XML chatlogs into Pidgin HTML chatlogs.

The logs are parsed into an intermediate structure of lists and dicts, so it can be saved as a simple JSON file to be reimported later on.

The JSON interface allows conversion between all logs formats, one just needs to write a parser from a specific format to JSON or a writer from JSON into some format.

## Parser

- Adium XML
- Purple HTML (in progress)

## Writer

- Purple HTML
- JSON
