import argparse
import time
from pathlib import Path
from openai import OpenAI

# 解析命令行参数
parser = argparse.ArgumentParser(description='Paper Reading Assistant Using KimiChat')
parser.add_argument('--paper', '-p', dest='paper', type=str, help='请上传待阅读的论文文件路径')
parser.add_argument('--questions', '-q', dest='questions', type=str, help='请上传问题列表文件的路径')
parser.add_argument('--output', '-o', dest='output', type=str, help='请指定论文总结输出的路径')
args = parser.parse_args()

# 设置API密钥
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url= "https://api.moonshot.cn/v1",
)

def read_questions(questions_path, separator='---'):
    with open(questions_path, 'r', encoding='utf-8') as file:
        questions = file.read().split(separator)
        questions = [q.strip() for q in questions if q.strip()]
    return questions

def read_paper(paper_path,questions_path,output_path):
    start_time = time.time()

    # 上传PDF文件
    print(f"正在读取论文：{paper_path}")
    file_object = client.files.create(file=Path(paper_path), purpose="file-extract")
    file_content = client.files.content(file_id=file_object.id).text
    
    # 读取问题列表
    print(f"正在读取问题列表：{questions_path}")
    questions = read_questions(questions_path)
    
    # 创建输出文件
    print(f"正在创建论文总结：{output_path}")
    output_file = Path(output_path)
    if output_file.is_file(): # 如果文件已存在，删除文件
        output_file.unlink()
    output_file.touch()

    # 准备对话历史
    history = [
        {
            "role": "system", 
            "content": "你是一名专业且严谨的科研文献阅读助手。"
        },
        {
            "role": "system",
            "content": file_content
        }
    ]
    
    # 开始对话
    try:
        for q in questions:
            print(f"问：{q}")
            history.append({
                "role": "user",
                "content": q
            })
            completion = client.chat.completions.create(
                model="moonshot-v1-32k",
                messages=history,
                temperature=0.3,
            )
            result = completion.choices[0].message.content
            print(f"答：{result}")
            history.append({
                "role": "assistant",
                "content": result
            })
            with open(output_file, 'a', encoding='utf-8') as f:
                # f.write(f"Q: {q}\nA: {result}\n---\n")
                f.write(f"{result}\n---\n")
        
        end_time = time.time()
        print(f"论文总结完成，总耗时：{end_time - start_time:.2f}秒")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    read_paper(args.paper,args.questions,args.output)
