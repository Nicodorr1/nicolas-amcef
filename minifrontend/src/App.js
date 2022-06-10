import React, { Component } from "react"
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
    state = {
      activeItem: {
        id: "",
        userId: "",
        title: "",
        body: "",
      },
      postList: []
    };

    async componentDidMount() {
      try {
        const res = await fetch('http://localhost:8000/all_posts/');
        const postList = await res.json();
        this.setState({
          postList
        });
      } catch (e) {
        console.log(e);
    }
    }

    toggle = () => {
      this.setState({ modal: !this.state.modal });
    };


    handleSubmit = item => {
      this.toggle();
      if (item.id) {
        axios
          .put(`http://localhost:8000/add_post/`, item)
        return;
      }
      axios
        .post("http://localhost:8000/all_posts/", item)
    };

    createItem = () => {
      const item = {id: "", userId: "", title: "", body: "" };
      this.setState({  modal: !this.state.modal });
    };


    renderItems = () => {
      const { viewCompleted } = this.state;
      const newItems = this.state.postList.filter(
        item => item.completed === viewCompleted
      );
      return newItems.map(item => (
        <div key={item.id} className="col-xs-12 col-lg-4 col-md-6 mt-4 mb-4 card">
        <h4 className="group inner list-group-item-heading">{item.title}</h4>
        <p className="group inner list-group-item-text">{item.body}</p>
        <div className="row">
          <div className="col-xs-12 col-md-6">
            <a className="btn btn-info" href="#">
              Details
            </a>
          </div>
        </div>
      </div>
      ));
    };

    render() {
      return (
        <main className="content">

          <div className="container-fluid px-4 mt-4">
            <div className="">
                <button onClick={this.createItem} className="btn btn-success">Add post</button>
              </div>
            <div className="row gx-5">{this.renderItems()}</div>
          </div>

        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ): null}
      </main>
      )
    }
  }

export default App;