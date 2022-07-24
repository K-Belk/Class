let memeAccordion = document.getElementById('meme-accordion')

let sortData = (data) => {
    data.forEach(element => {
        createMemeAccordion(element)
    });
}

fetch('https://api.imgflip.com/get_memes')
    .then(response => response.json())
    .then(data => {
        sortData(data.data.memes)
    })
    
    let addAttributes = (element, attrs) => {
        for(let key in attrs) {
            element.setAttribute(key, attrs[key])
        }
    }

    let createAccordion = () => {
        let accordion = document.createElement('div')
        accordion.className = "accordion-item"
        return accordion
    }

    let createAccordionHeader = (data) => {
        let accordionHeader = document.createElement('h2')
        accordionHeader.className = "accordion-header"
        accordionHeader.id = `heading-${data.id}`
        return accordionHeader
    }
    
    let createAccordionButton = (data) => {
        let accordionButton = document.createElement('button')
        accordionButton.className = "accordion-button"
        accordionButton.type = "button"
        let buttonAttributes = {'data-bs-toggle': 'collapse', 'data-bs-target': `#collapse-${data.id}`, "aria-expanded": "true", "aria-controls": `collapse-${data.id}`}
        addAttributes(accordionButton, buttonAttributes)
        accordionButton.innerText = `${data.name}`
        return accordionButton
    }

    let createAccordionOuterBody = (data) => {
        let accordionOuterBody = document.createElement('div')
        accordionOuterBody.id = `collapse-${data.id}`
        accordionOuterBody.className = "accordion-collapse collapse"
        let outerBodyAtrributes = {'aria-labelledby': `heading-${data.id}`, 'data-bs-parent': "#meme-accordion"}
        addAttributes(accordionOuterBody, outerBodyAtrributes)
        return accordionOuterBody
    }

    let createAccordionInnerBody = () => {
        let accordionInnerBody = document.createElement('div')
        accordionInnerBody.className = 'accordian-body'
        return accordionInnerBody
    }

    let createFlexImage = (data) => {
        let flexImage = document.createElement('img')
        flexImage.className = 'img-fluid'
        flexImage.src = data.url
        flexImage.alt = data.name
        return flexImage
    } 
    
    let createMemeAccordion = (data) => {
        let accordion = createAccordion()
        let accordionHeader = createAccordionHeader(data)
        let accordionButton = createAccordionButton(data)
        let accordionOuterBody = createAccordionOuterBody(data)
        let accordionInnerBody = createAccordionInnerBody()
        let flexImage = createFlexImage(data)
        
        accordionInnerBody.appendChild(flexImage)
        accordionOuterBody.appendChild(accordionInnerBody)
        accordionHeader.appendChild(accordionButton)
        accordion.appendChild(accordionHeader)
        accordion.appendChild(accordionOuterBody)
        memeAccordion.appendChild(accordion)
    }