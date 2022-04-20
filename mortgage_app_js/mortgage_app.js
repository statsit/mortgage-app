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

class Mortgage extends Connection {
    constructor(host, 
                dbName, 
                user, 
                password,
                 port,
                 lastMonth,
                 principal,
                 rate,
                 payment) {
        this.lastMonth = lastMonth;
        this.principal = principal;
        this.rate = rate;
        this.payment = payment;
        super(host, dbName, user, password, port);
    }
    
    setMonthPayment(date, amount) {
        if (this.getBalance() > 0) {
             this.principal = this.getBalance()
             
        }
    }
    getBalance() {
        return 0

    }
    insertDbResult(result) {

    }
    
}