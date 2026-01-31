from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Pipeline data model
class PipelineData(BaseModel):
    nodes: List[Dict]
    edges: List[Dict]


@app.get("/")
def root():
    return {"message": "Pipeline backend running"}


def is_dag(nodes, edges):
    graph = {node["id"]: [] for node in nodes}

    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        if src in graph:
            graph[src].append(tgt)

    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return False  # cycle detected

        if node in visited:
            return True

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False

        rec_stack.remove(node)
        return True

    for node in graph:
        if not dfs(node):
            return False
    
    return True


@app.post("/pipelines/parse")
async def parse_pipeline(data: PipelineData):
    num_nodes = len(data.nodes)
    num_edges = len(data.edges)
    dag_status = is_dag(data.nodes, data.edges)

    return {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "is_dag": dag_status
    }
