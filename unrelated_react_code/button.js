class Button{
  constructor(props){
    this.props = props
    this.state = {
      text: "this button has not been clicked"
    }
  }
  render(){
    return <button classname = "Button" onClick = ()=>{
      this.state.text = "this button got clicked!"
    }>testing button here. The test says: {this.state.text} </button>
  }
}

const cont = document.querySelector('#reactButton');
reactDOM.render(React.createElement(Button), cont)
