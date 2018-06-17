import React from 'react';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import {withStyles} from '@material-ui/core/styles';
import {connect} from 'react-redux';
import * as actionCreators from '../../actions/auth';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';

import Bar from "../../../../top/components/Bar";
import {listItems, otherItems} from "./TeacherData";
import {BACKEND_API, BACKEND_SERVER_URL} from "../../config";

function mapStateToProps(state) {
    return {};
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}

const styles = theme => ({
    Card: {
        width: '100%',
        marginLeft: 'auto',
        marginRight: 'auto',
        height: '50%',
    },
});


class TeacherView extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            name: '',
        };
    }

    componentDidMount() {
        let url = BACKEND_SERVER_URL + BACKEND_API.get_faculty_info + localStorage.getItem('username') + '/';
        fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': 'JWT ' + localStorage.getItem('token'),
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                return response.json();
            })
            .then((data) => {
                this.setState({
                    name: data.name,
                });
            })
            .catch(() => {
            });
    }

    render() {
        const {classes, theme, history} = this.props;
        const {name} = this.state;
        return (
            <Bar
                listItems={listItems}
                otherItems={otherItems}
                children={

                    <Card className={classes.Card}>
                        <CardContent>
                            <Typography variant="display1" gutterBottom>{'欢迎来到教务管理系统, ' + name}</Typography>
                        </CardContent>
                    </Card>
                }
                history={history}
            />

        );
    }
}

TeacherView.propType = {
    classes: PropTypes.object.isRequired,
    theme: PropTypes.object.isRequired,
};


export default withStyles(styles, {withTheme: true})(connect(mapStateToProps, mapDispatchToProps)(TeacherView));


