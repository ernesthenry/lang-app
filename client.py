from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/agent/")
remote_chain.invoke({"input": "how can langsmith help with testing?"})