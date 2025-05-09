import Header from "./components/Header"
import Entry from "./components/Entry"
import Data from "./data"
/**
 * Challenge:
 * - import the array of data from data.js
 * - map over the array to create an <Entry /> component
 *   for every item in the data array.
 * - display the array of Entry components in place of the current
 *   hard-coded <Entry /> instance.
 */

export default function App() {
    const newData = Data.map((data) => {
        return(
        <Entry
            data={data}
        />
        )  
    })
    return (
        <>
        <Header />
        <main className="container">
            {newData}
        </main>
        </>
    )
}