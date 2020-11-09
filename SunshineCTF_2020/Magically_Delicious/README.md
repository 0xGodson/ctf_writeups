# Magically Delicious:Crypto:100pts
Can you help me decipher this message?  
⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 ⭐🦄🌑 ⭐🌈🦄 ⭐🌑🍀 ⭐🦄🍀 ⭐🎈⭐ 🦄🦄 ⭐🦄🎈 ⭐🌑🍀 ⭐🌈🌑 ⭐🌑⭐ ⭐🦄🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄⭐ ⭐🌈🍀 🦄🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🌑🦄 🦄🦄 ⭐🌑🐴 ⭐🌑🦄 ⭐🌈🍀 ⭐🌈🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄🦄 ⭐🌑🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🦄🎈 ⭐🌑🌑 ⭐🎈🦄  
Note: If you don't see a message above, make sure your browser can render emojis.  
Tip: If you're digging into the unicode encoding of the emojis, you're on the wrong track!  

# Solution
絵文字をデコードするらしい。  
所々スペースが入っているので、そこで文字が区切られていると予測できる。  
アルファベットからシフトしてるのかと考えたが、`⭐🌈🦄`と`⭐🦄🌈`が異なる文字なので順番にも意味があるようだ。  
flagの最初は`sun{`なので、以下のように対応している。  
| alphabet | eflag |
----|----
| s | ⭐🌈🍀 |
| u | ⭐🌈🦄 |
| u | ⭐🦄🌈 |
| { | ⭐🎈🍀 |

先頭に`⭐`が多い。  
唸っていると仲間が、「バイナリでは？」と答えを発見した。  
[Text to Binary Converter](https://www.rapidtables.com/convert/number/ascii-to-binary.html)を使う。  
| alphabet | binary | eflag |
----|----|----
| s | 01 110 011 | ⭐🌈🍀 |
| u | 01 110 101 | ⭐🌈🦄 |
| u | 01 101 110 | ⭐🦄🌈 |
| { | 01 111 011 | ⭐🎈🍀 |

先頭のみ001が01になっているようだ。  
よって以下のバイナリと文字の対応表が得られる。  
| binary | eflag(chr) |
----|----
| 000 |  |
| 001 | ⭐ |
| 010 |  |
| 011 | 🍀 |
| 100 |  |
| 101 | 🦄 |
| 110 | 🌈 |
| 111 | 🎈 |

残るは、`🌑💜🐴`の3つだけだ。  
総当たりすればよい。  
以下のemoi.pyでデコードする。  
```python:emoi.py
eflag = "⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 ⭐🦄🌑 ⭐🌈🦄 ⭐🌑🍀 ⭐🦄🍀 ⭐🎈⭐ 🦄🦄 ⭐🦄🎈 ⭐🌑🍀 ⭐🌈🌑 ⭐🌑⭐ ⭐🦄🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄⭐ ⭐🌈🍀 🦄🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🌑🦄 🦄🦄 ⭐🌑🐴 ⭐🌑🦄 ⭐🌈🍀 ⭐🌈🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄🦄 ⭐🌑🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🦄🎈 ⭐🌑🌑 ⭐🎈🦄"

table = [
#("000",""),
("001","⭐"),
#("010",""),
("011","🍀"),
#("100",""),
("101","🦄"),
("110","🌈"),
("111","🎈")]

p1 = [
("000","🌑"),
("010","💜"),
("100","🐴")]
p2 = [
("000","🌑"),
("010","🐴"),
("100","💜")]
p3 = [
("000","💜"),
("010","🌑"),
("100","🐴")]
p4 = [
("000","🐴"),
("010","🌑"),
("100","💜")]
p5 = [
("000","💜"),
("010","🐴"),
("100","🌑")]
p6 = [
("000","🐴"),
("010","💜"),
("100","🌑")]

for p in [p1, p2, p3, p4, p5, p6]:
    for i in eflag.split(" "):
        for j in table + p:
            i = i.replace(j[1],j[0])
        print(chr(int(i.zfill(9)[1:], 2)),end="")
    print()
```
実行する。  
```bash
$ python emoi.py
sun{huCky-oCpAh-EnCo@inG-is-pjE-DEsp-EnCo@inG-mEpjo@}
sun{huCky-oCpAh-EnCo@inG-is-plE-BEsp-EnCo@inG-mEplo@}
sun{juSky-oSrQj-UnSoRinW-is-rhU-TUsr-UnSoRinW-mUrhoR}
sun{juSky-oSrQj-UnSoRinW-is-rlU-PUsr-UnSoRinW-mUrloR}
sun{lucky-octal-encoding-is-the-best-encoding-method}
sun{lucky-octal-encoding-is-tje-`est-encoding-metjod}
```
5番目に正しいflagが表示された。  

## sun{lucky-octal-encoding-is-the-best-encoding-method}