import React, { Component } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label

} from "reactstrap";

export default class CustomModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeItem: this.props.activeItem
        };
    }
    handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
            value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
    };
    render() {
        const { toggle, onSave } = this.props;
        return (
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}>Add new post</ModalHeader>
                <ModalBody>
                    <Form>
                        <FormGroup>
                            <Label for="id">Post ID</Label>
                            <Input
                              type="text"
                              name="id"
                              value={this.state.activeItem.id}
                              onChange={this.handleChange}
                              placeholder="Enter ID"
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label for="userId">User ID</Label>
                            <Input
                              type="text"
                              name="userId"
                              value={this.state.activeItem.userId}
                              onChange={this.handleChange}
                              placeholder="Enter User ID"
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label for="title">Title</Label>
                            <Input
                              type="text"
                              name="title"
                              value={this.state.activeItem.title}
                              onChange={this.handleChange}
                              placeholder="Enter Title"
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label for="body">Body</Label>
                            <Input
                            type="text"
                            name="body"
                            value={this.state.activeItem.body}
                            onChange={this.handleChange}
                            placeholder="Enter body"
                            />
                        </FormGroup>

                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                        Save
                    </Button>
                </ModalFooter>
            </Modal>
        );
    }
}