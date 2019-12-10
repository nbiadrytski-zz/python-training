from string import Template


def main():
    templ = Template("You're watching ${title} by ${author}")

    str1 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str1)  # You're watching Advanced Python by Joe Marini

    data = {
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    str2 = templ.substitute(data)
    print(str2)  # You're watching Advanced Python by Joe Marini


if __name__ == "__main__":
    main()
    # feature branch commit
