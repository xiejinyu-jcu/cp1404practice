"""
wimbledon
Estimate: 35 minutes
Actual:  50 minutes
"""

def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_file(filename)
    champion_count, countries = process_data(data)
    display_result(champion_count, countries)


def read_wimbledon_file(filename):
    """read the file and extract the champion and country """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            data.append([champion, country])
    return data


def process_data(data):
  """return champion win counts and the countries list """
  champion_count = {}
  countries = set()
  for record in data:
      champion = record[0]
      country = record[1]
      if champion in champion_count:
          champion_count[champion] += 1
      else:
          champion_count[champion] = 1
      countries.add(country)
  return champion_count, sorted(countries)


def display_result(champion_count, countries):
    """Display champions and countries"""
    print("Wimbledon champions:")
    for name, count in champion_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))



main()