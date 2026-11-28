import qrfunc
def main():
    while True:
        x=input("the link:").split()
        if x:
            y=input("the name:").split()
            if x and y:
                qrfunc.add_link(x,y)