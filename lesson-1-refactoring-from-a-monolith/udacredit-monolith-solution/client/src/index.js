import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            customers: [],
            employees: []
        };
    }

    loadCustomers = () => {
        fetch("http://localhost:5001/api/customers")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        customers: result.customers,
                    });
                },
                (error) => {
                    this.setState({
                        error,
                    });
                }
            )
    }

    loadEmployees = () => {
        fetch("http://localhost:5000/api/employees")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        employees: result.employees,
                    });
                },
                (error) => {
                    this.setState({
                        error,
                    });
                }
            )
    }

    componentDidMount() {
        this.loadCustomers();
        this.loadEmployees();
    }

    render() {
        const {error, customers, employees} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else {
            return (
                <div>
                    <h1>UdaCredit Union</h1>
                    <h2>Customers</h2>
                    <ul>
                        {customers.map(customer => (
                            <li key={customer.name}>
                                {customer.name} - {customer.balance}
                            </li>
                        ))}
                    </ul>
                    <h2>Employees</h2>
                    <ul>
                        {employees.map(employee => (
                            <li key={employee.name}>
                                {employee.name} - {employee.email}
                            </li>
                        ))}
                    </ul>
                </div>
            );
        }
    }
}

ReactDOM.render(
    <App/>,
    document.getElementById('root')
);