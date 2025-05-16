import React from "react"
import ClaudeRecipe from "./ClaudeRecipe"
import List from "./List"
import {getRecipeFromMistral} from "../ai"

export default function Main() {

    const [ingredients, setIngredients] = React.useState(
        []
    )

    const [recipe, setRecipe] = React.useState("")
    

    function addIngredient(formData) {
        const newIngredient = formData.get("ingredient")
        setIngredients(prevIngredients => [...prevIngredients, newIngredient])
    }

     async function showRecipe(){
        setRecipe(await getRecipeFromMistral(ingredients))
    }
    
    return (
        <main>
            <form action={addIngredient} className="add-ingredient-form">
                <input
                    type="text"
                    placeholder="e.g. oregano"
                    aria-label="Add ingredient"
                    name="ingredient"
                />
                <button>Add ingredient</button>
            </form>
            
            {ingredients.length > 0 && <List 
                ingredients={ingredients}
                showRecipe={showRecipe}
                />}
            
            {recipe && <ClaudeRecipe showRecipe={recipe}/>} 
        </main>
    )
}