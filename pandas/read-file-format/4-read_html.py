#Live Html source code you can importing requests
import requests
import pandas as pd

head = {"User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36"}
src_code = \
requests.get("https://www.animecharactersdatabase.com/characters.php?id=73892",headers=head)
def get_table(html_code=pd.read_html(src_code.text)):
    df = pd.DataFrame(html_code[3]).drop(9)
    df = df.rename(columns={0:"key",1:"value"})
    array_json = []
    for n in range(0,9):
        array_json.append(
                {df['key'][int(n)]:df['value'][int(n)]}
                )
    return array_json

if __name__=="__main__":
    print (url,end="\n\n")
    print (get_table())
