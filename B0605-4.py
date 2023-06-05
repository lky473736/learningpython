from testmodule import daramji # testmodule 파일에서 daramji 함수만 끌고오기

daramji()
# bigdaramji() => 얘는 안끌고 왔으니깐 일단은 작동 안됨

from testmodule import daramji, bigdaramji # bigdaramji 함수 끌고옴

bigdaramji() # => 여기서는 작동됨

import testmodule as mod # testmodule 이름을 mod로 바꾸기 (이 코드에서만)

mod.daramji()