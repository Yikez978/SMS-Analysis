import pandas as pd
import lxml.etree as ET

from textanalysis import myutil as my


def read_xml(path):
    """reads the xml file at the given path
        returns an ElementTree"""
    parser = ET.XMLParser(encoding = 'UTF-8', ns_clean=True, recover=True)
    tree = ET.parse(path, parser)
    return tree


def sms_backup_to_df(tree, start = 0, end = -1, format = 'sms'):
    """convert an smsbackup etree to dataframe"""
    root = tree.getroot()
    i = 0
    l = len(root)
    #iterate over children.
    if end == -1:
        end = l
    smses = []
    my.printProgress(i, end+start, prefix='Progress:', suffix='Complete', barLength=50)
    for i in range(start, end):
        #root[i] gives a etree object thingy
        msg = root[i]
        my.printProgress(i, end+start, prefix='Progress:', suffix='Complete', barLength=50)
        #this isn't that good because you have to cycle over it twice.
        #but that's only an arithmetic increase
        if msg.tag == format:
            #all the data is in the attributes
            smses.append(dict(msg.attrib))

    df = pd.DataFrame(smses)
    return (df)

def xmltutorial_to_df(tree):
    """convert the 20.5.1.2 Parsing XML tutorial file"""
    root = tree.getroot()
    #returns 'name'
    columns = root[0].keys()
    #empty list to store dicionaries for each row
    rows = []
    col = ['name','rank', 'year', 'gdppc']
    for child in root:
        data = [child[i].text for i in range(3)]
        data.insert(0,child.attrib['name'])
        #print(data)
        #append the dict representing a row
        rows.append(dict(zip(col, data)))
    #print(rows)
    return (pd.DataFrame(rows))


def get_sms_values(child):
    """assume it's good"""
    rowvals = []
    for e in child.values():
        rowvals.append(e)
    return(rowvals)


def main():
    """The main method."""
    print(" ")
    tree = read_xml(r"C:\Users\Ryan\PycharmProjects\TextAnalysis\xmltutorial\tutorial.xml")
    print(tree)
    df = xmltutorial_to_df(tree)
    print(df)

    tree = read_xml(r"C:\Users\Ryan\PycharmProjects\TextAnalysis\data\smsbackup\sms-20170429205511.xml")
    df = sms_backup_to_df(tree=tree)
    print(df.head)

if __name__ == "__main__": main()
