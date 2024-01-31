default_number = "444-123-1233"


def readfiles(file):
    # check if file exist
    if file is None:
        print("Error: No file")
    else:
        with open(file, "r") as file:
            rows = (line.split(" ", 1) for line in file)
            dict = {row[0]: row[1].strip() for row in rows}
            for key, value in dict.items():
                print(f"{key}: {value}")
            return dict


result = {}


def isactive(activeA, activeB):
    for key, value in activeB.items():
        if value == "Yes":
            partial_string = key
            for k, v in activeA.items():
                if partial_string in k:
                    if v is None:
                        v = default_number
                    result[key] = v

    return result


def main():
    print("welcome")
    fileA = readfiles("active_users_obi/fileA")
    fileB = readfiles("active_users_obi/fileB")
    res = isactive(fileA, fileB)

    for key, value in res.items():
        print(f"{key} {value}")


if __name__ == "__main__":
    main()
