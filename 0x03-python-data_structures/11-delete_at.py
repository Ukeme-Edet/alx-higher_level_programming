#!/usr/bin/python3
def delete_at(my_list, idx):
    return (
        my_list[:idx] + my_list[: idx + 1]
        if idx > -1 and idx < len(my_list)
        else my_list
    )
