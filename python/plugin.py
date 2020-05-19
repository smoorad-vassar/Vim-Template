import os
try:
    import vim
except ImportError:
    print("No vim module available outside vim")
    pass


def _generate_source_c(filename):
    pass


def _generate_source_cpp(filename):
    pass


def generate_source(filename):
    pass


def fill_skeleton(loaded_file, key, value):
    if not key or not value:
        return loaded_file

    return loaded_file.replace(key, value)


def load_skeleton(file_template):
    with open(file_template, "r") as template:
        return template.read()


def set_up_dict(DIRC):
    default_files = os.listdir(DIRC)
    default_dict = {}

    for i in default_files:
        default_dict[i.split("_")[0]] = i

    return default_dict


def _default(name):
    if not name:
        return None

    python_directory = str(os.path.dirname(os.path.realpath(__file__)))
    DIRC = python_directory + "/../default_templates/"
    default_dict = set_up_dict(DIRC)

    index = name.rfind(".")
    if(index == -1):
        return

    key = "%here%"
    value = name[0:index]
    extension = name[index+1:]
    return _final_buffer(extension, DIRC, default_dict, key, value)


def _custom(name):
    if not name:
        return None

    python_directory = str(os.path.dirname(os.path.realpath(__file__)))
    DIRC = python_directory + "/../custom_templates/"
    default_dict = set_up_dict(DIRC)
    return _final_buffer(name, DIRC, default_dict, None, None)


def _final_buffer(template, DIRC, default_dict, key, value):
    if(template not in default_dict):
        return None

    load_file = DIRC + default_dict[template]
    loaded_file = load_skeleton(load_file)
    return fill_skeleton(loaded_file, key, value)


def write_to_vim(Buffer, final_file):
    if not final_file:
        return

    final_file = final_file.split("\n")
    Buffer.append(final_file)
    del Buffer[0]
    pass


def _file_name(Buffer):
    name = Buffer.name
    index = name.rfind("/")

    if index == -1:
        return None

    return name[index+1:]


def default_template():
    Buffer = vim.current.buffer
    final_file = _default(_file_name(Buffer))
    write_to_vim(Buffer, final_file)
    pass


def custom_template():
    name = vim.eval("a:template")
    Buffer = vim.current.buffer
    final_file = _custom(name)
    write_to_vim(Buffer, final_file)
    pass


if __name__ == "__main__":
    default_template()
    pass