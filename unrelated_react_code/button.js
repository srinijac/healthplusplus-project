class Button{
  constructor(props){
    this.props = props
    self.state = {
      text: "this button has not been clicked"
    }
  }
  render(){
    return <button classname = "Button" onClick = ()=>{
      self.state.text = "this button got clicked!"
    }>testing button here. The test says: {self.state.text} </button>
  }
}

const cont = document.querySelector('#reactButton');
reactDOM.render(Button)
