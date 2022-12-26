import React, {useState} from 'react';

const Numbers = () => {

    const [numbers, setNumbers] = useState(['one','twp','threee']);
    const [letters, setLetters] = useState(['a','b','c']);
    const addNumber = () => {
            setNumbers([...numbers,'foirr'])
        }

        return (
        <div>
            <h1>Numbers</h1>
            {
                numbers.map(num=> {
                    return <h4>{num}</h4>
                })
            }
            <button onClick={addNumber}>Add a num</button>
        </div>
        )
}
export default Numbers;