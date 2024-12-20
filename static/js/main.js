// readme = when you search and change the page, the searching intruppte
// so you neeed to acces the value search and paste it again and do the 
// output for the anouther pages 

// get search form and get links
let searchForm = document.getElementById('searchForm') //getiting form 
let pageLinks = document.getElementsByClassName("page-link") //getting all buttons

if (searchForm) { 
for (let i = 0; pageLinks.length > i; i++) { //searching for button clicked

pageLinks[i].addEventListener('click', function (e) {

      e.preventDefault() //prevent button from refresh the page and load another page

      // get data attribute
      let page = this.dataset.page // get button value, ex: page=1 ,page=prev,page=next,...

      console.log("PAGE:", page) //log that vallue in console

      // you have entir form from id='searchFomr' you can add html inside it 
      searchForm.innerHTML += `<input value=${page} name="page"  hidden />` //adding hide input , value set to that page you want to go 

      // submit form
      searchForm.submit() // after adding page to form, need to send information both searchquery and page you want to see
      })
      }
}

