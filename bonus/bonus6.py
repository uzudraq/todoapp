contents = ["All carrots are to be sliced longitudinally.",
            "the carrots were reported sliced.",
            "the carrots are to be eaten. "]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)

a = "i am a string " \
    "on" \
    " my " \
    "own"
print(a)