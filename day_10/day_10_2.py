####关于包的概念
#a.b   a中的b
#关于模块化文件，太多了，难以赘述

#sound/                          顶层包
      # __init__.py               初始化 sound 包
      # formats/                  文件格式转换子包
      #         __init__.py
      #         wavread.py
      #         wavwrite.py
      #         aiffread.py
      #         aiffwrite.py
      #         auread.py
      #         auwrite.py
      #         ...
      # effects/                  声音效果子包
      #         __init__.py
      #         echo.py
      #         surround.py
      #         reverse.py
      #         ...
      # filters/                  filters 子包
      #         __init__.py
      #         equalizer.py
      #         vocoder.py
      #         karaoke.py
      #         ...

# import sound.effects.echo导入该包的特定模块
#sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)特定模块的特定功能
#from sound.effects import echo也可以这样导入


####导入的方法太多了







#####今天就到这里吧      ，本来还想学一下name的，，，，但是熄灯了‘’
#背单词去了！！！！！！