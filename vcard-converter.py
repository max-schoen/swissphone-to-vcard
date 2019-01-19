import sys

#generic form of a vcard (split into lines because some are optional)
begin = "BEGIN:VCARD\n"
version = "VERSION:2.1\n"
n = "N:{name}\n"
fn = "FN:{name}\n"
tel = "TEL;CELL:{tel_number}\n"
group = "X-GROUP-MEMBERSHIP:My Contacts\n"
end = "END:VCARD\n"

#format for name string

n_format = "{};{};{};{};{}"

def name(text):
    names = text.split()
    n = len(names)
    if n > 1:
        return n_format.format(names[0],names[1],names[2] if n > 2 else "", names[3] if n > 3 else "", names[4] if n > 4 else "")
    elif n == 1:
        return n_format.format("",names[0],"","","")
    else:
        return ""



#get input and output file
if len(sys.argv) <= 1:
    print("Too few arguments. You must at least specify the input file and may also specify the output file")
    sys.exit()
elif len(sys.argv) == 2:
    input_file = sys.argv[1]
    output_file = sys.argv[1][::-1].split(".",1)[0][::-1]+".vcf"
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

contacts = []

#read input file into dictionaries (1 per contact)
with open(input_file,encoding="utf-16") as f:
    contact = {}
    key = ""
    value = ""
    for i,line in enumerate(f):
        if i % 2 == 0:
            key = line[:-1]
        else:
            value = line[:-1]
            contact[key] = value
        if i % 16 == 15:
            contacts.append(contact.copy())

with open(output_file,"w+",encoding="utf-8") as f:
    for contact in contacts:
        f.write(begin)
        f.write(version)
        f.write(n.format(name=name(contact["NAME"])))
        f.write(fn.format(name=contact["NAME"]))
        f.write(tel.format(tel_number=contact["TEL"]))
        f.write(group)
        f.write(end)