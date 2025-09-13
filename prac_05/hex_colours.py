COLOR_CODES_NAME={"cornsilk1":"#fff8dc",
                  "cornsilk2":"#eee8cd",
                  "cornsilk3":"#cdc8b1",
                  "cornsilk4":"#8b8878",
                  "cosmic Cobalt":"#2e2d88",
                  "cosmic Latte":"#fff8e7",
                  "cotton Candy":"#ffbcd9",
                  "cream":"#fffdd0",
                  "crimson":"#dc143c",
                  "crystal":"#a7d8de"
}

def main():
    """ acquire the color name and jude which is in the dictionary"""
    color_name=input("Enter the color name:").strip().lower()
    while color_name!="":
         if color_name in COLOR_CODES_NAME:
             print(f"The color is {color_name} and the code is {COLOR_CODES_NAME[color_name]}")
         else:
             print(f"sorry, your color code {color_name} is invalid ")
         color_name=input("Enter the color name:").strip().lower()
main()