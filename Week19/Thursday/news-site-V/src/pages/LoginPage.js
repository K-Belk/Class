import React from 'react'
import { Form, Button } from 'react-bootstrap'

const LoginPage = () => {

  const handleLogin = (event) => {
    event.preventDefault()
    const loginData = {
      email: event.target.email.value,
      password: event.target.password.value,
    }
    console.log(loginData)
  }

  return (
    <div>
    <Form onSubmit={handleLogin}>
      <Form.Group className="m-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="email" placeholder="Enter email" name='email' />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="m-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" name='password'/>
      </Form.Group>

      <Button className="mx-3" variant="primary" type="submit">
        Submit
      </Button>
    </Form>
    </div>
  )
}

export default LoginPage