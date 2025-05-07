export default function Joke(props) {
    return(
    <>
      <p>{props.setup}</p>
      <p>{props.punchline}</p>  
    </>
    );
}