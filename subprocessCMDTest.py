# coding = utf-8
import  winpexpect

if(__name__=="__main__"):

    child = winpexpect.winspawn("sqlplus",timeout=5);
    child.expect([".*"]);

    print(child.before);
    print(child.after);
