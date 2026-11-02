import os

import requests


def main() -> None:
    url = "https://api.github.com/user"
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("GitHub 用户信息：")
        print(f"  登录名: {data.get('login')}")
        print(f"  姓名: {data.get('name')}")
        print(f"  公开仓库数: {data.get('public_repos')}")
        print(f"  粉丝数: {data.get('followers')}")
        print(f"  关注数: {data.get('following')}")
        print(f"  个人主页: {data.get('html_url')}")
    except requests.exceptions.HTTPError as exc:
        if response.status_code == 401:
            print("错误：未授权，请设置 GITHUB_TOKEN 环境变量后再运行。")
            print("获取方法：https://github.com/settings/tokens")
        else:
            print(f"HTTP 错误：{exc}")
    except requests.exceptions.RequestException as exc:
        print(f"请求失败：{exc}")


if __name__ == "__main__":
    main()
