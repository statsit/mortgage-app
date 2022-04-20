const PRINCIPAL = 54500000
const RATE = 0.15
let mortgage = {
    // Initialize the mortgage object
    principal: PRINCIPAL,
    rate: RATE,
    monthPaymentFn: function (date, amount) {
        let interest = (this.rate * this.principal)/12
        let principalPusInterest = this.principal + interest
        let balance = this.principal - amount
        return {
            'date': date,
            'amount': amount,
            'interest': interest,
            'principalPusInterest': principalPusInterest,
            'balance': balance
        }
    }

}


let date = new Date(2019, 0, 1)
const amount = 700000
mort = mortgage.monthPaymentFn(date, amount)
document.querySelector('#header').innerHTML = `${mort.date.toLocaleDateString()}`
document.getElementById('balance').innerHTML = `$${mort.balance}.00`