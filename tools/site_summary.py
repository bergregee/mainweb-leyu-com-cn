import json

SITE_DATA = {
    "name": "乐鱼体育",
    "url": "https://mainweb-leyu.com.cn",
    "tags": ["体育", "赛事", "直播", "娱乐"],
    "description": "乐鱼体育提供全球热门体育赛事直播、即时比分、赛程数据与互动社区服务，是运动爱好者的一站式数字平台。"
}

def extract_keywords(text):
    """从描述中提取关键词列表，基于常见分隔符分割"""
    import re
    words = re.split(r'[，,、\s]+', text)
    return [w for w in words if len(w) >= 2]

def generate_summary(data):
    """基于站点数据生成结构化摘要"""
    keywords = extract_keywords(data["description"])
    summary = {
        "site": data["name"],
        "url": data["url"],
        "tags": data["tags"],
        "keywords": list(set(keywords + data["tags"])),
        "brief": data["description"][:60]
    }
    return summary

def format_summary(summary):
    lines = []
    lines.append("站点摘要")
    lines.append("=" * 20)
    lines.append(f"名称: {summary['site']}")
    lines.append(f"URL: {summary['url']}")
    lines.append(f"标签: {', '.join(summary['tags'])}")
    lines.append(f"关键词: {', '.join(summary['keywords'])}")
    lines.append(f"简短说明: {summary['brief']}")
    return "\n".join(lines)

def save_summary(summary, filepath="site_summary_output.json"):
    """将摘要保存为JSON文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"摘要已保存至 {filepath}")

def main():
    summary = generate_summary(SITE_DATA)
    text = format_summary(summary)
    print(text)
    save_summary(summary)

if __name__ == "__main__":
    main()