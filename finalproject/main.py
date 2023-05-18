# ここでcsvを読み込んで、pandasのDataFrame型にする
# 必要であれば色々前処理をする
def read_csv() -> pandas.DataFrame:
    # TODO: 実装
    pass


# テキストに対する特徴(identity)
# いい感じにメソッドとかはやしてもらってOK
class Identity:
    def __init__(self):
        self.count_coordinate_adjectives = 0
        self.count_non_coordinate_adjectives = 0
        self.count_tensed_verbs = 0
        self.count_modalized_verbs = 0


# CSVがDataFrameで与えられるので特徴を抽出する
# 各著者に対して特徴のリストを持つ辞書を返す
def extract_identities(a: pandas.DataFrame) -> dict[str, list[Identity]]:
    # TODO: 実装
    pass


# textがauthorによって書かれたかどうかを判定する
def verify(d: dict[str, list[Identity]], text: str, author: str) -> bool:
    # TODO: 判定アルゴリズムを実装する
    pass


def main():
    pass


main()
