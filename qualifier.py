from typing import Any, List, Optional

def get_longest_str(lst : List[List[Any]], index: int) -> str:
    prod = []
    for row in lst:
        prod.append(str(row[index]))
    return max(prod, key=len)

def convert_all_to_str(lst: List[List[Any]]) -> list:
    for row_index, row in enumerate(lst):
        for item_index, item in enumerate(row):
            lst[row_index][item_index] = str(item)
    
    return lst

def get_longest_str_of_all_indexes(rows: List[List[Any]]) -> int:
    total: int = 0
    for item_index, item in enumerate(rows[0]):
        print(item_index, item)
        total += len(get_longest_str(rows, item_index))
            
    return total

def output_labels(labels: List[List[Any]], longest_str: int, centered: bool = False) -> str:
    return f" {labels[0]}{' '*(longest_str-len(labels[0])+1)}{Seps.vertical} \n"

def output_row(rows: List[List[Any]], row: List[str], centered: bool = False) -> str:
    output = """"""
    if not centered:
        for item_index, item in enumerate(row):
            output += f" {item}{' '*(len(get_longest_str(rows, item_index))-len(item)+1)}{Seps.vertical}"
        
    else:
        for item_index, item in enumerate(row):
            output += f"{item.center(len(get_longest_str(rows, item_index))+2)}{Seps.vertical}"
    output += "\n"
    return output

class Seps:
    horizontal: str = "─"
    vertical: str = "│"
    top_left_corner: str = "┌"
    top_right_corner: str = "┐"
    top_middle: str = "┬"
    bottom_left_corner: str = "└"
    bottom_right_corner: str = "┘"
    bottom_middle: str = "┴"
    middle_left: str = "├"
    middle_right: str = "┤"
    middle_center: str = "┼"

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    
    rows = convert_all_to_str(rows)
    output = """"""
    longest_length = len(get_longest_str(rows, 0))
    longest_str_of_all_indexes = get_longest_str_of_all_indexes(rows)
    print(get_longest_str_of_all_indexes(rows))
    print("longest_length", longest_length)
    if len(labels) == 0 or labels is None:
        output += Seps.top_left_corner + (Seps.horizontal*(longest_length+2)) + Seps.top_right_corner + "\n"
        for row in rows:
            output += Seps.vertical + output_row(rows, row, centered)
        output += Seps.bottom_left_corner + (Seps.horizontal*(longest_length+2)) + Seps.bottom_right_corner + "\n"
        
    else:
        output += Seps.top_left_corner + (Seps.horizontal*(longest_length+2)) + Seps.top_right_corner + "\n"
        output += Seps.vertical + output_labels(labels, longest_str_of_all_indexes)
        output += Seps.middle_left + (Seps.horizontal*(longest_length+2)) + (Seps.middle_center if len(labels) > 1 else Seps.middle_right) + "\n"
        for row in rows:
            output += Seps.vertical + output_row(rows, row, centered)
        output += Seps.bottom_left_corner + (Seps.horizontal*(longest_length+2)) + Seps.bottom_right_corner + "\n"
        

    
    return output


table = make_table(
    labels=["Names"],
    rows=[
        ["Lemon"],
        ["Sebastian"],
        ["KutieKatj9"],
        ["Jake"],
        ["Not Joe"],
        ["CookieTheCat"]
    ]
)
print(table)

ducky_table = make_table(
    rows=[
        ["Ducky Yellow", 3],
        ["Ducky Dave", 12],
        ["Ducky Tube", 7],
        ["Ducky Lemon", 1]
    ],
    labels=["Name", "Duckiness"],
    centered=True
)

print(ducky_table)

long_table = make_table(
    rows=[
        ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
        ["Hippopotomonstrosesquippedaliophobia"],
        ["Supercalifragilisticexpialidocious"],
        ["Pseudopseudohypoparathyroidism"],
        ["Floccinaucinihilipilification"],
        ["Antidisestablishmentarianism"],
        ["."]
    ],
    labels=["My Favourite Long Words"],
    centered=False
)

print(long_table)
