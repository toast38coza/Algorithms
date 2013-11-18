
def build_chessboard(n,m):

    for x in range(0,m):
        line = ""
        for x in range(0,n):
            if x%2==0:
                line = "{0}{1}" .format (line,"0")
            else:
                line = "{0}{1}" .format (line,"1")
        print line

def test_build_chessboard():

    n=7,m=4
    build_chessboard(n,m)

if __name__ == "__main__":
    test_build_chessboard()