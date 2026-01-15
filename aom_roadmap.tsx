import React, { useState } from 'react';
import { ChevronDown, ChevronRight, CheckCircle, Circle, Code, Database, Brain, Network, Zap, GitBranch, Users, Shield } from 'lucide-react';

const AOMRoadmap = () => {
  const [activePhase, setActivePhase] = useState(0);
  const [activeTab, setActiveTab] = useState('roadmap');

  const phases = [
    {
      phase: "Phase 1: Foundation (Week 1-2)",
      duration: "2 weeks",
      status: "start",
      color: "blue",
      tasks: [
        {
          title: "1.1 Project Setup",
          subtasks: [
            "Initialize Python project with Poetry/pip",
            "Setup FastAPI backend structure",
            "Configure environment variables (.env)",
            "Setup logging framework (structlog)",
            "Initialize Git repository",
            "Create docker-compose.yml"
          ]
        },
        {
          title: "1.2 Basic LangGraph Agent",
          subtasks: [
            "Install LangGraph, LangChain",
            "Create simple StateGraph with 3 nodes",
            "Implement basic state schema (TypedDict)",
            "Add conditional edges",
            "Test basic flow: Input → Process → Output",
            "Add streaming support"
          ]
        },
        {
          title: "1.3 Database Setup",
          subtasks: [
            "Setup PostgreSQL (Docker)",
            "Design schema (users, tasks, logs)",
            "Implement SQLAlchemy models",
            "Create Alembic migrations",
            "Setup connection pooling"
          ]
        }
      ]
    },
    {
      phase: "Phase 2: Memory & State (Week 3-4)",
      duration: "2 weeks",
      status: "progress",
      color: "purple",
      tasks: [
        {
          title: "2.1 Persistence Layer",
          subtasks: [
            "Implement SqliteSaver for checkpoints",
            "Add state serialization/deserialization",
            "Test agent resume after crash",
            "Implement state versioning",
            "Add checkpoint cleanup logic"
          ]
        },
        {
          title: "2.2 Vector Memory",
          subtasks: [
            "Setup Chroma/FAISS vector DB",
            "Implement embedding pipeline (OpenAI/local)",
            "Create document chunking strategy",
            "Build semantic search interface",
            "Add memory retrieval to agent state"
          ]
        },
        {
          title: "2.3 Short-term Memory",
          subtasks: [
            "Implement conversation buffer",
            "Add token counting",
            "Create memory summarization",
            "Implement sliding window context"
          ]
        }
      ]
    },
    {
      phase: "Phase 3: Graph RAG (Week 5-6)",
      duration: "2 weeks",
      status: "pending",
      color: "green",
      tasks: [
        {
          title: "3.1 Neo4j Setup",
          subtasks: [
            "Setup Neo4j (Docker/Cloud)",
            "Design graph schema (nodes/relationships)",
            "Implement Python driver integration",
            "Create entity extraction pipeline",
            "Build relationship inference logic"
          ]
        },
        {
          title: "3.2 Knowledge Graph Construction",
          subtasks: [
            "Parse code repositories (AST)",
            "Extract entities from docs/emails",
            "Build service dependency graph",
            "Link errors to services/commits",
            "Create user-action graphs"
          ]
        },
        {
          title: "3.3 Graph Query Engine",
          subtasks: [
            "Implement Cypher query builder",
            "Create graph traversal algorithms",
            "Build subgraph extraction",
            "Add graph-based context retrieval",
            "Combine vector + graph search"
          ]
        }
      ]
    },
    {
      phase: "Phase 4: Tools & Actions (Week 7-8)",
      duration: "2 weeks",
      status: "pending",
      color: "orange",
      tasks: [
        {
          title: "4.1 Core Tools",
          subtasks: [
            "Database query tool (SQL executor)",
            "Log search tool (Elasticsearch/grep)",
            "Code search tool (AST/regex)",
            "REST API caller (with auth)",
            "File system reader/writer"
          ]
        },
        {
          title: "4.2 Integration Tools",
          subtasks: [
            "Jira API integration",
            "GitHub API integration",
            "Slack webhook sender",
            "Email sender (SMTP)",
            "Calendar API (Google/Outlook)"
          ]
        },
        {
          title: "4.3 Tool Execution Framework",
          subtasks: [
            "Implement tool registry",
            "Add error handling & retries",
            "Create tool result validation",
            "Add rate limiting",
            "Implement tool chaining"
          ]
        }
      ]
    },
    {
      phase: "Phase 5: MCP Servers (Week 9-10)",
      duration: "2 weeks",
      status: "pending",
      color: "pink",
      tasks: [
        {
          title: "5.1 MCP Protocol Implementation",
          subtasks: [
            "Understand MCP specification",
            "Create base MCP server class",
            "Implement JSON-RPC transport",
            "Add capability negotiation",
            "Build server discovery mechanism"
          ]
        },
        {
          title: "5.2 Custom MCP Servers",
          subtasks: [
            "Email MCP (IMAP/SMTP)",
            "GitHub MCP (REST API)",
            "Calendar MCP (CalDAV)",
            "File System MCP (local/S3)",
            "Browser MCP (Playwright)"
          ]
        },
        {
          title: "5.3 MCP Integration",
          subtasks: [
            "Connect LangGraph to MCP",
            "Implement dynamic tool loading",
            "Add MCP server health checks",
            "Create MCP request routing",
            "Build MCP response caching"
          ]
        }
      ]
    },
    {
      phase: "Phase 6: Multi-Agent System (Week 11-12)",
      duration: "2 weeks",
      status: "pending",
      color: "indigo",
      tasks: [
        {
          title: "6.1 Agent Architecture",
          subtasks: [
            "Design agent hierarchy",
            "Create PlannerAgent graph",
            "Create ResearchAgent graph",
            "Create ActionAgent graph",
            "Create AuditorAgent graph"
          ]
        },
        {
          title: "6.2 Agent Coordination",
          subtasks: [
            "Implement subgraph execution",
            "Add inter-agent messaging",
            "Create agent state sharing",
            "Build agent result aggregation",
            "Add agent failure recovery"
          ]
        },
        {
          title: "6.3 Specialized Agents",
          subtasks: [
            "Code analysis agent",
            "Log analysis agent",
            "Incident response agent",
            "Deployment agent",
            "Communication agent"
          ]
        }
      ]
    },
    {
      phase: "Phase 7: Human-in-Loop (Week 13-14)",
      duration: "2 weeks",
      status: "pending",
      color: "red",
      tasks: [
        {
          title: "7.1 Interrupt System",
          subtasks: [
            "Implement interrupt() in LangGraph",
            "Create approval request schema",
            "Build approval queue (Redis/DB)",
            "Add timeout handling",
            "Implement approval UI endpoint"
          ]
        },
        {
          title: "7.2 Risk Assessment",
          subtasks: [
            "Define risk levels (low/med/high)",
            "Create action risk classifier",
            "Implement auto-approve rules",
            "Add rollback mechanisms",
            "Build audit trail"
          ]
        },
        {
          title: "7.3 Feedback Loop",
          subtasks: [
            "Collect human corrections",
            "Store feedback in graph",
            "Implement preference learning",
            "Add feedback-based routing",
            "Create feedback analytics"
          ]
        }
      ]
    },
    {
      phase: "Phase 8: Dashboard & API (Week 15-16)",
      duration: "2 weeks",
      status: "pending",
      color: "cyan",
      tasks: [
        {
          title: "8.1 REST API",
          subtasks: [
            "Design API endpoints (OpenAPI)",
            "Implement authentication (JWT)",
            "Add rate limiting (Redis)",
            "Create WebSocket for streaming",
            "Build API documentation (Swagger)"
          ]
        },
        {
          title: "8.2 Admin Dashboard",
          subtasks: [
            "Setup React/Vue frontend",
            "Create agent status view",
            "Build task queue monitor",
            "Add approval interface",
            "Implement graph visualization"
          ]
        },
        {
          title: "8.3 Monitoring",
          subtasks: [
            "Add Prometheus metrics",
            "Create Grafana dashboards",
            "Implement health checks",
            "Add error alerting (PagerDuty)",
            "Build performance profiling"
          ]
        }
      ]
    },
    {
      phase: "Phase 9: Testing & Reliability (Week 17-18)",
      duration: "2 weeks",
      status: "pending",
      color: "yellow",
      tasks: [
        {
          title: "9.1 Testing Strategy",
          subtasks: [
            "Unit tests (pytest, 80% coverage)",
            "Integration tests (agent flows)",
            "Load tests (Locust)",
            "Chaos testing (failure injection)",
            "Security tests (OWASP)"
          ]
        },
        {
          title: "9.2 Reliability Engineering",
          subtasks: [
            "Implement circuit breakers",
            "Add retry strategies",
            "Create fallback mechanisms",
            "Build idempotency layer",
            "Add transaction management"
          ]
        },
        {
          title: "9.3 Observability",
          subtasks: [
            "Distributed tracing (Jaeger)",
            "Structured logging",
            "Error tracking (Sentry)",
            "Performance monitoring (APM)",
            "Cost tracking"
          ]
        }
      ]
    },
    {
      phase: "Phase 10: Production Deploy (Week 19-20)",
      duration: "2 weeks",
      status: "pending",
      color: "teal",
      tasks: [
        {
          title: "10.1 Infrastructure",
          subtasks: [
            "Setup Kubernetes cluster",
            "Create Helm charts",
            "Configure CI/CD (GitHub Actions)",
            "Setup staging environment",
            "Implement blue-green deployment"
          ]
        },
        {
          title: "10.2 Security Hardening",
          subtasks: [
            "Secrets management (Vault)",
            "Network policies",
            "RBAC configuration",
            "SSL/TLS setup",
            "Vulnerability scanning"
          ]
        },
        {
          title: "10.3 Production Launch",
          subtasks: [
            "Load testing in staging",
            "Gradual rollout (canary)",
            "Monitoring setup",
            "Documentation completion",
            "Team training"
          ]
        }
      ]
    }
  ];

  const architecture = {
    layers: [
      {
        name: "Presentation Layer",
        components: [
          { name: "Admin Dashboard", tech: "React + Tailwind" },
          { name: "REST API", tech: "FastAPI" },
          { name: "WebSocket", tech: "FastAPI WebSocket" }
        ]
      },
      {
        name: "Orchestration Layer",
        components: [
          { name: "LangGraph Orchestrator", tech: "LangGraph" },
          { name: "Agent Router", tech: "Custom Logic" },
          { name: "State Manager", tech: "LangGraph State" }
        ]
      },
      {
        name: "Agent Layer",
        components: [
          { name: "Planner Agent", tech: "LangGraph Subgraph" },
          { name: "Research Agent", tech: "LangGraph Subgraph" },
          { name: "Action Agent", tech: "LangGraph Subgraph" },
          { name: "Auditor Agent", tech: "LangGraph Subgraph" }
        ]
      },
      {
        name: "Intelligence Layer",
        components: [
          { name: "LLM Interface", tech: "OpenAI/Claude API" },
          { name: "Graph RAG", tech: "Neo4j + Embeddings" },
          { name: "Vector Search", tech: "Chroma/FAISS" }
        ]
      },
      {
        name: "Integration Layer",
        components: [
          { name: "Tool Registry", tech: "Python Registry" },
          { name: "MCP Client", tech: "Custom Implementation" },
          { name: "API Connectors", tech: "httpx/requests" }
        ]
      },
      {
        name: "Data Layer",
        components: [
          { name: "PostgreSQL", tech: "Relational Data" },
          { name: "Neo4j", tech: "Knowledge Graph" },
          { name: "Chroma", tech: "Vector Embeddings" },
          { name: "Redis", tech: "Cache & Queue" }
        ]
      }
    ]
  };

  const techStack = [
    { category: "Backend", items: ["FastAPI", "Python 3.11+", "Poetry", "Pydantic"] },
    { category: "Agent Framework", items: ["LangGraph", "LangChain", "OpenAI SDK"] },
    { category: "Databases", items: ["PostgreSQL", "Neo4j", "Redis", "Chroma/FAISS"] },
    { category: "Infrastructure", items: ["Docker", "Kubernetes", "Nginx", "Grafana"] },
    { category: "Monitoring", items: ["Prometheus", "Jaeger", "Sentry", "Structlog"] },
    { category: "Frontend", items: ["React", "Tailwind CSS", "React Flow", "Recharts"] }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Brain className="w-12 h-12 text-purple-400" />
            <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
              AOM Agent
            </h1>
          </div>
          <p className="text-xl text-slate-300">AI Autonomous Operations Manager</p>
          <p className="text-sm text-slate-400 mt-2">Enterprise-Grade Multi-Agent System with Graph RAG & MCP</p>
        </div>

        {/* Tab Navigation */}
        <div className="flex gap-4 mb-8 bg-slate-800/50 p-2 rounded-xl backdrop-blur">
          {['roadmap', 'architecture', 'tech', 'flow'].map(tab => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`flex-1 py-3 px-6 rounded-lg font-semibold transition-all ${
                activeTab === tab
                  ? 'bg-purple-600 text-white shadow-lg'
                  : 'bg-slate-700/50 text-slate-300 hover:bg-slate-700'
              }`}
            >
              {tab === 'roadmap' && '🗺️ Roadmap'}
              {tab === 'architecture' && '🏗️ Architecture'}
              {tab === 'tech' && '⚡ Tech Stack'}
              {tab === 'flow' && '🔄 Flow Diagram'}
            </button>
          ))}
        </div>

        {/* Roadmap Tab */}
        {activeTab === 'roadmap' && (
          <div className="space-y-6">
            {phases.map((phase, idx) => (
              <div
                key={idx}
                className="bg-slate-800/50 rounded-xl p-6 backdrop-blur border border-slate-700 hover:border-purple-500 transition-all"
              >
                <div
                  className="flex items-center justify-between cursor-pointer"
                  onClick={() => setActivePhase(activePhase === idx ? -1 : idx)}
                >
                  <div className="flex items-center gap-4">
                    {activePhase === idx ? <ChevronDown className="w-6 h-6" /> : <ChevronRight className="w-6 h-6" />}
                    <div>
                      <h3 className="text-2xl font-bold text-purple-300">{phase.phase}</h3>
                      <p className="text-sm text-slate-400">{phase.duration} • Status: {phase.status}</p>
                    </div>
                  </div>
                  <div className={`w-4 h-4 rounded-full bg-${phase.color}-500`}></div>
                </div>

                {activePhase === idx && (
                  <div className="mt-6 space-y-4">
                    {phase.tasks.map((task, taskIdx) => (
                      <div key={taskIdx} className="bg-slate-900/50 rounded-lg p-4">
                        <h4 className="text-lg font-semibold text-purple-200 mb-3">{task.title}</h4>
                        <ul className="space-y-2">
                          {task.subtasks.map((subtask, subIdx) => (
                            <li key={subIdx} className="flex items-start gap-3 text-slate-300">
                              <Circle className="w-4 h-4 mt-1 text-slate-500 flex-shrink-0" />
                              <span>{subtask}</span>
                            </li>
                          ))}
                        </ul>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        {/* Architecture Tab */}
        {activeTab === 'architecture' && (
          <div className="space-y-6">
            {architecture.layers.map((layer, idx) => (
              <div key={idx} className="bg-slate-800/50 rounded-xl p-6 backdrop-blur border border-slate-700">
                <h3 className="text-2xl font-bold text-purple-300 mb-4">{layer.name}</h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  {layer.components.map((comp, compIdx) => (
                    <div key={compIdx} className="bg-slate-900/50 rounded-lg p-4">
                      <div className="flex items-center gap-2 mb-2">
                        <Code className="w-5 h-5 text-purple-400" />
                        <h4 className="font-semibold text-slate-200">{comp.name}</h4>
                      </div>
                      <p className="text-sm text-slate-400">{comp.tech}</p>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Tech Stack Tab */}
        {activeTab === 'tech' && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {techStack.map((category, idx) => (
              <div key={idx} className="bg-slate-800/50 rounded-xl p-6 backdrop-blur border border-slate-700">
                <h3 className="text-xl font-bold text-purple-300 mb-4">{category.category}</h3>
                <ul className="space-y-2">
                  {category.items.map((item, itemIdx) => (
                    <li key={itemIdx} className="flex items-center gap-2 text-slate-300">
                      <CheckCircle className="w-4 h-4 text-green-400" />
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        )}

        {/* Flow Diagram Tab */}
        {activeTab === 'flow' && (
          <div className="bg-slate-800/50 rounded-xl p-8 backdrop-blur border border-slate-700">
            <h3 className="text-2xl font-bold text-purple-300 mb-6 text-center">System Flow Diagram</h3>
            <div className="space-y-4 text-slate-300">
              <div className="flex items-center gap-4 p-4 bg-slate-900/50 rounded-lg">
                <Users className="w-8 h-8 text-blue-400" />
                <div>
                  <div className="font-bold">User / System Event</div>
                  <div className="text-sm text-slate-400">Trigger (API, Webhook, Schedule, Alert)</div>
                </div>
              </div>
              
              <div className="flex justify-center">
                <div className="w-0.5 h-8 bg-purple-500"></div>
              </div>

              <div className="flex items-center gap-4 p-4 bg-slate-900/50 rounded-lg">
                <GitBranch className="w-8 h-8 text-purple-400" />
                <div>
                  <div className="font-bold">LangGraph Orchestrator</div>
                  <div className="text-sm text-slate-400">State management, checkpointing, streaming</div>
                </div>
              </div>

              <div className="flex justify-center">
                <div className="w-0.5 h-8 bg-purple-500"></div>
              </div>

              <div className="flex items-center gap-4 p-4 bg-slate-900/50 rounded-lg">
                <Brain className="w-8 h-8 text-pink-400" />
                <div>
                  <div className="font-bold">Planner Agent (Decision Node)</div>
                  <div className="text-sm text-slate-400">Analyze request, create execution plan</div>
                </div>
              </div>

              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
                <div className="p-4 bg-green-900/30 rounded-lg border border-green-500">
                  <Database className="w-6 h-6 text-green-400 mb-2" />
                  <div className="font-semibold text-sm">Query Graph RAG</div>
                  <div className="text-xs text-slate-400">Neo4j + Vector</div>
                </div>
                <div className="p-4 bg-orange-900/30 rounded-lg border border-orange-500">
                  <Zap className="w-6 h-6 text-orange-400 mb-2" />
                  <div className="font-semibold text-sm">Call Tools</div>
                  <div className="text-xs text-slate-400">DB, API, File</div>
                </div>
                <div className="p-4 bg-pink-900/30 rounded-lg border border-pink-500">
                  <Network className="w-6 h-6 text-pink-400 mb-2" />
                  <div className="font-semibold text-sm">MCP Servers</div>
                  <div className="text-xs text-slate-400">Email, GitHub, Browser</div>
                </div>
                <div className="p-4 bg-red-900/30 rounded-lg border border-red-500">
                  <Shield className="w-6 h-6 text-red-400 mb-2" />
                  <div className="font-semibold text-sm">Ask Human</div>
                  <div className="text-xs text-slate-400">Approval Required</div>
                </div>
              </div>

              <div className="flex justify-center mt-4">
                <div className="w-0.5 h-8 bg-purple-500"></div>
              </div>

              <div className="flex items-center gap-4 p-4 bg-slate-900/50 rounded-lg">
                <GitBranch className="w-8 h-8 text-indigo-400" />
                <div>
                  <div className="font-bold">Action Agent</div>
                  <div className="text-sm text-slate-400">Execute plan, handle errors, retry logic</div>
                </div>
              </div>

              <div className="flex justify-center">
                <div className="w-0.5 h-8 bg-purple-500"></div>
              </div>

              <div className="flex items-center gap-4 p-4 bg-slate-900/50 rounded-lg">
                <CheckCircle className="w-8 h-8 text-green-400" />
                <div>
                  <div className="font-bold">Auditor Agent</div>
                  <div className="text-sm text-slate-400">Verify results, update knowledge graph</div>
                </div>
              </div>

              <div className="flex justify-center">
                <div className="w-0.5 h-8 bg-purple-500"></div>
              </div>

              <div className="flex items-center gap-4 p-4 bg-slate-900/50 rounded-lg">
                <Users className="w-8 h-8 text-cyan-400" />
                <div>
                  <div className="font-bold">Response to User</div>
                  <div className="text-sm text-slate-400">Result + context + next actions</div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Footer Stats */}
        <div className="mt-12 grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="bg-slate-800/50 rounded-xl p-6 text-center backdrop-blur border border-slate-700">
            <div className="text-3xl font-bold text-purple-400">20</div>
            <div className="text-sm text-slate-400">Weeks</div>
          </div>
          <div className="bg-slate-800/50 rounded-xl p-6 text-center backdrop-blur border border-slate-700">
            <div className="text-3xl font-bold text-pink-400">10</div>
            <div className="text-sm text-slate-400">Phases</div>
          </div>
          <div className="bg-slate-800/50 rounded-xl p-6 text-center backdrop-blur border border-slate-700">
            <div className="text-3xl font-bold text-green-400">6</div>
            <div className="text-sm text-slate-400">Agents</div>
          </div>
          <div className="bg-slate-800/50 rounded-xl p-6 text-center backdrop-blur border border-slate-700">
            <div className="text-3xl font-bold text-cyan-400">100%</div>
            <div className="text-sm text-slate-400">Production Ready</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AOMRoadmap;