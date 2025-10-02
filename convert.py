import csv

def convert_to_csv(input_file="x.txt", output_file="anki.csv"):
    pairs = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                word, synonyms = line.split("\t")
            except ValueError:
                parts = line.split(maxsplit=1)
                if len(parts) < 2:
                    continue
                word, synonyms = parts

            for synonym in synonyms.split(";"):
                synonym = synonym.strip()
                if synonym:
                    pairs.append((synonym, word))

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(pairs)

    print(f"Done! Saved {len(pairs)} cards to {output_file}")

if __name__ == "__main__":
    convert_to_csv()
