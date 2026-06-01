import subprocess

from .config import ANNOUNCER, SPEED
from .norml import convert


def process_message(data: dict):
    # print(data)

    if "hook_event_name" not in data:
        return
    event: str = data["hook_event_name"]

    msg = ""
    match event:
        case "SessionStart":
            msg = "会话已启动"
        case "SessionEnd":
            msg = "会话已结束"
        case "UserPromptSubmit":
            msg = data["prompt"]
        case "InstructionsLoaded":
            msg = "指令已加载"
        case "MessageDisplay":
            msg = data["delta"]
        case "PreToolUse":
            msg = f"开始调用工具 {data['tool_name']}"
        case "PostToolUse":
            msg = f"工具调用成功 {data['tool_name']}"
        case "PostToolBatch":
            msg = "工具批量调用成功"
        case "PostToolUseFailure":
            msg = f"{data['tool_name']} 工具调用失败"
        case "Stop":
            # msg = data["last_assistant_message"]
            msg = "本次处理结束"
        case "SubagentStop":
            msg = ""

    if msg == "":
        return

    say_msg = convert(msg)

    subprocess.run(
        ["say", "-v", ANNOUNCER, "-r", SPEED, say_msg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
