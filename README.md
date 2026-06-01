# Claude Speak

使 Claude 可以在执行的过程中说话

## 启动

```bash
uv run app
```

## Hooks 配置

将以下配置添加到 Claude 的 settings.json 中：

- **全局配置**（所有项目生效）：`~/.claude/settings.json`
- **项目级配置**（仅当前项目生效）：`.claude/settings.json`

```json
{
    "hooks": {
        "PreToolUse": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "PostToolUse": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "PostToolUseFailure": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "PostToolBatch": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "Notification": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "UserPromptSubmit": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "UserPromptExpansion": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "SessionStart": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "SessionEnd": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "Stop": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "StopFailure": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "SubagentStart": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "SubagentStop": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "PreCompact": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "PostCompact": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "PermissionRequest": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "PermissionDenied": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "Setup": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "TeammateIdle": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "TaskCreated": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "TaskCompleted": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "Elicitation": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "ElicitationResult": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "ConfigChange": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "WorktreeCreate": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "WorktreeRemove": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "InstructionsLoaded": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "CwdChanged": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "FileChanged": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ],
        "MessageDisplay": [
            {
                "hooks": [
                    {
                        "type": "http",
                        "url": "http://localhost:8000/message",
                        "context": {}
                    }
                ]
            }
        ]
    }
}
```

