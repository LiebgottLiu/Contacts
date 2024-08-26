import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import ContactForm from './ContactForm'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([])
  const [isModalopen, setIsModalOpen] = useState(false)
  const [currentContact, setCurrentContact] = useState({})

useEffect(() => {
  fetchContacts()
}, [])

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  };

  const closeModle = () => {
    setIsModalOpen(false)
    setCurrentContact({})
  }

  const openCreateModal = () => {
    if(!isModalopen){
      setIsModalOpen(true)
    }
  }

  const openEditModal = (contact) => {
    if(isModalopen) return
    setCurrentContact(contact)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModle()
    fetchContacts()
  }

  return <>
  <ContactList contacts = {contacts} updateCpmtact={openEditModal}  updateCallback={onUpdate}/>
  <button onClick={openCreateModal}>Create New Contance</button>
  {
    isModalopen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick = {closeModle}>&times;</span>
          <ContactForm existingContact={currentContact}  updateCallback={onUpdate}/>
        </div>
    </div>
  }
  
  </>
}

export default App
