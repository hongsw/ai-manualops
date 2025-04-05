import Config

config :pythonx, :uv_init,
  pyproject_toml: """
  [project]
  name = "ai_manualops"
  version = "0.1.0"
  requires-python = ">=3.10"
  dependencies = [
    "erlastic>=2.0.0",
    "numpy>=1.24.0",
    "pandas>=2.0.0",
    "pydantic>=2.0.0"
  ]
  """
