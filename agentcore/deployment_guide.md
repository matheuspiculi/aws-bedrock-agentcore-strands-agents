# Guia de Deploy no Amazon Bedrock AgentCore

Este guia mostra como levar seu agente Strands para produção usando **Amazon Bedrock AgentCore**.

## 1. Pré-requisitos

- Acesso ao Amazon Bedrock AgentCore (preview ou GA conforme data)
- AWS CLI v2 configurado
- Permissões IAM necessárias (AgentCore Runtime, Bedrock, etc.)

## 2. Estrutura Recomendada para Deploy

```python
# agent.py (seu código Strands)
from strands import Agent
# ...

# Exponha como função para o Runtime
async def handler(event, context):
    user_input = event.get("input", "")
    response = agent(user_input)
    return {"response": str(response)}
```

## 3. Passos para Deploy (via AWS Console ou CLI)

1. Acesse o console do **Amazon Bedrock** > **AgentCore**
2. Crie um novo **Agent** ou use o **Runtime**
3. Faça upload do seu código (pode usar container image ou zip)
4. Configure:
   - Modelo (via Bedrock)
   - Memória (AgentCore Memory)
   - Identity (para tools)
   - Gateway (para expor tools/Lambda)

## 4. Usando Strands com AgentCore Runtime

O Strands Agents é totalmente compatível com o AgentCore Runtime. Basta empacotar sua aplicação.

Recomendação: Use o **AgentCore Starter Toolkit** ou CLI para simplificar.

## 5. Boas Práticas

- Sempre use **AgentCore Identity** para autenticação segura de tools
- Configure **Policy** para limitar ações do agente
- Ative **Observability** + CloudWatch/X-Ray
- Use **long-term memory** para agentes que precisam aprender

## Recursos Oficiais

- [What is Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [Strands + AgentCore Integration](https://strandsagents.com/)

---

*Guia inicial - personalize conforme sua arquitetura.*