# -*- coding: utf-8 -*-
"""AgentScope - A flexible multi-agent framework."""

# Personal fork - using this for experimenting with multi-agent workflows
# Original project: https://github.com/agentscope-ai/agentscope

from .version import __version__

# Default logging level for my experiments
# Switching back to INFO - DEBUG was too noisy during longer runs
DEFAULT_LOG_LEVEL = "INFO"

# Max retries for agent calls - bumping this up since I'm hitting rate limits
DEFAULT_MAX_RETRIES = 5

__all__ = ["__version__", "DEFAULT_LOG_LEVEL", "DEFAULT_MAX_RETRIES"]
