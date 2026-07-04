#!/usr/bin/env python3
"""
Exemplo simples de Agente com Strands Agents SDK + Amazon Bedrock

Execute localmente após configurar credenciais AWS e habilitar modelo no Bedrock.
"""

from strands import Agent
from strands.models.bedrock import BedrockModel

# Configura o modelo (use Claude 3.5 Sonnet ou Amazon Nova Premier)
model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20241022-v2:0",  # ou "amazon.nova-premier-v1:0"
    region_name="us-east-1"  # ajuste conforme sua região
)

# Cria o agente
agent = Agent(
    model=model,
    system_prompt="""Você é um assistente útil especializado em AWS e arquitetura de sistemas.
    Responda de forma clara, técnica e amigável. Se precisar de ferramentas, avise.
    """ 
)

def main():
    print("\n🤖 Agente Strands + Bedrock iniciado!")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Até logo!")
            break
        
        if not user_input:
            continue
            
        try:
            response = agent(user_input)
            print(f"Agente: {response}\n")
        except Exception as e:
            print(f"Erro: {e}\n")

if __name__ == "__main__":
    main()