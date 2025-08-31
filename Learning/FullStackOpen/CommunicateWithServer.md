# Communicating with Server

## c. Getting data from server

**Define db.json at root**

```json
{
  "notes": [
    {
      "id": "1",
      "content": "HTML is easy",
      "important": true
    },
    {
      "id": "2",
      "content": "Browser can execute only JavaScript",
      "important": false
    },
    {
      "id": "3",
      "content": "GET and POST are the most important methods of HTTP protocol",
      "important": true
    }
  ]
}
```

You can start the JSON Server without a spearate installation by running the npx command in the root directory of the application:

```bash
npx json-server --port 3001 db.json
```

### npm

Example of a Json server

**Install dependencies**

```bash
npm install axios
npm install json-server --save-dev
```

**Modify package.json for it's scirpts part**

```json
"start:json-server": "json-server --watch db.json --port 3000"
```

start the server

```bash
npm run start:json-server
```

test by curl

```bash
curl http://localhost:3000/notes
```

### Axio and promises

```ts
axios
	.get('http://localhost:3000/notes')
	.then(response => {
		const notes = response.data
		console.log(notes)
	}
)
```

### Effect-hooks

```js
import { useEffect } from 'react'

const App = () => {
    const [notes, setNotes] = useState([])
    
    useEffect(() => {
        console.log('effect')
        axios
        	.get('http://localhost:3000/notes')
        	.then(response => {
            console.log('promise fulfilled')
            setNotes(response.data)
        })
    }, [])
    console.log('render', notes.length, 'notes')
    
    // ...
}
```

### The development runtime environment

![](https://fullstackopen.com/static/0e3766361ce9d08f0c4fdd39152cf493/5a190/18e.png)

### Exercise 2.11

Store the initial state of the application in the file db.json, which should be placed in the root of the project.

```json
{
  "persons":[
    { 
      "name": "Arto Hellas", 
      "number": "040-123456",
      "id": "1"
    },
    { 
      "name": "Ada Lovelace", 
      "number": "39-44-5323523",
      "id": "2"
    },
    { 
      "name": "Dan Abramov", 
      "number": "12-43-234345",
      "id": "3"
    },
    { 
      "name": "Mary Poppendieck", 
      "number": "39-23-6423122",
      "id": "4"
    }
  ]
}
```

The modify the application such that the initial state of the data is fetched from the server using the axiso-library. Complete the fetching with an Effect hook.



## d. Altering data in server

### Sending Data to the Server

```js
addNote = event => {
    event.preventDefault()
    const noteObject = {
        content: newNote,
        important: Math.random() < 0.5,
    }
    axios
    	.post('http://localhost:3000/note', noteObject)
    	.then(response => {
        	console.log(response)
    	}
    )
}
```

### Changing the Importance of Notes

```js
const Note = ({ note, toggleImportance }) => {
  const label = note.important
    ? 'make not important' : 'make important'

  return (
    <li>
      {note.content} 
      <button onClick={toggleImportance}>{label}</button>
    </li>
  )
}
```

```js
const App = () => {
  const [notes, setNotes] = useState([]) 
  const [newNote, setNewNote] = useState('')
  const [showAll, setShowAll] = useState(true)

  // ...


  const toggleImportanceOf = (id) => {
    console.log('importance of ' + id + ' needs to be toggled')
  }

  // ...

  return (
    <div>
      <h1>Notes</h1>
      <div>
        <button onClick={() => setShowAll(!showAll)}>
          show {showAll ? 'important' : 'all' }
        </button>
      </div>      
      <ul>
        {notesToShow.map(note => 
          <Note
            key={note.id}
            note={note} 

            toggleImportance={() => toggleImportanceOf(note.id)}
          />
        )}
      </ul>
      // ...
    </div>
  )
}
```

### Promises and Errors

```js
axios
	.get('http://example.com/probably_will_fail')
	.then(response => {
    	console.log('success')
	})
	.catch(error => {
    	console.log('fail')
	})

```

### Exercises 2.12 - 2.15

**2.12: The Phonebook step 7**

Currently, the numbers that are added to the phonebook are note saved to a bac

```js
axios
	.post('http://localhost:3000/persons', personObject)
	.then((response) => {
		setPersons(persons.concat(response.data));
})
```

**2.13: The Phonebook step 8**

Extract the code that handles the communication with the backend into its own module by following the example shown earlier in this part of the course material.

```js
import axios from "axios";
const baseUrl = "http://localhost:3000/persons";

const getAll = () => {
    return axios.get(baseUrl).then(response => response.data);
};

const create = (newPerson) => {
    return axios.post(baseUrl, newPerson).then(response => response.data);
};

const remove = (id) => {
    return axios.delete(`${baseUrl}/${id}`);
};

const update = (id, updatedPerson) => {
    return axios.put(`${baseUrl}/${id}`, updatedPerson).then(response => response.data);
};

export default {
    getAll,
    create,
    remove,
    update,
};
```

**2.14: The Phonebook step 9**

Make it possible for users to delete entries from the phonebook. The deletion can be done through a dedicated button for each person in the phonebook list. You can confirm the action from the user by using the window.confirm method

```js
const handleDeletePerson = (id, name) => {
    const confirmDelete = window.confirm(`Delete ${name}?`);
    if (!confirmDelete) return;
    personService.remove(id)
        .then(() => {
            setPersons(persons.filter(person => person.id !== id));
        })
        .catch(() => {
            alert(`The person '${name}' was already removed from server`);
            setPersons(persons.filter(person => person.id !== id));
        });
};
```

**2.15: The Phonebook step 10**

Change the functionality so that if a number is added to an already existing user, the new number will replace the old number. It's recommended to use the HTTP PUT method for updating the phone number.

```js
const addNewPerson = (event) => {
  event.preventDefault();

  const existingPerson = persons.find(person => person.name === newName);

  if (existingPerson) {
    const confirmUpdate = window.confirm(
      `${newName} is already added to the phonebook, replace the old number with a new one?`
    );

    if (confirmUpdate) {
      const updatedPerson = { ...existingPerson, number: newNumber };

      personService.update(existingPerson.id, updatedPerson)
        .then(returnedPerson => {
          setPersons(persons.map(p =>
            p.id !== existingPerson.id ? p : returnedPerson
          ));
          setNewName("");
          setNewNumber("");
        })
        .catch(error => {
          alert(`The person '${newName}' was already removed from server`);
          setPersons(persons.filter(p => p.id !== existingPerson.id));
        });
    }

    return;
  }

  // New person logic
  const personObject = { name: newName, number: newNumber };

  personService.create(personObject).then(returnedPerson => {
    setPersons(persons.concat(returnedPerson));
    setNewName("");
    setNewNumber("");
  });
};
```

## e. Adding styles to React app

### Inline styles

React also makes it possible to write syles directly in the code as so-called inline styles.

Let's add a footer component, Footer, to our application and define inline styles for it. The component is defined in the file `components/Footer.jsx` and used in the file `App.jsx` as follows:
```js
const Footer = () => {
  const footerStyle = {
    color: 'green',
    fontStyle: 'italic'
  }

  return (
    <div style={footerStyle}>
      <br />
      <p>
        Note app, Department of Computer Science, University of Helsinki 2025
      </p>
    </div>
  )
}

export default Footer
```

```js
import { useState, useEffect } from 'react'

import Footer from './components/Footer'
import Note from './components/Note'
import Notification from './components/Notification'
import noteService from './services/notes'

const App = () => {
  // ...

  return (
    <div>
      <h1>Notes</h1>

      <Notification message={errorMessage} />

      // ...  


      <Footer />
    </div>
  )
}
```

