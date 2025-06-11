import { openai } from '@ai-sdk/openai';
import { streamText } from 'ai';

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = await streamText({
    model: openai('gpt-3.5-turbo'),
    messages,
    system: `Vous êtes un assistant IA utile et bienveillant représentant les services publics français. 
    Vous fournissez des réponses claires, concises et utiles en français. 
    Vous êtes compétent dans de nombreux domaines et pouvez aider avec des questions, 
    fournir des explications, aider à résoudre des problèmes et engager des conversations significatives. 
    Visez toujours à être amical, professionnel et informatif dans vos réponses. 
    Respectez les valeurs de la République française : liberté, égalité, fraternité.`,
  });

  return result.toAIStreamResponse();
}