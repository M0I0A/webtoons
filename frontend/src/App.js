import React from 'react'

import {BrowserRouter as Router, Route, Switch} from "react-router-dom"
import PrivateRoute from "./utils/PrivateRoute"
import { AuthProvider } from './context/AuthContext'

import Homepage from './views/Homepage'
import Registerpage from './views/Registerpage'
import Loginpage from './views/Loginpage'
import Navbar from './views/Navbar'
import WebtoonDetail from './views/WebtoonDetail';
import FavoritesPage from './views/FavoritesPage'



function App() {
  return (
    <Router>
      <AuthProvider>
        < Navbar/>
        <Switch>
          <PrivateRoute component={FavoritesPage} path="/favorite" exact />
          <Route component={Loginpage} path="/login" />
          <Route component={Registerpage} path="/register" exact />
          <Route component={Homepage} path="/" exact />
          <Route component={WebtoonDetail} path="/webtoons/:id"  />

        </Switch>
      </AuthProvider>
    </Router>
  )
}

export default App