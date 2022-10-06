const express = require('express')
const app = express()

app.use(express.json())

let book_details = []

app.post('/add_book', (req, res) => {
    let priv_id;
    if(book_details.length == 0){
        priv_id = 0
    }else{
        priv_id = book_details[book_details.length -1].id
    }
    
    let new_book_details = {
        "id" : priv_id + 1,
        'book_name' : req.body.book_name,
        'author' : req.body.author,
        'category' : req.body.category,
        'purchase_date' : req.body.purchase_date
    }
   
    book_details.push(new_book_details)
    res.send("Record inserted successfully")
})
app.get('/list_books', (req, res) => {
    res.send(book_details)
})

app.delete('/delete/:id', (req, res) => {
    let id = parseInt(req.params.id)
    let remain_books = book_details.filter((book_detail) => book_detail.id !== id)
    book_details = remain_books
    res.send("deleted successfully")
})

app.listen(3000, (req, res) => {
    console.log("Server is running")
})

