from typing import Dict, List

from langchain_core.tools import BaseTool
from langchain_core.tools.base import BaseToolkit

from langchain_community.tools.clickup.prompt import (
    CLICKUP_FOLDER_CREATE_PROMPT,
    CLICKUP_GET_ALL_TEAMS_PROMPT,
    CLICKUP_GET_FOLDERS_PROMPT,
    CLICKUP_GET_LIST_PROMPT,
    CLICKUP_GET_SPACES_PROMPT,
    CLICKUP_GET_TASK_ATTRIBUTE_PROMPT,
    CLICKUP_GET_TASK_PROMPT,
    CLICKUP_LIST_CREATE_PROMPT,
    CLICKUP_TASK_CREATE_PROMPT,
    CLICKUP_UPDATE_TASK_ASSIGNEE_PROMPT,
    CLICKUP_UPDATE_TASK_PROMPT,
)
from langchain_community.tools.clickup.tool import ClickupAction
from langchain_community.utilities.clickup import ClickupAPIWrapper


class ClickupToolkit(BaseToolkit):
    """Clickup Toolkit.

    *Security Note*: This toolkit contains tools that can read and modify
        the state of a service; e.g., by reading, creating, updating, deleting
        data associated with this service.

        See https://python.langchain.com/docs/security for more information.

    Parameters:
        tools: List[BaseTool]. The tools in the toolkit. Default is an empty list.
    """

    tools: List[BaseTool] = []

    @classmethod
    def from_clickup_api_wrapper(
        cls, clickup_api_wrapper: ClickupAPIWrapper
    ) -> "ClickupToolkit":
        """Create a ClickupToolkit from a ClickupAPIWrapper.

        Args:
            clickup_api_wrapper: ClickupAPIWrapper. The Clickup API wrapper.

        Returns:
            ClickupToolkit. The Clickup toolkit.
        """
        operations: List[Dict] = [
            {
                "name": "get_task",
                "description": CLICKUP_GET_TASK_PROMPT,
            },
            {
                "name": "get_task_attribute",
                "description": CLICKUP_GET_TASK_ATTRIBUTE_PROMPT,
            },
            {
                "name": "get_teams",
                "description": CLICKUP_GET_ALL_TEAMS_PROMPT,
            },
            {
                "name": "create_task",
                "description": CLICKUP_TASK_CREATE_PROMPT,
            },
            {
                "name": "create_list",
                "description": CLICKUP_LIST_CREATE_PROMPT,
            },
            {
                "name": "create_folder",
                "description": CLICKUP_FOLDER_CREATE_PROMPT,
            },
            {
                "name": "get_list",
                "description": CLICKUP_GET_LIST_PROMPT,
            },
            {
                "name": "get_folders",
                "description": CLICKUP_GET_FOLDERS_PROMPT,
            },
            {
                "name": "get_spaces",
                "description": CLICKUP_GET_SPACES_PROMPT,
            },
            {
                "name": "update_task",
                "description": CLICKUP_UPDATE_TASK_PROMPT,
            },
            {
                "name": "update_task_assignees",
                "description": CLICKUP_UPDATE_TASK_ASSIGNEE_PROMPT,
            },
        ]
        tools = [
            ClickupAction(
                name=action["name"],
                description=action["description"],
                mode=action["name"],
                api_wrapper=clickup_api_wrapper,
            )
            for action in operations
        ]
        return cls(tools=tools)  # type: ignore[arg-type]

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
