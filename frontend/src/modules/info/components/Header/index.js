import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import {AppBar,Drawer ,MenuItem,FlatButton,Divider} from 'material-ui';

import PropTypes from 'prop-types';


import * as actionCreators from '../../actions/auth';

function mapStateToProps(state) {
    return {
        
        isAuthenticated: state.info.auth.isAuthenticated,
        token: state.info.auth.token,
        userName: state.info.auth.userName,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}



class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {
            open: false,
        };

    }

    dispatchNewRoute(route) {
        BrowserRouter.push(route);
        this.setState({
            open: false,
        });

    }


    handleClickOutside() {
        this.setState({
            open: false,
        });
    }


    logout(e) {
        e.preventDefault();
        this.props.logoutAndRedirect();
        this.setState({
            open: false,
        });
    }

    openNav() {
        this.setState({
            open: true,
        });
    }

    render() {
        return (
            <header>
                <Drawer docked={false} open={this.state.open}>
                    {

                        !this.props.isAuthenticated ?
                            <div>
                                
                                <MenuItem onClick={() => this.dispatchNewRoute('/login')}>
                                    Login
                                </MenuItem>

                                {/*<MenuItem onClick={() => this.dispatchNewRoute('/register')}>*/}
                                    {/*Register*/}
                                {/*</MenuItem>*/}
                                {/*<MenuItem onClick={() => this.dispatchNewRoute('/analytics')}>*/}
                                    {/*Analytics*/}
                                {/*</MenuItem>*/}

                            </div>
                            :
                            <div>

                                {/*<MenuItem onClick={() => this.dispatchNewRoute('/analytics')}>*/}
                                    {/*Analytics*/}
                                {/*</MenuItem>*/}
                                <AppBar
                                    title="Information Management System"
                                />

                                <MenuItem onClick={(e) => this.logout(e)}>
                                    Logout
                                </MenuItem>
                            </div>
                    }
                </Drawer>
                {/*<AppBar*/}
                    {/*title="Information Management System"*/}
                {/*/>*/}
                {/*<AppBar*/}
                  {/*title="Information Management System"*/}
                  {/*onLeftIconButtonTouchTap={() => this.openNav()}*/}
                  {/*iconElementRight={*/}
                      {/*<FlatButton label="Home" onClick={() => this.dispatchNewRoute('/')} />*/}
                    {/*}*/}
                {/*/>*/}
            </header>

        );
    }
}

Header.propTypes = {
    logoutAndRedirect: PropTypes.func,
    isAuthenticated: PropTypes.bool,
};
export default connect(mapStateToProps, mapDispatchToProps)(Header);

