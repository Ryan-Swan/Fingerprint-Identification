import React, { Component } from 'react';
import {Form, Container, Button, Checkbox, Header} from 'semantic-ui-react';

class Login extends Component {
  render() {
    return (
      <div className="login">
        <Container>
        	<div style={{"margin":"auto", "margin-top":"10px", "text-align": "center", "max-width":"300px"}}>
	        	<Header size="huge">Fingerprint Program</Header>
	        	<Form>
				    <Form.Field>
					    <label style={{"text-align": "left"}}>Username</label>
					    <input />
				   	</Form.Field>
				    <Form.Field>
					    <label  style={{"text-align": "left"}}>Password</label>
					    <input type="password" />
				    </Form.Field>
				    <Form.Field>
				    <Button type='submit'>Login</Button>
				    </Form.Field>
				    <Form.Field>
				    	<a href="#">Forgot Password</a>
				    	<div style={{"margin-top":"10px"}}><Checkbox label='Remember username' /></div>
				    </Form.Field>
				    <Form.Field>
					    
				    </Form.Field>
				    
				  </Form>
			  </div>
        </Container>
      </div>
    );
  }
}

export default Login;
