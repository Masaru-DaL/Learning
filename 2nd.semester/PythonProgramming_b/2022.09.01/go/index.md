```go:
func Pic(dx, dy int) [][]uint8 {
  // 2次元配列の作成
  pic := make([][]unit8, dy)

}

## 3-19. Maps
`make`関数を使用して、mapを生成することができる。
`make(map[キーの型]値の型)`

```go: map
package main

import "fmt"

func main() {
    m := make(map[string]int)

    fmt.Println(m)

    m["key1"] = 10
    m["key2"] = 20

    fmt.Println(m)
}
```
map[]
map[key1:10 key2:20]

- 上記を踏まえた上で
```go: map(Tour)
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

func main() {
  // 1.
	m = make(map[string]Vertex)
	fmt.Println(m)

	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}

  // 2.
	fmt.Println(m)

  // 3.
	fmt.Println(m["Bell Labs"])
}
```
map[]
map[Bell Labs:{40.68433 -74.39967}]
{40.68433 -74.39967}

1. make関数で作成すると初期化して使用可能な状態になる。

2. key: `Bell Labs`, value: `{40.68433 -74.39967}`だと分かる。

3. keyを指定すると、対応したvalueが出力される。
