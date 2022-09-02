# Go interfaceの存在意義について考える
こちらのサイトが参考になった
[今さら訊けない？ Go言語のInterfaceについてその本質をズバリ解説。](https://thiscalifornianlife.com/2021/01/10/golang-interface/)

## interfaceを使用しないと何が起こる？
monkey, humanという2つの構造体を定義する。
持っている要素は`Name`だけの簡単なものにする。

```go: not interface
package main

import "fmt"

// struct(monkey)
type monkey struct {Name string}

func (m monkey) imitate(){
  fmt.Println("Imitating")
}
func (m monkey) makeADream(){
  fmt.Println("Make a Dream!")
}

// struct(human)
type human struct {Name string}

func (h human) talk(){
  fmt.Println("Talking")
}
func (h human) makeADream(){
  fmt.Println("Make a Dream!")
}
```

- monkey
  - imitate, makeADream の2つのメソッド


