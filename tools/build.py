import glob
import csv
import os

# フォルダーパス
input_dir = "../src/IDiME for Meltype"
output_dir = "../out"
output_filename = "IDiME_for_Meltype.tsv"
output_path = os.path.join(output_dir, output_filename)
tsv_files = sorted(glob.glob(os.path.join(input_dir, "*.tsv")))

if not tsv_files:
    print("対象のソースファイルが見つかりませんでした")
    exit()

header_written = False

with open(output_path, "w", encoding="utf-8", newline="") as outfile:
    writer = csv.writer(outfile, delimiter="\t")

    for tsv_file in tsv_files:
        if os.path.abspath(tsv_file) == os.path.abspath(output_path):
            continue

        print(f"処理中: {tsv_file}")
        with open(tsv_file, "r", encoding="utf-8", newline="") as infile:
            reader = csv.reader(infile, delimiter="\t")

            try:
                header = next(reader) # 1行目を読み込む
            except StopIteration:
                continue # 空ファイルをスキップ

            if not header_written:
                writer.writerow(header)
                header_written = True

            # 残りを書き込む
            for row in reader:
                writer.writerow(row)
print(f"統合が完了しました → {output_path}")