import Joke from "../components/Joke";
export default function App() {
  return (
    <>
      <Joke
        setup="Setup: I got my daughter a fridge for her birthday."
        punchline="Punchline: I can't wait to see her face light up when she opens it." 
      />
      <Joke
        setup="Setup: How did the hacker escape the police?"
        punchline="Punchline: He just ransomware!" 
      />
        <Joke
        setup="Setup: Why don't pirates travel on mountain roads?"
        punchline="Punchline: Scurvy." 
      />
      <Joke
        setup="Setup: Why do bees stay in the hive in the winter?"
        punchline="Punchline: Swarm." 
      />
    </>
      
  );
}