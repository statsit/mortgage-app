class Connection {
    constructor(host, dbName, user, password, port) {
        this.host = host;
        this.dbName = dbName;
        this.user = user;
        this.password = password;
        this.port = port;
    }
    connect() {
        return `postgres://${this.user}:${this.password}@${this.host}:${this.port}/${this.dbName}`;
    }
}

class MortgageSimulator {
    constructor(principal, interestRate, startDate, monthlyPaymment, baseSaving, monthlyContribution) {
        this.principal = principal;
        this.interestRate = interestRate;
        this.startDate = startDate;
        this.monthlyPaymment = monthlyPaymment;
        this.baseSaving = baseSaving;
        this.monthlyContribution = monthlyContribution;
        

    }

    addDays(date) {
        date.setDate(date.getDate() + 30);
        return date;
    }

    calculate() {
        let recPrincipal = [];
        let month = this.startDate.getMonth();
        let year = this.startDate.getFullYear();

        while (this.principal > 0) {
            let interest = (this.principal * this.interestRate)/12;
            this.principal = (this.principal + interest) - this.monthlyPaymment
            this.baseSaving += this.monthlyContribution
            // recPrincipal.push(this.principal);
            // date.push(this.startDate);

            recPrincipal.push(
                {
                    date: this.startDate, 
                    principal: this.principal,
                    saving: this.baseSaving
                }
                    )
            if (month === 11) {
                month = 0;
                year += 1;
                this.startDate = new Date(year, month, 2);
            }
            else {
                month += 1;
                this.startDate = new Date(year, month, 2);
            }
        }
        // console.log(recPrincipal.length, recPrincipal.length/12)

        return recPrincipal;
    }
};

let principal = document.getElementById('principal').value;
let interestRate = document.getElementById('interestRate').value;
let startDate = document.getElementById('date').value;
let baseSaving = document.getElementById('basesaving').value;

console.log(typeof principal)
console.log(typeof startDate)


let m = new MortgageSimulator(48000000, 0.15, new Date(2023, 3, 2), 1500000, 55000,2000);
let res = m.calculate();

const table = document.createElement('table');
const header = document.createElement('tr');
header.innerHTML = `<th>Date</th><th>Principal</th><th>Saving</th>`
table.appendChild(header);

res.forEach((item) => {
    const row = document.createElement('tr');
    row.innerHTML = `
    <td>${item.date.toLocaleDateString()}</td>
    <td>$${item.principal.toFixed(2)}</td>
    <td>$${item.saving}.00</td>
    `
    table.appendChild(row);
})

document.body.appendChild(table);

// console.table(m.calculate())

console.log(principal)
